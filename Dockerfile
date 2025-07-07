FROM python:3.11-slim

WORKDIR /app

COPY app.py .

# Run the script
CMD ["python", "app.py"]
