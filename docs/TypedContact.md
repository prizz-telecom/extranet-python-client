# TypedContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_workflows** | **List[str]** | liste des processus disponible pour l&#39;objet | [optional] 
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_class** | **str** |  | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.typed_contact import TypedContact

# TODO update the JSON string below
json = "{}"
# create an instance of TypedContact from a JSON string
typed_contact_instance = TypedContact.from_json(json)
# print the JSON string representation of the object
print(TypedContact.to_json())

# convert the object into a dict
typed_contact_dict = typed_contact_instance.to_dict()
# create an instance of TypedContact from a dict
typed_contact_from_dict = TypedContact.from_dict(typed_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


