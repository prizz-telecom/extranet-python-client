# InvoiceSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**legal_entity_id** | **str** |  | [optional] 
**client_legal_entity_id** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 

## Example

```python
from prizz_extranet.models.invoice_search import InvoiceSearch

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceSearch from a JSON string
invoice_search_instance = InvoiceSearch.from_json(json)
# print the JSON string representation of the object
print(InvoiceSearch.to_json())

# convert the object into a dict
invoice_search_dict = invoice_search_instance.to_dict()
# create an instance of InvoiceSearch from a dict
invoice_search_from_dict = InvoiceSearch.from_dict(invoice_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


