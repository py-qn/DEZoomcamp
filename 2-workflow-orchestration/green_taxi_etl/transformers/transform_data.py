if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    # Remove rows where passenger count or trip distance is zero
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Create a new column lpep_pickup_date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Rename columns to Snake Case
    data.rename(columns={
        'VendorID': 'vendor_id',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id'
    }, inplace=True)


    return data


@test
def test_output(output, *args) -> None:
    
    assert output['vendor_id'].isin([1, 2]).all(), "Vendor ID should be either 1 or 2"
   
@test
def test_output(output, *args) -> None:
    assert (output['passenger_count'] > 0).all(), "Passenger count should be greater than 0"

@test
def test_output(output, *args) -> None:
    
    assert (output['trip_distance'] > 0).all(), "Trip distance should be greater than 0"    

