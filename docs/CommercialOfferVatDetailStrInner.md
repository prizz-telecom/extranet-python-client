# CommercialOfferVatDetailStrInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vat** | **float** | taux de tva | [optional] 
**total_without_taxes** | **str** | total HT pour cette tva | [optional] 
**total** | **str** | montant pour cette tva | [optional] 

## Example

```python
from prizz_extranet.models.commercial_offer_vat_detail_str_inner import CommercialOfferVatDetailStrInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialOfferVatDetailStrInner from a JSON string
commercial_offer_vat_detail_str_inner_instance = CommercialOfferVatDetailStrInner.from_json(json)
# print the JSON string representation of the object
print(CommercialOfferVatDetailStrInner.to_json())

# convert the object into a dict
commercial_offer_vat_detail_str_inner_dict = commercial_offer_vat_detail_str_inner_instance.to_dict()
# create an instance of CommercialOfferVatDetailStrInner from a dict
commercial_offer_vat_detail_str_inner_from_dict = CommercialOfferVatDetailStrInner.from_dict(commercial_offer_vat_detail_str_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


