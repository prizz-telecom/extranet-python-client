# EligibilityHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**address** | **str** |  | [optional] 
**client** | [**ClientLegalEntity**](ClientLegalEntity.md) |  | [optional] 
**result** | [**List[EligibilityResult]**](EligibilityResult.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.eligibility_history import EligibilityHistory

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityHistory from a JSON string
eligibility_history_instance = EligibilityHistory.from_json(json)
# print the JSON string representation of the object
print(EligibilityHistory.to_json())

# convert the object into a dict
eligibility_history_dict = eligibility_history_instance.to_dict()
# create an instance of EligibilityHistory from a dict
eligibility_history_from_dict = EligibilityHistory.from_dict(eligibility_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


