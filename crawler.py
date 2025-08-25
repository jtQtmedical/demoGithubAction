#!/usr/bin/env python3
"""
簡單的網站爬蟲範例
用於 GitHub Actions 自動化爬取資料
"""

import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
import time
import os

def crawl_website():
    """爬取網站資料"""
    try:
        # 設定 User-Agent 避免被擋
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # 範例：爬取 GitHub Trending 頁面
        url = "https://github.com/trending"
        print(f"🔄 開始爬取: {url}")
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()  # 檢查 HTTP 錯誤
        
        # 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取 trending repositories
        trending_repos = []
        repo_articles = soup.find_all('article', class_='Box-row')
        
        for article in repo_articles[:10]:  # 只取前 10 個
            try:
                # 提取 repository 名稱
                repo_link = article.find('h2', class_='h3 lh-condensed')
                if repo_link:
                    repo_name = repo_link.get_text(strip=True)
                    
                    # 提取描述
                    description_elem = article.find('p')
                    description = description_elem.get_text(strip=True) if description_elem else "無描述"
                    
                    # 提取語言
                    language_elem = article.find('span', {'itemprop': 'programmingLanguage'})
                    language = language_elem.get_text(strip=True) if language_elem else "未知"
                    
                    # 提取星數
                    stars_elem = article.find('a', href=lambda x: x and 'stargazers' in x)
                    stars = stars_elem.get_text(strip=True) if stars_elem else "0"
                    
                    trending_repos.append({
                        'name': repo_name,
                        'description': description,
                        'language': language,
                        'stars': stars,
                        'crawled_at': datetime.now().isoformat()
                    })
            except Exception as e:
                print(f"⚠️ 解析 repository 時出錯: {e}")
                continue
        
        return trending_repos
        
    except requests.RequestException as e:
        print(f"❌ 網路請求失敗: {e}")
        return None
    except Exception as e:
        print(f"❌ 爬蟲執行失敗: {e}")
        return None

def save_data(data, filename='trending_repos.json'):
    """儲存資料到檔案"""
    try:
        # 讀取現有資料（如果存在）
        existing_data = []
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        
        # 添加新資料
        if data:
            existing_data.append({
                'date': datetime.now().strftime('%Y-%m-%d'),
                'repos': data
            })
        
        # 只保留最近 30 天的資料
        if len(existing_data) > 30:
            existing_data = existing_data[-30:]
        
        # 儲存到檔案
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 資料已儲存到 {filename}")
        return True
        
    except Exception as e:
        print(f"❌ 儲存資料失敗: {e}")
        return False

def main():
    """主函數"""
    print(f"🚀 開始執行爬蟲: {datetime.now()}")
    
    # 爬取資料
    data = crawl_website()
    
    if data:
        print(f"📊 成功爬取 {len(data)} 個 trending repositories")
        
        # 儲存資料
        if save_data(data):
            print("✅ 爬蟲任務完成")
        else:
            print("❌ 儲存資料失敗")
            exit(1)
    else:
        print("❌ 爬蟲失敗")
        exit(1)

if __name__ == "__main__":
    main()