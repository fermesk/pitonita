FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV OPENAI_API_KEY = OPENAI_API_KEY
ENV TELEGRAM_BOT_TOKEN = TELEGRAM_API_KEY

CMD ["python", "./potinita.py"]