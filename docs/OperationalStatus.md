# OperationalStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**last_check** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.operational_status import OperationalStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OperationalStatus from a JSON string
operational_status_instance = OperationalStatus.from_json(json)
# print the JSON string representation of the object
print(OperationalStatus.to_json())

# convert the object into a dict
operational_status_dict = operational_status_instance.to_dict()
# create an instance of OperationalStatus from a dict
operational_status_from_dict = OperationalStatus.from_dict(operational_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


