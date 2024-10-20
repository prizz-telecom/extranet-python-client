# EligibilityHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**GetClientLegalEntities200ResponsePagination**](GetClientLegalEntities200ResponsePagination.md) |  | [optional] 
**items** | [**List[EligibilityHistory]**](EligibilityHistory.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.eligibility_history200_response import EligibilityHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityHistory200Response from a JSON string
eligibility_history200_response_instance = EligibilityHistory200Response.from_json(json)
# print the JSON string representation of the object
print(EligibilityHistory200Response.to_json())

# convert the object into a dict
eligibility_history200_response_dict = eligibility_history200_response_instance.to_dict()
# create an instance of EligibilityHistory200Response from a dict
eligibility_history200_response_from_dict = EligibilityHistory200Response.from_dict(eligibility_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


