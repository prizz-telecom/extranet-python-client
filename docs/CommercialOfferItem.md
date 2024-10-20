# CommercialOfferItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_workflows** | **List[str]** | liste des processus disponible pour l&#39;objet | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**unit_price** | **int** |  | [optional] 
**unit_price_str** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**vat** | **str** |  | [optional] 
**recurrence** | **str** |  | [optional] 
**unit_price_discount** | **int** |  | [optional] 
**unit_price_discount_str** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
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
**price** | **int** |  | [optional] 
**section_id** | **int** |  | [optional] 
**commercial_offer_id** | **int** |  | [optional] 
**price_str** | **str** |  | [optional] 
**vat_rate** | **float** |  | [optional] 
**commercial_code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**to_estimate** | **bool** |  | [optional] 
**price_list_item** | [**PriceListItem**](PriceListItem.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.commercial_offer_item import CommercialOfferItem

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialOfferItem from a JSON string
commercial_offer_item_instance = CommercialOfferItem.from_json(json)
# print the JSON string representation of the object
print(CommercialOfferItem.to_json())

# convert the object into a dict
commercial_offer_item_dict = commercial_offer_item_instance.to_dict()
# create an instance of CommercialOfferItem from a dict
commercial_offer_item_from_dict = CommercialOfferItem.from_dict(commercial_offer_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


