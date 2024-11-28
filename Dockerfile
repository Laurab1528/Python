
FROM python:3.11-slim


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


RUN pytest > result.log; tail -n 10 result.log


CMD ["python", "main.py"]
