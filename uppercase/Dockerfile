FROM python:3.9-slim
WORKDIR /app
COPY uppercase.py .
RUN pip install requests
CMD ["python", "-u", "uppercase.py"]
