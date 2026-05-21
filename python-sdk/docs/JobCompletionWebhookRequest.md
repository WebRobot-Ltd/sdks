# JobCompletionWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**execution_id** | **str** |  | [optional] 
**spark_application_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**output_dataset_path** | **str** |  | [optional] 
**output_dataset_format** | **str** |  | [optional] 
**output_dataset_schema** | **str** |  | [optional] 
**duration_seconds** | **int** |  | [optional] 
**records_processed** | **int** |  | [optional] 
**records_output** | **int** |  | [optional] 
**output_file_size_bytes** | **int** |  | [optional] 
**partitions_count** | **int** |  | [optional] 
**driver_memory_used_bytes** | **int** |  | [optional] 
**executor_memory_used_bytes** | **int** |  | [optional] 
**executor_count** | **int** |  | [optional] 
**total_cpu_time_seconds** | **int** |  | [optional] 
**error_count** | **int** |  | [optional] 
**warning_count** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**additional_metrics** | **Dict[str, object]** |  | [optional] 
**started_at** | **str** |  | [optional] 
**completed_at** | **str** |  | [optional] 
**spark_ui_url** | **str** |  | [optional] 
**metrics** | **Dict[str, object]** |  | [optional] 

## Example

```python
from webrobot.models.job_completion_webhook_request import JobCompletionWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobCompletionWebhookRequest from a JSON string
job_completion_webhook_request_instance = JobCompletionWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(JobCompletionWebhookRequest.to_json())

# convert the object into a dict
job_completion_webhook_request_dict = job_completion_webhook_request_instance.to_dict()
# create an instance of JobCompletionWebhookRequest from a dict
job_completion_webhook_request_from_dict = JobCompletionWebhookRequest.from_dict(job_completion_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


