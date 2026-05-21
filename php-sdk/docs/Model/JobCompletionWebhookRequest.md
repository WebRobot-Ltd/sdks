# # JobCompletionWebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **string** |  | [optional]
**execution_id** | **string** |  | [optional]
**spark_application_name** | **string** |  | [optional]
**status** | **string** |  | [optional]
**output_dataset_path** | **string** |  | [optional]
**output_dataset_format** | **string** |  | [optional]
**output_dataset_schema** | **string** |  | [optional]
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
**error_message** | **string** |  | [optional]
**additional_metrics** | **array<string,object>** |  | [optional]
**started_at** | **string** |  | [optional]
**completed_at** | **string** |  | [optional]
**spark_ui_url** | **string** |  | [optional]
**metrics** | **array<string,object>** |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
