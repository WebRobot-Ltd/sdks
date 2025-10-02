# DatasetUploadApiDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**attachment_name** | **str** |  | [optional] 
**headerline** | **str** |  | [optional] 

## Example

```python
from webrobot.models.dataset_upload_api_dto import DatasetUploadApiDto

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetUploadApiDto from a JSON string
dataset_upload_api_dto_instance = DatasetUploadApiDto.from_json(json)
# print the JSON string representation of the object
print(DatasetUploadApiDto.to_json())

# convert the object into a dict
dataset_upload_api_dto_dict = dataset_upload_api_dto_instance.to_dict()
# create an instance of DatasetUploadApiDto from a dict
dataset_upload_api_dto_from_dict = DatasetUploadApiDto.from_dict(dataset_upload_api_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


