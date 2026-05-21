# ImportOptionsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_organization_id** | **str** |  | [optional] 
**overwrite_existing** | **bool** |  | [optional] 
**import_existing_projects** | **bool** |  | [optional] 
**import_existing_agents** | **bool** |  | [optional] 
**import_existing_jobs** | **bool** |  | [optional] 
**import_existing_tasks** | **bool** |  | [optional] 
**import_existing_datasets** | **bool** |  | [optional] 

## Example

```python
from webrobot.models.import_options_dto import ImportOptionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImportOptionsDto from a JSON string
import_options_dto_instance = ImportOptionsDto.from_json(json)
# print the JSON string representation of the object
print(ImportOptionsDto.to_json())

# convert the object into a dict
import_options_dto_dict = import_options_dto_instance.to_dict()
# create an instance of ImportOptionsDto from a dict
import_options_dto_from_dict = ImportOptionsDto.from_dict(import_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


