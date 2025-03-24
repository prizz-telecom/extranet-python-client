# AppointmentTech


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
from prizz_extranet.models.appointment_tech import AppointmentTech

# TODO update the JSON string below
json = "{}"
# create an instance of AppointmentTech from a JSON string
appointment_tech_instance = AppointmentTech.from_json(json)
# print the JSON string representation of the object
print(AppointmentTech.to_json())

# convert the object into a dict
appointment_tech_dict = appointment_tech_instance.to_dict()
# create an instance of AppointmentTech from a dict
appointment_tech_from_dict = AppointmentTech.from_dict(appointment_tech_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


