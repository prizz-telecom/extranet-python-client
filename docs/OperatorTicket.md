# OperatorTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero** | **str** |  | [optional] 
**date_creation** | **str** |  | [optional] 
**date_cloture** | **str** |  | [optional] 
**date_debut_incident** | **str** |  | [optional] 
**date_resolution** | **str** |  | [optional] 
**date_gtr** | **str** |  | [optional] 
**etat** | **str** |  | [optional] 
**running_workflows** | [**List[RunningProcess]**](RunningProcess.md) |  | [optional] 
**archived_workflows** | [**List[RunningProcess]**](RunningProcess.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.operator_ticket import OperatorTicket

# TODO update the JSON string below
json = "{}"
# create an instance of OperatorTicket from a JSON string
operator_ticket_instance = OperatorTicket.from_json(json)
# print the JSON string representation of the object
print(OperatorTicket.to_json())

# convert the object into a dict
operator_ticket_dict = operator_ticket_instance.to_dict()
# create an instance of OperatorTicket from a dict
operator_ticket_from_dict = OperatorTicket.from_dict(operator_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


