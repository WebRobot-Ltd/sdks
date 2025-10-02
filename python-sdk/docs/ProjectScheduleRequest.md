# ProjectScheduleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_schedule** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from webrobot.models.project_schedule_request import ProjectScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectScheduleRequest from a JSON string
project_schedule_request_instance = ProjectScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectScheduleRequest.to_json())

# convert the object into a dict
project_schedule_request_dict = project_schedule_request_instance.to_dict()
# create an instance of ProjectScheduleRequest from a dict
project_schedule_request_from_dict = ProjectScheduleRequest.from_dict(project_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


