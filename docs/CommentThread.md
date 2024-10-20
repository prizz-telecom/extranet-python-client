# CommentThread


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**owner** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**entity_class** | **str** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**public** | **str** |  | [optional] 
**subscribers** | **List[str]** |  | [optional] 
**comments** | [**List[CommentTree]**](CommentTree.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.comment_thread import CommentThread

# TODO update the JSON string below
json = "{}"
# create an instance of CommentThread from a JSON string
comment_thread_instance = CommentThread.from_json(json)
# print the JSON string representation of the object
print(CommentThread.to_json())

# convert the object into a dict
comment_thread_dict = comment_thread_instance.to_dict()
# create an instance of CommentThread from a dict
comment_thread_from_dict = CommentThread.from_dict(comment_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


