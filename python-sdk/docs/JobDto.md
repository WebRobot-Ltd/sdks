# JobDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**agent_id** | **str** |  | [optional] 
**input_dataset_id** | **str** |  | [optional] 
**execution_status** | **str** |  | [optional] 
**scheduled_time** | **datetime** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**task_ids** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from webrobot.models.job_dto import JobDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobDto from a JSON string
job_dto_instance = JobDto.from_json(json)
# print the JSON string representation of the object
print(JobDto.to_json())

# convert the object into a dict
job_dto_dict = job_dto_instance.to_dict()
# create an instance of JobDto from a dict
job_dto_from_dict = JobDto.from_dict(job_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


