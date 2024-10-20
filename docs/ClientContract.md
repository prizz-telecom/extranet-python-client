# ClientContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**price_list** | [**PriceList**](PriceList.md) |  | [optional] 
**payment_term_days** | **int** |  | [optional] 
**vat_reverse_charge** | **bool** |  | [optional] 
**invoice_consolidation** | **bool** |  | [optional] 

## Example

```python
from prizz_extranet.models.client_contract import ClientContract

# TODO update the JSON string below
json = "{}"
# create an instance of ClientContract from a JSON string
client_contract_instance = ClientContract.from_json(json)
# print the JSON string representation of the object
print(ClientContract.to_json())

# convert the object into a dict
client_contract_dict = client_contract_instance.to_dict()
# create an instance of ClientContract from a dict
client_contract_from_dict = ClientContract.from_dict(client_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


