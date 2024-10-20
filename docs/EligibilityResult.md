# EligibilityResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**tech** | **int** |  | [optional] 
**delivery** | **int** |  | [optional] 
**grt_min** | **int** |  | [optional] 
**grt_max** | **int** |  | [optional] 
**grt_non_working_hours_option_available** | **bool** |  | [optional] 
**grt_non_working_hours_option_mandatory** | **bool** |  | [optional] 
**nrc_min** | **int** |  | [optional] 
**nrc_max** | **int** |  | [optional] 
**commitment_min** | **int** |  | [optional] 
**commitment_max** | **int** |  | [optional] 
**upload_min** | **int** |  | [optional] 
**upload_max** | **int** |  | [optional] 
**download_min** | **int** |  | [optional] 
**download_max** | **int** |  | [optional] 
**guaranteed_upload_min** | **int** |  | [optional] 
**guaranteed_upload_max** | **int** |  | [optional] 
**guaranteedd_download_min** | **int** |  | [optional] 
**guaranteedd_download_max** | **int** |  | [optional] 
**rc_min** | **int** |  | [optional] 
**rc_max** | **int** |  | [optional] 
**price_list_items_groups** | [**EligibilityResultPriceListItemsGroups**](EligibilityResultPriceListItemsGroups.md) |  | [optional] 
**offer_id** | **int** |  | [optional] 
**price_list_id** | **int** |  | [optional] 
**combinations** | [**List[EligibilityResultCombination]**](EligibilityResultCombination.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.eligibility_result import EligibilityResult

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityResult from a JSON string
eligibility_result_instance = EligibilityResult.from_json(json)
# print the JSON string representation of the object
print(EligibilityResult.to_json())

# convert the object into a dict
eligibility_result_dict = eligibility_result_instance.to_dict()
# create an instance of EligibilityResult from a dict
eligibility_result_from_dict = EligibilityResult.from_dict(eligibility_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


