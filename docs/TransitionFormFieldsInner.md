# TransitionFormFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 
**values** | [**List[TransitionFormFieldsInnerValuesInner]**](TransitionFormFieldsInnerValuesInner.md) |  | [optional] 
**type** | **str** |  | [optional] 
**help** | **str** |  | [optional] 
**multiple** | **bool** |  | [optional] 
**expanded** | **bool** |  | [optional] 

## Example

```python
from prizz_extranet.models.transition_form_fields_inner import TransitionFormFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransitionFormFieldsInner from a JSON string
transition_form_fields_inner_instance = TransitionFormFieldsInner.from_json(json)
# print the JSON string representation of the object
print(TransitionFormFieldsInner.to_json())

# convert the object into a dict
transition_form_fields_inner_dict = transition_form_fields_inner_instance.to_dict()
# create an instance of TransitionFormFieldsInner from a dict
transition_form_fields_inner_from_dict = TransitionFormFieldsInner.from_dict(transition_form_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


