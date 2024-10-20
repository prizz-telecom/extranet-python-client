# Transition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**form_fields** | [**List[TransitionFormFieldsInner]**](TransitionFormFieldsInner.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.transition import Transition

# TODO update the JSON string below
json = "{}"
# create an instance of Transition from a JSON string
transition_instance = Transition.from_json(json)
# print the JSON string representation of the object
print(Transition.to_json())

# convert the object into a dict
transition_dict = transition_instance.to_dict()
# create an instance of Transition from a dict
transition_from_dict = Transition.from_dict(transition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


