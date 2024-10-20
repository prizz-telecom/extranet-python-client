# CreateWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_name** | **str** |  | [optional] 
**entity_id** | **int** |  | [optional] 

## Example

```python
from prizz_extranet.models.create_workflow import CreateWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkflow from a JSON string
create_workflow_instance = CreateWorkflow.from_json(json)
# print the JSON string representation of the object
print(CreateWorkflow.to_json())

# convert the object into a dict
create_workflow_dict = create_workflow_instance.to_dict()
# create an instance of CreateWorkflow from a dict
create_workflow_from_dict = CreateWorkflow.from_dict(create_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


