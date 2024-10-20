# CreateCommercialOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_entity_id** | **int** |  | [optional] 
**client_legal_entity_id** | **int** |  | [optional] 

## Example

```python
from prizz_extranet.models.create_commercial_offer import CreateCommercialOffer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommercialOffer from a JSON string
create_commercial_offer_instance = CreateCommercialOffer.from_json(json)
# print the JSON string representation of the object
print(CreateCommercialOffer.to_json())

# convert the object into a dict
create_commercial_offer_dict = create_commercial_offer_instance.to_dict()
# create an instance of CreateCommercialOffer from a dict
create_commercial_offer_from_dict = CreateCommercialOffer.from_dict(create_commercial_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


