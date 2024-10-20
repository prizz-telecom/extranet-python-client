# ClientLegalEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_workflows** | **List[str]** | liste des processus disponible pour l&#39;objet | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**house_number** | **int** |  | [optional] 
**house_number_complement** | **str** |  | [optional] 
**street_name** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**city_name** | **str** |  | [optional] 
**insee_code** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**num_vat_intracommunity** | **str** |  | [optional] 
**siren** | **str** |  | [optional] 
**code_ape** | **str** |  | [optional] 
**rcs** | **str** |  | [optional] 
**tel** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**projection** | **str** |  | [optional] 
**arcep_code** | **str** |  | [optional] 
**contacts** | [**List[Contact]**](Contact.md) |  | [optional] 
**configured_contacts** | [**List[TypedContact]**](TypedContact.md) |  | [optional] 
**contracts** | [**List[ClientContract]**](ClientContract.md) |  | [optional] 
**roles** | [**List[UserRole]**](UserRole.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.client_legal_entity import ClientLegalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ClientLegalEntity from a JSON string
client_legal_entity_instance = ClientLegalEntity.from_json(json)
# print the JSON string representation of the object
print(ClientLegalEntity.to_json())

# convert the object into a dict
client_legal_entity_dict = client_legal_entity_instance.to_dict()
# create an instance of ClientLegalEntity from a dict
client_legal_entity_from_dict = ClientLegalEntity.from_dict(client_legal_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


