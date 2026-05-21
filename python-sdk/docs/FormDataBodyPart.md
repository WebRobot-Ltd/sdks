# FormDataBodyPart


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
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**form_data_content_disposition** | [**FormDataContentDisposition**](FormDataContentDisposition.md) |  | [optional] 
**simple** | **bool** |  | [optional] 
**parameterized_headers** | **Dict[str, List[ParameterizedHeader]]** |  | [optional] 

## Example

```python
from webrobot.models.form_data_body_part import FormDataBodyPart

# TODO update the JSON string below
json = "{}"
# create an instance of FormDataBodyPart from a JSON string
form_data_body_part_instance = FormDataBodyPart.from_json(json)
# print the JSON string representation of the object
print(FormDataBodyPart.to_json())

# convert the object into a dict
form_data_body_part_dict = form_data_body_part_instance.to_dict()
# create an instance of FormDataBodyPart from a dict
form_data_body_part_from_dict = FormDataBodyPart.from_dict(form_data_body_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


