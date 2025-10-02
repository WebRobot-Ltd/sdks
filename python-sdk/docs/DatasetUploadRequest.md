# DatasetUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_path** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from webrobot.models.dataset_upload_request import DatasetUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetUploadRequest from a JSON string
dataset_upload_request_instance = DatasetUploadRequest.from_json(json)
# print the JSON string representation of the object
print(DatasetUploadRequest.to_json())

# convert the object into a dict
dataset_upload_request_dict = dataset_upload_request_instance.to_dict()
# create an instance of DatasetUploadRequest from a dict
dataset_upload_request_from_dict = DatasetUploadRequest.from_dict(dataset_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


