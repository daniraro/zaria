FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install streamlit==1.38.0 pandas==2.2.2 requests==2.32.3

COPY frontend/ ./frontend/

EXPOSE 8501

CMD ["streamlit", "run", "frontend/app.py", "--server.address", "0.0.0.0"]
