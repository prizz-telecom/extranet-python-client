# TicketAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.ticket_attachment import TicketAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of TicketAttachment from a JSON string
ticket_attachment_instance = TicketAttachment.from_json(json)
# print the JSON string representation of the object
print(TicketAttachment.to_json())

# convert the object into a dict
ticket_attachment_dict = ticket_attachment_instance.to_dict()
# create an instance of TicketAttachment from a dict
ticket_attachment_from_dict = TicketAttachment.from_dict(ticket_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


