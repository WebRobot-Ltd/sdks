# AgentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**api_endpoint** | **str** |  | [optional] 
**execution_mode** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**backstory** | **str** |  | [optional] 
**default_prompt** | **str** |  | [optional] 
**prompts** | **str** |  | [optional] 
**config** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**code_type_id** | **str** |  | [optional] 
**pyspark_code** | **str** |  | [optional] 
**python_extensions** | **str** |  | [optional] 
**stack_type** | **str** |  | [optional] 
**generated_at** | **datetime** |  | [optional] 
**tool_ids** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from webrobot.models.agent_dto import AgentDto

# TODO update the JSON string below
json = "{}"
# create an instance of AgentDto from a JSON string
agent_dto_instance = AgentDto.from_json(json)
# print the JSON string representation of the object
print(AgentDto.to_json())

# convert the object into a dict
agent_dto_dict = agent_dto_instance.to_dict()
# create an instance of AgentDto from a dict
agent_dto_from_dict = AgentDto.from_dict(agent_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


