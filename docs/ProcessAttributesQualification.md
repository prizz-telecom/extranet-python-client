# ProcessAttributesQualification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**ProcessAttributesQualificationValues**](ProcessAttributesQualificationValues.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.process_attributes_qualification import ProcessAttributesQualification

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessAttributesQualification from a JSON string
process_attributes_qualification_instance = ProcessAttributesQualification.from_json(json)
# print the JSON string representation of the object
print(ProcessAttributesQualification.to_json())

# convert the object into a dict
process_attributes_qualification_dict = process_attributes_qualification_instance.to_dict()
# create an instance of ProcessAttributesQualification from a dict
process_attributes_qualification_from_dict = ProcessAttributesQualification.from_dict(process_attributes_qualification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


