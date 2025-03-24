# AppointmentContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_workflows** | **List[str]** | liste des processus disponible pour l&#39;objet | [optional] 
**id** | **int** |  | [optional] 
**firstname** | **str** |  | [optional] 
**lastname** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone1** | **str** |  | [optional] 
**phone2** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 

## Example

```python
from prizz_extranet.models.appointment_contact import AppointmentContact

# TODO update the JSON string below
json = "{}"
# create an instance of AppointmentContact from a JSON string
appointment_contact_instance = AppointmentContact.from_json(json)
# print the JSON string representation of the object
print(AppointmentContact.to_json())

# convert the object into a dict
appointment_contact_dict = appointment_contact_instance.to_dict()
# create an instance of AppointmentContact from a dict
appointment_contact_from_dict = AppointmentContact.from_dict(appointment_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


