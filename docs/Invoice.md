# Invoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_workflows** | **List[str]** | liste des processus disponible pour l&#39;objet | [optional] 
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**rc_total** | **Dict[str, int]** |  | [optional] 
**rc_total_str** | **Dict[str, str]** |  | [optional] 
**rc_vat_total** | **Dict[str, int]** |  | [optional] 
**rc_vat_total_str** | **Dict[str, str]** |  | [optional] 
**nrc_total** | **int** |  | [optional] 
**nrc_total_str** | **str** |  | [optional] 
**nrc_vat_total** | **int** |  | [optional] 
**nrc_vat_total_str** | **str** |  | [optional] 
**client_legal_entity** | [**ClientLegalEntity**](ClientLegalEntity.md) |  | [optional] 
**legal_entity** | [**LegalEntity**](LegalEntity.md) |  | [optional] 
**ref** | **str** |  | [optional] 
**month_period** | **int** |  | [optional] 
**year_period** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**total_str** | **str** |  | [optional] 
**total_vat** | **int** |  | [optional] 
**total_vat_str** | **str** |  | [optional] 
**details** | [**List[InvoiceDetail]**](InvoiceDetail.md) |  | [optional] 
**use_vat_reverse_charge** | **bool** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**submit_date** | **datetime** |  | [optional] 

## Example

```python
from prizz_extranet.models.invoice import Invoice

# TODO update the JSON string below
json = "{}"
# create an instance of Invoice from a JSON string
invoice_instance = Invoice.from_json(json)
# print the JSON string representation of the object
print(Invoice.to_json())

# convert the object into a dict
invoice_dict = invoice_instance.to_dict()
# create an instance of Invoice from a dict
invoice_from_dict = Invoice.from_dict(invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


