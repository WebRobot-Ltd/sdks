# ModelPublishRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_model_path** | **str** |  | [optional] 
**model_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from webrobot.models.model_publish_request import ModelPublishRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPublishRequest from a JSON string
model_publish_request_instance = ModelPublishRequest.from_json(json)
# print the JSON string representation of the object
print(ModelPublishRequest.to_json())

# convert the object into a dict
model_publish_request_dict = model_publish_request_instance.to_dict()
# create an instance of ModelPublishRequest from a dict
model_publish_request_from_dict = ModelPublishRequest.from_dict(model_publish_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


