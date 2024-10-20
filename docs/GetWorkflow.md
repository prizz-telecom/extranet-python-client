# GetWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**redirect** | [**GetWorkflowRedirect**](GetWorkflowRedirect.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.get_workflow import GetWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkflow from a JSON string
get_workflow_instance = GetWorkflow.from_json(json)
# print the JSON string representation of the object
print(GetWorkflow.to_json())

# convert the object into a dict
get_workflow_dict = get_workflow_instance.to_dict()
# create an instance of GetWorkflow from a dict
get_workflow_from_dict = GetWorkflow.from_dict(get_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


