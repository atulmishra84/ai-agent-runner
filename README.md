
# Entra RPA Bot 🤖

An AI-powered RPA bot that automates user creation in Microsoft Entra using Playwright and Gradio.

## 🚀 Features

- Automates Microsoft Entra login and user creation
- Runs using Playwright in headless mode
- Triggered via Gradio web interface
- Screenshot preview of the RPA result
- Deployable via Docker or 1-click on Render

## 🧪 Local Development

```bash
pip install -r requirements.txt
playwright install
python app.py
```

## 🐳 Docker Deployment

```bash
docker build -t entra-rpa-bot .
docker run -p 7860:7860 entra-rpa-bot
```

## ☁️ 1-Click Deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

Or use this URL:

```
https://render.com/deploy?repo=https://github.com/<your-username>/entra-rpa-bot
```

## 📂 Project Structure

- app.py
- rpa_logic.py
- Dockerfile
- requirements.txt
- render.yaml
- .github/workflows/deploy.yml
