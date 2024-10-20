# ServiceContractNrc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**unit_price** | **int** |  | [optional] 
**unit_price_str** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**vat** | **str** |  | [optional] 
**recurrence** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**unit_price_discount** | **int** |  | [optional] 
**unit_price_discount_str** | **str** |  | [optional] 
**attributes** | **object** |  | [optional] 
**house_number** | **int** |  | [optional] 
**house_number_complement** | **str** |  | [optional] 
**street_name** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**city_name** | **str** |  | [optional] 
**insee_code** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**projection** | **str** |  | [optional] 
**service_contract_id** | **int** |  | [optional] 
**base_item_id** | **int** |  | [optional] 
**billed** | **bool** |  | [optional] 
**price** | **int** |  | [optional] 
**price_str** | **str** |  | [optional] 
**va_trate** | **float** |  | [optional] 
**commercial_code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.service_contract_nrc import ServiceContractNrc

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceContractNrc from a JSON string
service_contract_nrc_instance = ServiceContractNrc.from_json(json)
# print the JSON string representation of the object
print(ServiceContractNrc.to_json())

# convert the object into a dict
service_contract_nrc_dict = service_contract_nrc_instance.to_dict()
# create an instance of ServiceContractNrc from a dict
service_contract_nrc_from_dict = ServiceContractNrc.from_dict(service_contract_nrc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


