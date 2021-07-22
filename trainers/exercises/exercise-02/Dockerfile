FROM python:3.7.1-slim
LABEL maintainer="travisdent@godatadriven.com"
WORKDIR /app
COPY requirements.txt . 
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
