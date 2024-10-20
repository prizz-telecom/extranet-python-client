# PricesListOffers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offers** | [**List[Offer]**](Offer.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.prices_list_offers import PricesListOffers

# TODO update the JSON string below
json = "{}"
# create an instance of PricesListOffers from a JSON string
prices_list_offers_instance = PricesListOffers.from_json(json)
# print the JSON string representation of the object
print(PricesListOffers.to_json())

# convert the object into a dict
prices_list_offers_dict = prices_list_offers_instance.to_dict()
# create an instance of PricesListOffers from a dict
prices_list_offers_from_dict = PricesListOffers.from_dict(prices_list_offers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


