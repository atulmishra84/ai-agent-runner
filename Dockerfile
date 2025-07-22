
FROM mcr.microsoft.com/playwright/python:v1.44.0-focal

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN playwright install --with-deps

EXPOSE 7860
CMD ["python", "app.py"]
