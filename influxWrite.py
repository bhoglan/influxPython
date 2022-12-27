from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "outsideenviro"

self.client = InfluxDBClient.from_config_file("influxdb.ini")

write_api = self.client.write_api(write_options=SYNCHRONOUS)
query_api = self.client.query_api()

weatherDict = {
    "measurement": "weather",
    "tags": {"location": "outside", "device": "Enviro+"},
    "fields": {"temperature": temp},
    "fields": {"pressure": baro},
    "fields": {"humidity": humidity}
    }

gasDict = {
    "measurement": "gas",
    "tags": {"location": "outside", "device": "Enviro+"},
    "fields": {"oxidising": ox},
    "fields": {"reducing": red},
    "fields": {"nh3": nh3}
}

#particulateDict = {Placeholder}

write_api.write(bucket=bucket, record=weatherDict)
write_api.write(bucket=bucket, record=gasDict)

## Using table structure
tables = query_api.query('from(bucket:"testBucket") |> range(start: -10m)')

for table in tables:
    print(table)
    for row in table.records:
        print (row.values)

### Using csv library
#csv_result = query_api.query_csv('from(bucket:"testBucket") |> range(start: -10m)')
#val_count = 0
#for row in csv_result:
#    for cell in row:
#        val_count +=1