CREATE OR REPLACE EXTERNAL TABLE `dtc-de-412312.ny_taxy.external_green_trip`
OPTIONS (
  format = 'parquet',
  uris = ['gs://mage-zoomcamp-bucket1/green/green_tripdata_2022.parquet']
);

CREATE OR REPLACE TABLE `dtc-de-412312.ny_taxy.internal_green_trip`
AS SELECT * FROM `dtc-de-412312.ny_taxy.external_green_trip`;


SELECT COUNT(*)
FROM `dtc-de-412312.ny_taxy.external_green_trip` 
WHERE fare_amount = 0;

SELECT DISTINCT PULocationID
FROM `dtc-de-412312.ny_taxy.external_green_trip` 
WHERE lpep_pickup_datetime >= TIMESTAMP('2022-06-01')
AND lpep_pickup_datetime < TIMESTAMP('2022-07-01');

CREATE OR REPLACE TABLE `dtc-de-412312.ny_taxy.external_green_trip_partitioned`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PULocationID AS (
  SELECT * FROM `dtc-de-412312.ny_taxy.external_green_trip`
);


SELECT DISTINCT PULocationID
FROM `dtc-de-412312.ny_taxy.external_green_trip_partitioned` 
WHERE lpep_pickup_datetime >= TIMESTAMP('2022-06-01')
AND lpep_pickup_datetime < TIMESTAMP('2022-07-01');



