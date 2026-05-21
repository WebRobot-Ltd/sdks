# EtlLibraryVersionApiDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**build_type** | **str** |  | [optional] 
**build_number** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**jar_path** | **str** |  | [optional] 
**jar_path_obfuscated** | **str** |  | [optional] 
**jar_size_bytes** | **int** |  | [optional] 
**uploaded_at** | **datetime** |  | [optional] 
**active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**image_tag** | **str** |  | [optional] 

## Example

```python
from webrobot.models.etl_library_version_api_dto import EtlLibraryVersionApiDto

# TODO update the JSON string below
json = "{}"
# create an instance of EtlLibraryVersionApiDto from a JSON string
etl_library_version_api_dto_instance = EtlLibraryVersionApiDto.from_json(json)
# print the JSON string representation of the object
print(EtlLibraryVersionApiDto.to_json())

# convert the object into a dict
etl_library_version_api_dto_dict = etl_library_version_api_dto_instance.to_dict()
# create an instance of EtlLibraryVersionApiDto from a dict
etl_library_version_api_dto_from_dict = EtlLibraryVersionApiDto.from_dict(etl_library_version_api_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


