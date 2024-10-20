# EligibilityResultCombination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combination_id** | **str** |  | [optional] 
**total** | **int** |  | [optional] 
**total_without_nrc** | **int** |  | [optional] 
**nrc** | **int** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from prizz_extranet.models.eligibility_result_combination import EligibilityResultCombination

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityResultCombination from a JSON string
eligibility_result_combination_instance = EligibilityResultCombination.from_json(json)
# print the JSON string representation of the object
print(EligibilityResultCombination.to_json())

# convert the object into a dict
eligibility_result_combination_dict = eligibility_result_combination_instance.to_dict()
# create an instance of EligibilityResultCombination from a dict
eligibility_result_combination_from_dict = EligibilityResultCombination.from_dict(eligibility_result_combination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


