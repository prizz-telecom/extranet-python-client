# CommercialOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_workflows** | **List[str]** | liste des processus disponible pour l&#39;objet | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**notes** | **str** |  | [optional] 
**rc_total** | **Dict[str, int]** |  | [optional] 
**rc_total_str** | **Dict[str, str]** |  | [optional] 
**rc_vat_total** | **Dict[str, int]** |  | [optional] 
**rc_vat_total_str** | **Dict[str, str]** |  | [optional] 
**nrc_total** | **int** |  | [optional] 
**nrc_total_str** | **str** |  | [optional] 
**nrc_vat_total** | **int** |  | [optional] 
**nrc_vat_total_str** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**legal_entity** | [**LegalEntity**](LegalEntity.md) |  | [optional] 
**client_legal_entity** | [**ClientLegalEntity**](ClientLegalEntity.md) |  | [optional] 
**sign_date** | **datetime** |  | [optional] 
**submit_date** | **datetime** |  | [optional] 
**delivery_delay** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**total_str** | **str** |  | [optional] 
**vat_total** | **int** |  | [optional] 
**vat_total_str** | **str** |  | [optional] 
**section_names** | **str** |  | [optional] 
**vat_detail** | [**List[CommercialOfferVatDetailInner]**](CommercialOfferVatDetailInner.md) |  | [optional] 
**vat_detail_str** | [**List[CommercialOfferVatDetailStrInner]**](CommercialOfferVatDetailStrInner.md) |  | [optional] 
**sections** | [**List[CommercialOfferSection]**](CommercialOfferSection.md) |  | [optional] 
**contacts** | [**List[Contact]**](Contact.md) |  | [optional] 
**configured_contacts** | [**List[TypedContact]**](TypedContact.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.commercial_offer import CommercialOffer

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialOffer from a JSON string
commercial_offer_instance = CommercialOffer.from_json(json)
# print the JSON string representation of the object
print(CommercialOffer.to_json())

# convert the object into a dict
commercial_offer_dict = commercial_offer_instance.to_dict()
# create an instance of CommercialOffer from a dict
commercial_offer_from_dict = CommercialOffer.from_dict(commercial_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


