FROM python:3.7

LABEL "project"="ACME" 
LABEL "maintainer"="foo"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python"]

CMD ["app.py"]
