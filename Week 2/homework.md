# Note
The Code for the homework is located in the mage file directly:

# Question 1:
/workspaces/zoomcamp24/Week 2/mage-zoomcamp/magic-zoomcamp/data_loaders/load_taxi.py

# Question 2-5:
/workspaces/zoomcamp24/Week 2/mage-zoomcamp/magic-zoomcamp/transformers/green_transform.py

For Question 3:
I used data 
```python 
['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime']).dt.date 
```
to produce the answer.

However:
```python
# Question 3. Data Transformation:
# Makes no sense
# data = data['lpep_pickup_datetime'].date

# wrong parenthesis
# data('lpep_pickup_date') = data['lpep_pickup_datetime'].date

# This one works:
data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

# dt and date are not callable
#data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt().date()
```

# Question 6
The export code is located here: /workspaces/zoomcamp24/Week 2/mage-zoomcamp/magic-zoomcamp/data_exporters/taxi_to_gcs_partitioned_parquet.py