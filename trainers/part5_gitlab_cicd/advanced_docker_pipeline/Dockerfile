FROM python:3.7.1-slim

LABEL maintainer="travisdent@godatadriven.com"

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]
