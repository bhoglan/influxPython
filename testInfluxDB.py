from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "testBucket"

client = InfluxDBClient(url="http://influxdb.briantheimpaler.com:8086", token="WUMGlb-JuByF5BvpbECbel-2DlKb7usc37yELOGonUIsmvTAEo5CmGspp6FfY3WLD7rmqczOmdSMwCxuMcZFNg==", org="briantheimpaler.com")

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

p = Point("my_measurement").tag("location", "Outside").field("temperature", 25.3)

write_api.write(bucket=bucket, record=p)

## Using table structure
tables = query_api.query('from(bucket:"testBucket") |> range(start: -10m)')

for table in tables:
    print(table)
    for row in table.records:
        print (row.values)

## Using csv library
csv_result = query_api.query_csv('from(bucket:"testBucket") |> range(start: -10m)')
val_count = 0
for row in csv_result:
    for cell in row:
        val_count +=1