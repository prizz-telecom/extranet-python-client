# InvoiceDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_workflows** | **List[str]** | liste des processus disponible pour l&#39;objet | [optional] 
**id** | **int** |  | [optional] 
**unit_price** | **int** |  | [optional] 
**unit_price_str** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**vat** | **str** |  | [optional] 
**recurrence** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**unit_price_discount** | **int** |  | [optional] 
**unit_price_discount_str** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
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
**amount** | **int** |  | [optional] 
**invoice_id** | **int** |  | [optional] 
**amount_str** | **str** |  | [optional] 
**va_trate** | **float** |  | [optional] 
**service_id** | **int** |  | [optional] 
**service_contract_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 

## Example

```python
from prizz_extranet.models.invoice_detail import InvoiceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetail from a JSON string
invoice_detail_instance = InvoiceDetail.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetail.to_json())

# convert the object into a dict
invoice_detail_dict = invoice_detail_instance.to_dict()
# create an instance of InvoiceDetail from a dict
invoice_detail_from_dict = InvoiceDetail.from_dict(invoice_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


