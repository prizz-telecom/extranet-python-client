# ServiceContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_workflows** | **List[str]** | liste des processus disponible pour l&#39;objet | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**canceled_reason** | **str** |  | [optional] 
**canceled_date** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**legal_entity_id** | **int** |  | [optional] 
**client_contract_id** | **int** |  | [optional] 
**subscription_date** | **datetime** |  | [optional] 
**activation_date** | **datetime** |  | [optional] 
**first_activation_date** | **datetime** |  | [optional] 
**offer** | [**Offer**](Offer.md) |  | [optional] 
**client** | [**ClientLegalEntity**](ClientLegalEntity.md) |  | [optional] 
**ref_client** | **str** | ref set by customer | [optional] 
**ref_service** | **str** | ref used by Prizz Telecom NOC | [optional] 
**description** | **str** |  | [optional] 
**services** | [**List[Service]**](Service.md) |  | [optional] 
**nrcs** | [**List[ServiceContractNrc]**](ServiceContractNrc.md) |  | [optional] 
**planned_activation_date** | **datetime** |  | [optional] 
**sold_activation_date** | **datetime** |  | [optional] 
**commitment_end_date** | **datetime** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**consolidated_attributes** | **Dict[str, object]** |  | [optional] 
**consolidated_attributes_staging_or_new** | **Dict[str, object]** |  | [optional] 
**commercial_offers** | [**List[ServiceContractCommercialOffersInner]**](ServiceContractCommercialOffersInner.md) |  | [optional] 
**contacts** | [**List[Contact]**](Contact.md) |  | [optional] 
**configured_contacts** | [**List[TypedContact]**](TypedContact.md) |  | [optional] 
**replaces** | **int** |  | [optional] 

## Example

```python
from prizz_extranet.models.service_contract import ServiceContract

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceContract from a JSON string
service_contract_instance = ServiceContract.from_json(json)
# print the JSON string representation of the object
print(ServiceContract.to_json())

# convert the object into a dict
service_contract_dict = service_contract_instance.to_dict()
# create an instance of ServiceContract from a dict
service_contract_from_dict = ServiceContract.from_dict(service_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


