FROM python
EXPOSE 80
EXPOSE 8000
RUN mkdir /code
RUN apt-get update
RUN apt install -y nginx && apt install -y ufw
RUN ufw allow 'Nginx HTTP'
WORKDIR /code
COPY . /code/
COPY requirements.txt /code/
RUN mkdir /usr/share/nginx/html/static
COPY /static/ /usr/share/nginx/html/static
RUN rm -f /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/

RUN pip install -r requirements.txt
COPY init.sh /code/init.sh
CMD ["./init.sh"]
   
# docker build --no-cache  --rm -t yema-backend .
# docker tag yema-backend:latest alejandro180192/yema-back:latest
# docker push alejandro180192/yema-back:latest

# docker run -d -p 80:80 -p 8000:8000 --name yema-backend yema-backend
# docker exec -it ID-CONTAINER bash
# docker ps
# docker container stop 3426914376a2
# docker container rm 3426914376a2
# docker login