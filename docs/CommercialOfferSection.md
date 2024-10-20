# CommercialOfferSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_workflows** | **List[str]** | liste des processus disponible pour l&#39;objet | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**commercial_offer_id** | **int** |  | [optional] 
**client_reference** | **str** |  | [optional] 
**commercial_offer_items** | [**List[CommercialOfferItem]**](CommercialOfferItem.md) |  | [optional] 
**offer** | [**Offer**](Offer.md) |  | [optional] 
**service_contract** | [**ServiceContract**](ServiceContract.md) |  | [optional] 
**client_contract** | [**ClientContract**](ClientContract.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.commercial_offer_section import CommercialOfferSection

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialOfferSection from a JSON string
commercial_offer_section_instance = CommercialOfferSection.from_json(json)
# print the JSON string representation of the object
print(CommercialOfferSection.to_json())

# convert the object into a dict
commercial_offer_section_dict = commercial_offer_section_instance.to_dict()
# create an instance of CommercialOfferSection from a dict
commercial_offer_section_from_dict = CommercialOfferSection.from_dict(commercial_offer_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


