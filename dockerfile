FROM python:3.9

WORKDIR /app

COPY . /app

# Create and activate the virtual environment
RUN python -m venv venv
RUN . venv/bin/activate

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Run the application
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]