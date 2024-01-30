FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY ingestConn.py ingestConn.py 
COPY green_tripdata_2019-09.csv green_tripdata_2019-09.csv

ENTRYPOINT [ "python", "ingestConn.py" ]