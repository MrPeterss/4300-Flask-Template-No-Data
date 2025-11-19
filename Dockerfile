FROM python:3.10-slim

ENV CONTAINER_HOME=/var/www

# Copy requirements and install dependencies
COPY requirements.txt $CONTAINER_HOME/requirements.txt
RUN pip install --no-cache-dir -r $CONTAINER_HOME/requirements.txt

# Copy application files
COPY app.py models.py routes.py $CONTAINER_HOME/
COPY static/ $CONTAINER_HOME/static/
COPY templates/ $CONTAINER_HOME/templates/

# Set working directory
WORKDIR $CONTAINER_HOME


# Run the Flask application using gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]

