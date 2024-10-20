# GetPublicAttachments200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[Attachment]**](Attachment.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.get_public_attachments200_response import GetPublicAttachments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicAttachments200Response from a JSON string
get_public_attachments200_response_instance = GetPublicAttachments200Response.from_json(json)
# print the JSON string representation of the object
print(GetPublicAttachments200Response.to_json())

# convert the object into a dict
get_public_attachments200_response_dict = get_public_attachments200_response_instance.to_dict()
# create an instance of GetPublicAttachments200Response from a dict
get_public_attachments200_response_from_dict = GetPublicAttachments200Response.from_dict(get_public_attachments200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


