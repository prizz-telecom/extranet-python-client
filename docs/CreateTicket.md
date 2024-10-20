# CreateTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero** | **str** |  | [optional] 
**ticket_id** | **int** |  | [optional] 
**running_process** | [**List[RunningProcess]**](RunningProcess.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.create_ticket import CreateTicket

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTicket from a JSON string
create_ticket_instance = CreateTicket.from_json(json)
# print the JSON string representation of the object
print(CreateTicket.to_json())

# convert the object into a dict
create_ticket_dict = create_ticket_instance.to_dict()
# create an instance of CreateTicket from a dict
create_ticket_from_dict = CreateTicket.from_dict(create_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


