import pyarrow as pa
import pyarrow.parquet as pq
from pandas import DataFrame
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/dtc-de-412312-3abec3b29a44.json'
project_id = 'dtc-de-412312'
bucket_name = 'mage-zoomcamp-amal-1'
object_key = 'green_taxi_data.parquet'
table_name = 'green_taxi_data'
root_path = f'{bucket_name}/{table_name}'



@data_exporter
def export_data(data, *args, **kwargs):

    
    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )


