# BodyPartMediaType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 
**parameters** | **Dict[str, str]** |  | [optional] 
**wildcard_type** | **bool** |  | [optional] 
**wildcard_subtype** | **bool** |  | [optional] 

## Example

```python
from webrobot.models.body_part_media_type import BodyPartMediaType

# TODO update the JSON string below
json = "{}"
# create an instance of BodyPartMediaType from a JSON string
body_part_media_type_instance = BodyPartMediaType.from_json(json)
# print the JSON string representation of the object
print(BodyPartMediaType.to_json())

# convert the object into a dict
body_part_media_type_dict = body_part_media_type_instance.to_dict()
# create an instance of BodyPartMediaType from a dict
body_part_media_type_from_dict = BodyPartMediaType.from_dict(body_part_media_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


