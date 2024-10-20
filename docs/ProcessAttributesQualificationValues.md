# ProcessAttributesQualificationValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**date_debut_incident** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.process_attributes_qualification_values import ProcessAttributesQualificationValues

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessAttributesQualificationValues from a JSON string
process_attributes_qualification_values_instance = ProcessAttributesQualificationValues.from_json(json)
# print the JSON string representation of the object
print(ProcessAttributesQualificationValues.to_json())

# convert the object into a dict
process_attributes_qualification_values_dict = process_attributes_qualification_values_instance.to_dict()
# create an instance of ProcessAttributesQualificationValues from a dict
process_attributes_qualification_values_from_dict = ProcessAttributesQualificationValues.from_dict(process_attributes_qualification_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


