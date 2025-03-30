# Storybook Webhook Service

A Flask application that handles webhook requests from Storybook.

## Directory Structure

```
├── app/
│   ├── __init__.py          # Flask app initialization
│   └── routes/
│       └── storybook_webhook.py  # Webhook routes
├── requirements.txt         # Dependencies
├── run.py                   # Application entry point
└── Dockerfile               # Container configuration
```

## Development

### Setup

1. Create a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python run.py
   ```

## Docker Deployment

1. Build the Docker image:

   ```
   docker build -t storybook-webhook-service .
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 storybook-webhook-service
   ```

## API Endpoints

- `POST /webhook/storybook`: Main webhook endpoint for Storybook
- `GET /webhook/health`: Health check endpoint
