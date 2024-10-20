# CommentTree


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**Comment**](Comment.md) |  | [optional] 
**children** | [**List[CommentTree]**](CommentTree.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.comment_tree import CommentTree

# TODO update the JSON string below
json = "{}"
# create an instance of CommentTree from a JSON string
comment_tree_instance = CommentTree.from_json(json)
# print the JSON string representation of the object
print(CommentTree.to_json())

# convert the object into a dict
comment_tree_dict = comment_tree_instance.to_dict()
# create an instance of CommentTree from a dict
comment_tree_from_dict = CommentTree.from_dict(comment_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


