# ArchivedProcess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**lib** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 
**create_date** | **str** |  | [optional] 
**process_class** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.archived_process import ArchivedProcess

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivedProcess from a JSON string
archived_process_instance = ArchivedProcess.from_json(json)
# print the JSON string representation of the object
print(ArchivedProcess.to_json())

# convert the object into a dict
archived_process_dict = archived_process_instance.to_dict()
# create an instance of ArchivedProcess from a dict
archived_process_from_dict = ArchivedProcess.from_dict(archived_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


