# MultiPart


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
**body_parts** | [**List[BodyPart]**](BodyPart.md) |  | [optional] 
**parameterized_headers** | **Dict[str, List[ParameterizedHeader]]** |  | [optional] 

## Example

```python
from webrobot.models.multi_part import MultiPart

# TODO update the JSON string below
json = "{}"
# create an instance of MultiPart from a JSON string
multi_part_instance = MultiPart.from_json(json)
# print the JSON string representation of the object
print(MultiPart.to_json())

# convert the object into a dict
multi_part_dict = multi_part_instance.to_dict()
# create an instance of MultiPart from a dict
multi_part_from_dict = MultiPart.from_dict(multi_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


