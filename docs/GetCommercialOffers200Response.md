# GetCommercialOffers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**GetClientLegalEntities200ResponsePagination**](GetClientLegalEntities200ResponsePagination.md) |  | [optional] 
**items** | [**List[CommercialOffer]**](CommercialOffer.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.get_commercial_offers200_response import GetCommercialOffers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommercialOffers200Response from a JSON string
get_commercial_offers200_response_instance = GetCommercialOffers200Response.from_json(json)
# print the JSON string representation of the object
print(GetCommercialOffers200Response.to_json())

# convert the object into a dict
get_commercial_offers200_response_dict = get_commercial_offers200_response_instance.to_dict()
# create an instance of GetCommercialOffers200Response from a dict
get_commercial_offers200_response_from_dict = GetCommercialOffers200Response.from_dict(get_commercial_offers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


