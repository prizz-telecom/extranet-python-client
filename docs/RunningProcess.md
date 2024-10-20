# RunningProcess


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
from prizz_extranet.models.running_process import RunningProcess

# TODO update the JSON string below
json = "{}"
# create an instance of RunningProcess from a JSON string
running_process_instance = RunningProcess.from_json(json)
# print the JSON string representation of the object
print(RunningProcess.to_json())

# convert the object into a dict
running_process_dict = running_process_instance.to_dict()
# create an instance of RunningProcess from a dict
running_process_from_dict = RunningProcess.from_dict(running_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


