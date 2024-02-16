import requests
import json
import example1

# Pros: High throughput, easy memory management, because we are downloading a file

# Cons: Difficult to do for columnar file formats, as entire blocks need to be downloaded 
#       before they can be deserialised to rows. Sometimes, the code is complex too.

# In a jsonl file each line is a json document, or a “row” of data, so we yield them as they get downloaded. 
# This allows us to download one row and process it before getting the next row.

def stream_download_jsonl(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    for line in response.iter_lines():
        if line:
            yield json.loads(line)


def download_and_yield_rows(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an HTTPError for bad responses

    for line in response.iter_lines():
        if line:
            yield json.loads(line)

# Replace the URL with your actual URL
url = "https://storage.googleapis.com/dtc_zoomcamp_api/yellow_tripdata_2009-06.jsonl"

# Use the generator to iterate over rows with minimal memory usage
for row in download_and_yield_rows(url):
    # Process each row as needed
    print(row)