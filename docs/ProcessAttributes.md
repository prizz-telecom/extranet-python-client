# ProcessAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verif_cablage_ok** | **bool** |  | [optional] 
**etat_voyants** | **str** |  | [optional] 
**qualification** | [**ProcessAttributesQualification**](ProcessAttributesQualification.md) |  | [optional] 
**customer_mails** | **List[str]** |  | [optional] 
**messages** | [**ProcessAttributesMessages**](ProcessAttributesMessages.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.process_attributes import ProcessAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessAttributes from a JSON string
process_attributes_instance = ProcessAttributes.from_json(json)
# print the JSON string representation of the object
print(ProcessAttributes.to_json())

# convert the object into a dict
process_attributes_dict = process_attributes_instance.to_dict()
# create an instance of ProcessAttributes from a dict
process_attributes_from_dict = ProcessAttributes.from_dict(process_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


