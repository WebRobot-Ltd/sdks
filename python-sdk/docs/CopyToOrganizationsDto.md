# CopyToOrganizationsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** |  | [optional] 

## Example

```python
from webrobot.models.copy_to_organizations_dto import CopyToOrganizationsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CopyToOrganizationsDto from a JSON string
copy_to_organizations_dto_instance = CopyToOrganizationsDto.from_json(json)
# print the JSON string representation of the object
print(CopyToOrganizationsDto.to_json())

# convert the object into a dict
copy_to_organizations_dto_dict = copy_to_organizations_dto_instance.to_dict()
# create an instance of CopyToOrganizationsDto from a dict
copy_to_organizations_dto_from_dict = CopyToOrganizationsDto.from_dict(copy_to_organizations_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


