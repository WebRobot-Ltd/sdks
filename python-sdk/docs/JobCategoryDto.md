# JobCategoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**agent_ids** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from webrobot.models.job_category_dto import JobCategoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobCategoryDto from a JSON string
job_category_dto_instance = JobCategoryDto.from_json(json)
# print the JSON string representation of the object
print(JobCategoryDto.to_json())

# convert the object into a dict
job_category_dto_dict = job_category_dto_instance.to_dict()
# create an instance of JobCategoryDto from a dict
job_category_dto_from_dict = JobCategoryDto.from_dict(job_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


