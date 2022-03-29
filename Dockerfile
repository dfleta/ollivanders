# For more information, please refer to https://aka.ms/vscode-docker-python
# best Docker base image for your Python application: Debian slim buster
# https://pythonspeed.com/articles/base-image-python-docker-images/
FROM python:3.8-slim-buster

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /ollivander
COPY . /ollivander

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /ollivander
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# controller:app => fichero_con_instancia_flask:variable_flask
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
