FROM python:3.9-slim

WORKDIR /app

# Copy shared modules from the current context (which should include them)
COPY ./shared_module /app/shared_module

# Copy service-specific code
COPY ./service_a /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]