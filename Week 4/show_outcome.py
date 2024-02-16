# show outcome
import dlt
import duckdb

generators_pipeline = dlt.pipeline(destination='duckdb', dataset_name='generators')
conn = duckdb.connect(f"{generators_pipeline.pipeline_name}.duckdb")

# let's see the tables
conn.sql(f"SET search_path = '{generators_pipeline.dataset_name}'")
print('Loaded tables: ')
display(conn.sql("show tables"))

# and the data

print("\n\n\n http_download table below:")

rides = conn.sql("SELECT * FROM http_download").df()
display(rides)

print("\n\n\n stream_download table below:")

passengers = conn.sql("SELECT * FROM stream_download").df()
display(passengers)

# As you can see, the same data was loaded in both cases.