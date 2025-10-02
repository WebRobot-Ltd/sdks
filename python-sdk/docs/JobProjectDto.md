# JobProjectDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**cron_schedule** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**job_ids** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from webrobot.models.job_project_dto import JobProjectDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobProjectDto from a JSON string
job_project_dto_instance = JobProjectDto.from_json(json)
# print the JSON string representation of the object
print(JobProjectDto.to_json())

# convert the object into a dict
job_project_dto_dict = job_project_dto_instance.to_dict()
# create an instance of JobProjectDto from a dict
job_project_dto_from_dict = JobProjectDto.from_dict(job_project_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


