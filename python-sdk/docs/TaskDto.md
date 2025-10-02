# TaskDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**job_id** | **str** |  | [optional] 
**bot_id** | **str** |  | [optional] 
**output_dataset_id** | **str** |  | [optional] 
**task_type** | **str** |  | [optional] 
**execution_reference_id** | **str** |  | [optional] 
**execution_status** | **str** |  | [optional] 
**execution_log** | **str** |  | [optional] 
**scheduled_time** | **datetime** |  | [optional] 
**execution_mode** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**api_key** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from webrobot.models.task_dto import TaskDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDto from a JSON string
task_dto_instance = TaskDto.from_json(json)
# print the JSON string representation of the object
print(TaskDto.to_json())

# convert the object into a dict
task_dto_dict = task_dto_instance.to_dict()
# create an instance of TaskDto from a dict
task_dto_from_dict = TaskDto.from_dict(task_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


