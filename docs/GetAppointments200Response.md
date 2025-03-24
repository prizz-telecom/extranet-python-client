# GetAppointments200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Appointment]**](Appointment.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.get_appointments200_response import GetAppointments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppointments200Response from a JSON string
get_appointments200_response_instance = GetAppointments200Response.from_json(json)
# print the JSON string representation of the object
print(GetAppointments200Response.to_json())

# convert the object into a dict
get_appointments200_response_dict = get_appointments200_response_instance.to_dict()
# create an instance of GetAppointments200Response from a dict
get_appointments200_response_from_dict = GetAppointments200Response.from_dict(get_appointments200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


