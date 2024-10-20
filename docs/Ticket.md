# Ticket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**operator_id** | **int** |  | [optional] 
**operator_name** | **str** |  | [optional] 
**numero** | **str** |  | [optional] 
**etat** | **str** |  | [optional] 
**etat_lib** | **str** |  | [optional] 
**titre** | **str** |  | [optional] 
**cust_name** | **str** |  | [optional] 
**ref_commande** | **str** |  | [optional] 
**id_service_sicom** | **int** |  | [optional] 
**ref_service** | **str** |  | [optional] 
**cust_address** | **str** |  | [optional] 
**ref_tiers** | **str** |  | [optional] 
**date_creation** | **str** |  | [optional] 
**date_ouverture** | **str** |  | [optional] 
**date_resolution** | **str** |  | [optional] 
**date_cloture** | **str** |  | [optional] 
**last_message** | **str** |  | [optional] 
**running_process** | [**List[RunningProcess]**](RunningProcess.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.ticket import Ticket

# TODO update the JSON string below
json = "{}"
# create an instance of Ticket from a JSON string
ticket_instance = Ticket.from_json(json)
# print the JSON string representation of the object
print(Ticket.to_json())

# convert the object into a dict
ticket_dict = ticket_instance.to_dict()
# create an instance of Ticket from a dict
ticket_from_dict = Ticket.from_dict(ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


