# ExportOptionsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_projects** | **bool** |  | [optional] 
**include_agents** | **bool** |  | [optional] 
**include_jobs** | **bool** |  | [optional] 
**include_tasks** | **bool** |  | [optional] 
**include_datasets** | **bool** |  | [optional] 

## Example

```python
from webrobot.models.export_options_dto import ExportOptionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExportOptionsDto from a JSON string
export_options_dto_instance = ExportOptionsDto.from_json(json)
# print the JSON string representation of the object
print(ExportOptionsDto.to_json())

# convert the object into a dict
export_options_dto_dict = export_options_dto_instance.to_dict()
# create an instance of ExportOptionsDto from a dict
export_options_dto_from_dict = ExportOptionsDto.from_dict(export_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


