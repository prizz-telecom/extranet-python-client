# AddServiceContractComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**thread_id** | **int** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.add_service_contract_comment import AddServiceContractComment

# TODO update the JSON string below
json = "{}"
# create an instance of AddServiceContractComment from a JSON string
add_service_contract_comment_instance = AddServiceContractComment.from_json(json)
# print the JSON string representation of the object
print(AddServiceContractComment.to_json())

# convert the object into a dict
add_service_contract_comment_dict = add_service_contract_comment_instance.to_dict()
# create an instance of AddServiceContractComment from a dict
add_service_contract_comment_from_dict = AddServiceContractComment.from_dict(add_service_contract_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


