FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Install dependencies (with Werkzeug 2.0.1 first to avoid the url_quote error)
RUN pip install --no-cache-dir Werkzeug==2.0.1 && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"] 