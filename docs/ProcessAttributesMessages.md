# ProcessAttributesMessages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operateur** | [**List[ProcessMessage]**](ProcessMessage.md) |  | [optional] 
**noc** | [**List[ProcessMessage]**](ProcessMessage.md) |  | [optional] 
**terrain** | [**List[ProcessMessage]**](ProcessMessage.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.process_attributes_messages import ProcessAttributesMessages

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessAttributesMessages from a JSON string
process_attributes_messages_instance = ProcessAttributesMessages.from_json(json)
# print the JSON string representation of the object
print(ProcessAttributesMessages.to_json())

# convert the object into a dict
process_attributes_messages_dict = process_attributes_messages_instance.to_dict()
# create an instance of ProcessAttributesMessages from a dict
process_attributes_messages_from_dict = ProcessAttributesMessages.from_dict(process_attributes_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


