# CreateCommercialOffer201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**success** | **bool** |  | [optional] 
**last_log** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.create_commercial_offer201_response import CreateCommercialOffer201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommercialOffer201Response from a JSON string
create_commercial_offer201_response_instance = CreateCommercialOffer201Response.from_json(json)
# print the JSON string representation of the object
print(CreateCommercialOffer201Response.to_json())

# convert the object into a dict
create_commercial_offer201_response_dict = create_commercial_offer201_response_instance.to_dict()
# create an instance of CreateCommercialOffer201Response from a dict
create_commercial_offer201_response_from_dict = CreateCommercialOffer201Response.from_dict(create_commercial_offer201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


