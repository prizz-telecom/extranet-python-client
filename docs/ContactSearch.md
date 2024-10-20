# ContactSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**phone1** | **str** |  | [optional] 
**phone2** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.contact_search import ContactSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ContactSearch from a JSON string
contact_search_instance = ContactSearch.from_json(json)
# print the JSON string representation of the object
print(ContactSearch.to_json())

# convert the object into a dict
contact_search_dict = contact_search_instance.to_dict()
# create an instance of ContactSearch from a dict
contact_search_from_dict = ContactSearch.from_dict(contact_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


