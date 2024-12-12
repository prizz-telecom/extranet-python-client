# GetEligibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wf** | **int** | Workflow id | [optional] 
**wfs** | **str** | Workflow status | [optional] 
**attrs** | **object** | Attributes of the workflow | [optional] 
**wftr** | **List[object]** | Workflow transitions history | [optional] 
**client** | [**ClientLegalEntity**](ClientLegalEntity.md) |  | [optional] 
**response** | [**List[EligibilityResult]**](EligibilityResult.md) | Eligibility results | [optional] 

## Example

```python
from prizz_extranet.models.get_eligibility import GetEligibility

# TODO update the JSON string below
json = "{}"
# create an instance of GetEligibility from a JSON string
get_eligibility_instance = GetEligibility.from_json(json)
# print the JSON string representation of the object
print(GetEligibility.to_json())

# convert the object into a dict
get_eligibility_dict = get_eligibility_instance.to_dict()
# create an instance of GetEligibility from a dict
get_eligibility_from_dict = GetEligibility.from_dict(get_eligibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


