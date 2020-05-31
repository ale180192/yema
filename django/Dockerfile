FROM python:3.6
RUN mkdir /code
RUN apt-get update
WORKDIR /code
COPY . /code/
COPY requirements.txt /code/

RUN pip install -r requirements.txt
EXPOSE 9000
CMD ["gunicorn", "-b", ":9000", "app.wsgi"]
   
# docker build --no-cache  --rm -t yema-backend .
# docker tag yema-backend:latest alejandro180192/yema-back:latest
# docker push alejandro180192/yema-back:latest

# docker run -d -p 9000:9000 --name yema-backend yema-backend
# docker exec -it ID-CONTAINER bash
# docker ps
# docker container stop 3426914376a2
# docker container rm 3426914376a2
# docker login