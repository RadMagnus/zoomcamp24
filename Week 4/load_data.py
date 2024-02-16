import dlt
from example1 import paginated_getter
from example3 import stream_download_jsonl

# define the connection to load to.
# We now use duckdb, but you can switch to Bigquery later
generators_pipeline = dlt.pipeline(destination='duckdb', dataset_name='generators')


# we can load any generator to a table at the pipeline destnation as follows:
info = generators_pipeline.run(paginated_getter(),
										table_name="http_download",
										write_disposition="replace")

# the outcome metadata is returned by the load and we can inspect it by printing it.
print(info)

# # we can load the next generator to the same or to a different table.
# info = generators_pipeline.run(stream_download_jsonl(url),
# 										table_name="stream_download",
# 										write_disposition="replace")

# print(info)