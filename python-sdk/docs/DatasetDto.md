# DatasetDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**source_type** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**file_format** | **str** |  | [optional] 
**file_size** | **int** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**field_ids** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**storage_path** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**dataset_type** | **str** |  | [optional] 
**trino_schema** | **str** |  | [optional] 
**storage_type** | **str** |  | [optional] 
**cloud_credential_id** | **int** |  | [optional] 

## Example

```python
from webrobot.models.dataset_dto import DatasetDto

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetDto from a JSON string
dataset_dto_instance = DatasetDto.from_json(json)
# print the JSON string representation of the object
print(DatasetDto.to_json())

# convert the object into a dict
dataset_dto_dict = dataset_dto_instance.to_dict()
# create an instance of DatasetDto from a dict
dataset_dto_from_dict = DatasetDto.from_dict(dataset_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


