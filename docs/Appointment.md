# Appointment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_workflows** | **List[str]** | liste des processus disponible pour l&#39;objet | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**house_number** | **int** |  | [optional] 
**house_number_complement** | **str** |  | [optional] 
**street_name** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**city_name** | **str** |  | [optional] 
**insee_code** | **str** |  | [optional] 
**service_contract** | [**AppointmentServiceContract**](AppointmentServiceContract.md) |  | [optional] 
**contact** | [**AppointmentContact**](AppointmentContact.md) |  | [optional] 
**tech** | [**AppointmentTech**](AppointmentTech.md) |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**accepted** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**confirmation_process_id** | **int** |  | [optional] 

## Example

```python
from prizz_extranet.models.appointment import Appointment

# TODO update the JSON string below
json = "{}"
# create an instance of Appointment from a JSON string
appointment_instance = Appointment.from_json(json)
# print the JSON string representation of the object
print(Appointment.to_json())

# convert the object into a dict
appointment_dict = appointment_instance.to_dict()
# create an instance of Appointment from a dict
appointment_from_dict = Appointment.from_dict(appointment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


