# GetRunningWorkflows200ResponseWorkflowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**context** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_run_date** | **datetime** |  | [optional] 
**entity_class** | **str** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_description** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 
**last_log** | **str** |  | [optional] 
**html** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.get_running_workflows200_response_workflows_inner import GetRunningWorkflows200ResponseWorkflowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRunningWorkflows200ResponseWorkflowsInner from a JSON string
get_running_workflows200_response_workflows_inner_instance = GetRunningWorkflows200ResponseWorkflowsInner.from_json(json)
# print the JSON string representation of the object
print(GetRunningWorkflows200ResponseWorkflowsInner.to_json())

# convert the object into a dict
get_running_workflows200_response_workflows_inner_dict = get_running_workflows200_response_workflows_inner_instance.to_dict()
# create an instance of GetRunningWorkflows200ResponseWorkflowsInner from a dict
get_running_workflows200_response_workflows_inner_from_dict = GetRunningWorkflows200ResponseWorkflowsInner.from_dict(get_running_workflows200_response_workflows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


