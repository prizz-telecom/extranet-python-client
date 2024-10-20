# Service


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**unit_price_discount** | **int** |  | [optional] 
**unit_price_discount_str** | **str** |  | [optional] 
**house_number** | **int** |  | [optional] 
**house_number_complement** | **str** |  | [optional] 
**street_name** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**city_name** | **str** |  | [optional] 
**insee_code** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**attributes** | **object** |  | [optional] 
**quantity** | **int** |  | [optional] 
**unit_price** | **int** |  | [optional] 
**unit_price_str** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**vat** | **str** |  | [optional] 
**recurrence** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**projection** | **str** |  | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**status** | **str** |  | [optional] 
**subscription_date** | **datetime** |  | [optional] 
**activation_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**termination_date** | **datetime** |  | [optional] 
**service_contract_id** | **int** |  | [optional] 
**paid_until** | **datetime** |  | [optional] 

## Example

```python
from prizz_extranet.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print(Service.to_json())

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_from_dict = Service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


