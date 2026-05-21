# BodyPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_disposition** | [**ContentDisposition**](ContentDisposition.md) |  | [optional] 
**entity** | **object** |  | [optional] 
**headers** | **Dict[str, List[str]]** |  | [optional] 
**media_type** | [**BodyPartMediaType**](BodyPartMediaType.md) |  | [optional] 
**message_body_workers** | **object** |  | [optional] 
**parent** | [**MultiPart**](MultiPart.md) |  | [optional] 
**providers** | **object** |  | [optional] 
**parameterized_headers** | **Dict[str, List[ParameterizedHeader]]** |  | [optional] 

## Example

```python
from webrobot.models.body_part import BodyPart

# TODO update the JSON string below
json = "{}"
# create an instance of BodyPart from a JSON string
body_part_instance = BodyPart.from_json(json)
# print the JSON string representation of the object
print(BodyPart.to_json())

# convert the object into a dict
body_part_dict = body_part_instance.to_dict()
# create an instance of BodyPart from a dict
body_part_from_dict = BodyPart.from_dict(body_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


