FROM python:3.6-alpine
# RUN echo First Build Docker images
WORKDIR /app
ADD . /app/www
# COPY . /app
COPY . .
RUN pip -V
RUN python3 -V
RUN pip3 install flask
# RUN python3 server.py  จะค้างถ้าทำงี้
EXPOSE 5001
 CMD ["python3","server.py"] 
 #CMD จะรันต่อเมื่อรัน image แล้ว