FROM python:3.9-slim
WORKDIR /app
COPY inverse.py .
RUN pip install requests
CMD ["python", "-u", "inverse.py"]
