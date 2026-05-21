# CronJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**schedule** | **str** |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**job_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**cluster_provider** | **str** |  | [optional] 
**cluster_config_id** | **str** |  | [optional] 
**secret_name** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**image** | **str** |  | [optional] 

## Example

```python
from webrobot.models.cron_job_request import CronJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CronJobRequest from a JSON string
cron_job_request_instance = CronJobRequest.from_json(json)
# print the JSON string representation of the object
print(CronJobRequest.to_json())

# convert the object into a dict
cron_job_request_dict = cron_job_request_instance.to_dict()
# create an instance of CronJobRequest from a dict
cron_job_request_from_dict = CronJobRequest.from_dict(cron_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


