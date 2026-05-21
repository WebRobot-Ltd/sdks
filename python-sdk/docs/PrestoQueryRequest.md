# PrestoQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sql** | **str** |  | [optional] 
**catalog** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from webrobot.models.presto_query_request import PrestoQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrestoQueryRequest from a JSON string
presto_query_request_instance = PrestoQueryRequest.from_json(json)
# print the JSON string representation of the object
print(PrestoQueryRequest.to_json())

# convert the object into a dict
presto_query_request_dict = presto_query_request_instance.to_dict()
# create an instance of PrestoQueryRequest from a dict
presto_query_request_from_dict = PrestoQueryRequest.from_dict(presto_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


