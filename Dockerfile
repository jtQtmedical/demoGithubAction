# 使用官方 Node.js 18 映像
FROM node:18-alpine

# 設定工作目錄
WORKDIR /app

# 複製 package.json 和 package-lock.json
COPY node-demo/package*.json ./

# 安裝依賴
RUN npm ci --only=production

# 複製應用程式程式碼
COPY node-demo/ ./

# 暴露端口
EXPOSE 8080

# 啟動應用程式
CMD ["npm", "start"]