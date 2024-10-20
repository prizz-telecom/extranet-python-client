# SetServiceContractVlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vid** | **int** | vlan id in group | [optional] 

## Example

```python
from prizz_extranet.models.set_service_contract_vlan_request import SetServiceContractVlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetServiceContractVlanRequest from a JSON string
set_service_contract_vlan_request_instance = SetServiceContractVlanRequest.from_json(json)
# print the JSON string representation of the object
print(SetServiceContractVlanRequest.to_json())

# convert the object into a dict
set_service_contract_vlan_request_dict = set_service_contract_vlan_request_instance.to_dict()
# create an instance of SetServiceContractVlanRequest from a dict
set_service_contract_vlan_request_from_dict = SetServiceContractVlanRequest.from_dict(set_service_contract_vlan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


