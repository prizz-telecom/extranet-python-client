# Process


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_id** | **int** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_class** | **str** |  | [optional] 
**process_class** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**state_lib** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**attrs** | [**ProcessAttributes**](ProcessAttributes.md) |  | [optional] 
**lib** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**states** | **List[object]** |  | [optional] 
**attachments** | [**List[TicketAttachment]**](TicketAttachment.md) |  | [optional] 
**actions** | [**List[ProcessAction]**](ProcessAction.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.process import Process

# TODO update the JSON string below
json = "{}"
# create an instance of Process from a JSON string
process_instance = Process.from_json(json)
# print the JSON string representation of the object
print(Process.to_json())

# convert the object into a dict
process_dict = process_instance.to_dict()
# create an instance of Process from a dict
process_from_dict = Process.from_dict(process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


