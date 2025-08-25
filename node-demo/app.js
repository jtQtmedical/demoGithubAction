import express from 'express';

const app = express();
const port = process.env.PORT || 8080;

// 設定基本路由
app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Node.js Demo App</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                color: white;
            }
            .container {
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                padding: 2rem;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }
            h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 1rem;
                opacity: 0.9;
            }
            .timestamp {
                font-size: 0.9rem;
                opacity: 0.7;
                margin-top: 2rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>�� Hello World!</h1>
            <p>歡迎來到 Node.js Demo 應用程式</p>
            <p>部署在 Google Cloud Run 上</p>
            <div class="timestamp">
                部署時間: ${new Date().toLocaleString('zh-TW')}
            </div>
        </div>
    </body>
    </html>
  `);
});

// 健康檢查端點
app.get('/health', (req, res) => {
  res.json({ 
    status: 'OK', 
    timestamp: new Date().toISOString(),
    environment: process.env.NODE_ENV || 'development'
  });
});

// 啟動伺服器
app.listen(port, () => {
  console.log(`🚀 伺服器運行在 http://localhost:${port}`);
  console.log(`📊 健康檢查: http://localhost:${port}/health`);
});