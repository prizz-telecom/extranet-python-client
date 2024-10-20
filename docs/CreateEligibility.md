# CreateEligibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[ClientLegalEntity]**](ClientLegalEntity.md) | list your clientlegalentities used for eligibility, give an indication of pricelists and contracts used | [optional] 
**responses** | **List[int]** | workflow ids where you can get responses | [optional] 

## Example

```python
from prizz_extranet.models.create_eligibility import CreateEligibility

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEligibility from a JSON string
create_eligibility_instance = CreateEligibility.from_json(json)
# print the JSON string representation of the object
print(CreateEligibility.to_json())

# convert the object into a dict
create_eligibility_dict = create_eligibility_instance.to_dict()
# create an instance of CreateEligibility from a dict
create_eligibility_from_dict = CreateEligibility.from_dict(create_eligibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


