# JobCompletionWebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**JobId** | Pointer to **string** |  | [optional] 
**ExecutionId** | Pointer to **string** |  | [optional] 
**SparkApplicationName** | Pointer to **string** |  | [optional] 
**Status** | Pointer to **string** |  | [optional] 
**OutputDatasetPath** | Pointer to **string** |  | [optional] 
**OutputDatasetFormat** | Pointer to **string** |  | [optional] 
**OutputDatasetSchema** | Pointer to **string** |  | [optional] 
**DurationSeconds** | Pointer to **int64** |  | [optional] 
**RecordsProcessed** | Pointer to **int64** |  | [optional] 
**RecordsOutput** | Pointer to **int64** |  | [optional] 
**OutputFileSizeBytes** | Pointer to **int64** |  | [optional] 
**PartitionsCount** | Pointer to **int32** |  | [optional] 
**DriverMemoryUsedBytes** | Pointer to **int64** |  | [optional] 
**ExecutorMemoryUsedBytes** | Pointer to **int64** |  | [optional] 
**ExecutorCount** | Pointer to **int32** |  | [optional] 
**TotalCpuTimeSeconds** | Pointer to **int64** |  | [optional] 
**ErrorCount** | Pointer to **int32** |  | [optional] 
**WarningCount** | Pointer to **int32** |  | [optional] 
**ErrorMessage** | Pointer to **string** |  | [optional] 
**AdditionalMetrics** | Pointer to **map[string]map[string]interface{}** |  | [optional] 
**StartedAt** | Pointer to **string** |  | [optional] 
**CompletedAt** | Pointer to **string** |  | [optional] 
**SparkUiUrl** | Pointer to **string** |  | [optional] 
**Metrics** | Pointer to **map[string]map[string]interface{}** |  | [optional] 

## Methods

### NewJobCompletionWebhookRequest

`func NewJobCompletionWebhookRequest() *JobCompletionWebhookRequest`

NewJobCompletionWebhookRequest instantiates a new JobCompletionWebhookRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewJobCompletionWebhookRequestWithDefaults

`func NewJobCompletionWebhookRequestWithDefaults() *JobCompletionWebhookRequest`

NewJobCompletionWebhookRequestWithDefaults instantiates a new JobCompletionWebhookRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetJobId

`func (o *JobCompletionWebhookRequest) GetJobId() string`

GetJobId returns the JobId field if non-nil, zero value otherwise.

### GetJobIdOk

`func (o *JobCompletionWebhookRequest) GetJobIdOk() (*string, bool)`

GetJobIdOk returns a tuple with the JobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobId

`func (o *JobCompletionWebhookRequest) SetJobId(v string)`

SetJobId sets JobId field to given value.

### HasJobId

`func (o *JobCompletionWebhookRequest) HasJobId() bool`

HasJobId returns a boolean if a field has been set.

### GetExecutionId

`func (o *JobCompletionWebhookRequest) GetExecutionId() string`

GetExecutionId returns the ExecutionId field if non-nil, zero value otherwise.

### GetExecutionIdOk

`func (o *JobCompletionWebhookRequest) GetExecutionIdOk() (*string, bool)`

GetExecutionIdOk returns a tuple with the ExecutionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecutionId

`func (o *JobCompletionWebhookRequest) SetExecutionId(v string)`

SetExecutionId sets ExecutionId field to given value.

### HasExecutionId

`func (o *JobCompletionWebhookRequest) HasExecutionId() bool`

HasExecutionId returns a boolean if a field has been set.

### GetSparkApplicationName

`func (o *JobCompletionWebhookRequest) GetSparkApplicationName() string`

GetSparkApplicationName returns the SparkApplicationName field if non-nil, zero value otherwise.

### GetSparkApplicationNameOk

`func (o *JobCompletionWebhookRequest) GetSparkApplicationNameOk() (*string, bool)`

GetSparkApplicationNameOk returns a tuple with the SparkApplicationName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSparkApplicationName

`func (o *JobCompletionWebhookRequest) SetSparkApplicationName(v string)`

SetSparkApplicationName sets SparkApplicationName field to given value.

### HasSparkApplicationName

`func (o *JobCompletionWebhookRequest) HasSparkApplicationName() bool`

HasSparkApplicationName returns a boolean if a field has been set.

### GetStatus

`func (o *JobCompletionWebhookRequest) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *JobCompletionWebhookRequest) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *JobCompletionWebhookRequest) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *JobCompletionWebhookRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetOutputDatasetPath

`func (o *JobCompletionWebhookRequest) GetOutputDatasetPath() string`

GetOutputDatasetPath returns the OutputDatasetPath field if non-nil, zero value otherwise.

### GetOutputDatasetPathOk

`func (o *JobCompletionWebhookRequest) GetOutputDatasetPathOk() (*string, bool)`

GetOutputDatasetPathOk returns a tuple with the OutputDatasetPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutputDatasetPath

`func (o *JobCompletionWebhookRequest) SetOutputDatasetPath(v string)`

SetOutputDatasetPath sets OutputDatasetPath field to given value.

### HasOutputDatasetPath

`func (o *JobCompletionWebhookRequest) HasOutputDatasetPath() bool`

HasOutputDatasetPath returns a boolean if a field has been set.

### GetOutputDatasetFormat

`func (o *JobCompletionWebhookRequest) GetOutputDatasetFormat() string`

GetOutputDatasetFormat returns the OutputDatasetFormat field if non-nil, zero value otherwise.

### GetOutputDatasetFormatOk

`func (o *JobCompletionWebhookRequest) GetOutputDatasetFormatOk() (*string, bool)`

GetOutputDatasetFormatOk returns a tuple with the OutputDatasetFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutputDatasetFormat

`func (o *JobCompletionWebhookRequest) SetOutputDatasetFormat(v string)`

SetOutputDatasetFormat sets OutputDatasetFormat field to given value.

### HasOutputDatasetFormat

`func (o *JobCompletionWebhookRequest) HasOutputDatasetFormat() bool`

HasOutputDatasetFormat returns a boolean if a field has been set.

### GetOutputDatasetSchema

`func (o *JobCompletionWebhookRequest) GetOutputDatasetSchema() string`

GetOutputDatasetSchema returns the OutputDatasetSchema field if non-nil, zero value otherwise.

### GetOutputDatasetSchemaOk

`func (o *JobCompletionWebhookRequest) GetOutputDatasetSchemaOk() (*string, bool)`

GetOutputDatasetSchemaOk returns a tuple with the OutputDatasetSchema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutputDatasetSchema

`func (o *JobCompletionWebhookRequest) SetOutputDatasetSchema(v string)`

SetOutputDatasetSchema sets OutputDatasetSchema field to given value.

### HasOutputDatasetSchema

`func (o *JobCompletionWebhookRequest) HasOutputDatasetSchema() bool`

HasOutputDatasetSchema returns a boolean if a field has been set.

### GetDurationSeconds

`func (o *JobCompletionWebhookRequest) GetDurationSeconds() int64`

GetDurationSeconds returns the DurationSeconds field if non-nil, zero value otherwise.

### GetDurationSecondsOk

`func (o *JobCompletionWebhookRequest) GetDurationSecondsOk() (*int64, bool)`

GetDurationSecondsOk returns a tuple with the DurationSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDurationSeconds

`func (o *JobCompletionWebhookRequest) SetDurationSeconds(v int64)`

SetDurationSeconds sets DurationSeconds field to given value.

### HasDurationSeconds

`func (o *JobCompletionWebhookRequest) HasDurationSeconds() bool`

HasDurationSeconds returns a boolean if a field has been set.

### GetRecordsProcessed

`func (o *JobCompletionWebhookRequest) GetRecordsProcessed() int64`

GetRecordsProcessed returns the RecordsProcessed field if non-nil, zero value otherwise.

### GetRecordsProcessedOk

`func (o *JobCompletionWebhookRequest) GetRecordsProcessedOk() (*int64, bool)`

GetRecordsProcessedOk returns a tuple with the RecordsProcessed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecordsProcessed

`func (o *JobCompletionWebhookRequest) SetRecordsProcessed(v int64)`

SetRecordsProcessed sets RecordsProcessed field to given value.

### HasRecordsProcessed

`func (o *JobCompletionWebhookRequest) HasRecordsProcessed() bool`

HasRecordsProcessed returns a boolean if a field has been set.

### GetRecordsOutput

`func (o *JobCompletionWebhookRequest) GetRecordsOutput() int64`

GetRecordsOutput returns the RecordsOutput field if non-nil, zero value otherwise.

### GetRecordsOutputOk

`func (o *JobCompletionWebhookRequest) GetRecordsOutputOk() (*int64, bool)`

GetRecordsOutputOk returns a tuple with the RecordsOutput field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecordsOutput

`func (o *JobCompletionWebhookRequest) SetRecordsOutput(v int64)`

SetRecordsOutput sets RecordsOutput field to given value.

### HasRecordsOutput

`func (o *JobCompletionWebhookRequest) HasRecordsOutput() bool`

HasRecordsOutput returns a boolean if a field has been set.

### GetOutputFileSizeBytes

`func (o *JobCompletionWebhookRequest) GetOutputFileSizeBytes() int64`

GetOutputFileSizeBytes returns the OutputFileSizeBytes field if non-nil, zero value otherwise.

### GetOutputFileSizeBytesOk

`func (o *JobCompletionWebhookRequest) GetOutputFileSizeBytesOk() (*int64, bool)`

GetOutputFileSizeBytesOk returns a tuple with the OutputFileSizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutputFileSizeBytes

`func (o *JobCompletionWebhookRequest) SetOutputFileSizeBytes(v int64)`

SetOutputFileSizeBytes sets OutputFileSizeBytes field to given value.

### HasOutputFileSizeBytes

`func (o *JobCompletionWebhookRequest) HasOutputFileSizeBytes() bool`

HasOutputFileSizeBytes returns a boolean if a field has been set.

### GetPartitionsCount

`func (o *JobCompletionWebhookRequest) GetPartitionsCount() int32`

GetPartitionsCount returns the PartitionsCount field if non-nil, zero value otherwise.

### GetPartitionsCountOk

`func (o *JobCompletionWebhookRequest) GetPartitionsCountOk() (*int32, bool)`

GetPartitionsCountOk returns a tuple with the PartitionsCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPartitionsCount

`func (o *JobCompletionWebhookRequest) SetPartitionsCount(v int32)`

SetPartitionsCount sets PartitionsCount field to given value.

### HasPartitionsCount

`func (o *JobCompletionWebhookRequest) HasPartitionsCount() bool`

HasPartitionsCount returns a boolean if a field has been set.

### GetDriverMemoryUsedBytes

`func (o *JobCompletionWebhookRequest) GetDriverMemoryUsedBytes() int64`

GetDriverMemoryUsedBytes returns the DriverMemoryUsedBytes field if non-nil, zero value otherwise.

### GetDriverMemoryUsedBytesOk

`func (o *JobCompletionWebhookRequest) GetDriverMemoryUsedBytesOk() (*int64, bool)`

GetDriverMemoryUsedBytesOk returns a tuple with the DriverMemoryUsedBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriverMemoryUsedBytes

`func (o *JobCompletionWebhookRequest) SetDriverMemoryUsedBytes(v int64)`

SetDriverMemoryUsedBytes sets DriverMemoryUsedBytes field to given value.

### HasDriverMemoryUsedBytes

`func (o *JobCompletionWebhookRequest) HasDriverMemoryUsedBytes() bool`

HasDriverMemoryUsedBytes returns a boolean if a field has been set.

### GetExecutorMemoryUsedBytes

`func (o *JobCompletionWebhookRequest) GetExecutorMemoryUsedBytes() int64`

GetExecutorMemoryUsedBytes returns the ExecutorMemoryUsedBytes field if non-nil, zero value otherwise.

### GetExecutorMemoryUsedBytesOk

`func (o *JobCompletionWebhookRequest) GetExecutorMemoryUsedBytesOk() (*int64, bool)`

GetExecutorMemoryUsedBytesOk returns a tuple with the ExecutorMemoryUsedBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecutorMemoryUsedBytes

`func (o *JobCompletionWebhookRequest) SetExecutorMemoryUsedBytes(v int64)`

SetExecutorMemoryUsedBytes sets ExecutorMemoryUsedBytes field to given value.

### HasExecutorMemoryUsedBytes

`func (o *JobCompletionWebhookRequest) HasExecutorMemoryUsedBytes() bool`

HasExecutorMemoryUsedBytes returns a boolean if a field has been set.

### GetExecutorCount

`func (o *JobCompletionWebhookRequest) GetExecutorCount() int32`

GetExecutorCount returns the ExecutorCount field if non-nil, zero value otherwise.

### GetExecutorCountOk

`func (o *JobCompletionWebhookRequest) GetExecutorCountOk() (*int32, bool)`

GetExecutorCountOk returns a tuple with the ExecutorCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecutorCount

`func (o *JobCompletionWebhookRequest) SetExecutorCount(v int32)`

SetExecutorCount sets ExecutorCount field to given value.

### HasExecutorCount

`func (o *JobCompletionWebhookRequest) HasExecutorCount() bool`

HasExecutorCount returns a boolean if a field has been set.

### GetTotalCpuTimeSeconds

`func (o *JobCompletionWebhookRequest) GetTotalCpuTimeSeconds() int64`

GetTotalCpuTimeSeconds returns the TotalCpuTimeSeconds field if non-nil, zero value otherwise.

### GetTotalCpuTimeSecondsOk

`func (o *JobCompletionWebhookRequest) GetTotalCpuTimeSecondsOk() (*int64, bool)`

GetTotalCpuTimeSecondsOk returns a tuple with the TotalCpuTimeSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalCpuTimeSeconds

`func (o *JobCompletionWebhookRequest) SetTotalCpuTimeSeconds(v int64)`

SetTotalCpuTimeSeconds sets TotalCpuTimeSeconds field to given value.

### HasTotalCpuTimeSeconds

`func (o *JobCompletionWebhookRequest) HasTotalCpuTimeSeconds() bool`

HasTotalCpuTimeSeconds returns a boolean if a field has been set.

### GetErrorCount

`func (o *JobCompletionWebhookRequest) GetErrorCount() int32`

GetErrorCount returns the ErrorCount field if non-nil, zero value otherwise.

### GetErrorCountOk

`func (o *JobCompletionWebhookRequest) GetErrorCountOk() (*int32, bool)`

GetErrorCountOk returns a tuple with the ErrorCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorCount

`func (o *JobCompletionWebhookRequest) SetErrorCount(v int32)`

SetErrorCount sets ErrorCount field to given value.

### HasErrorCount

`func (o *JobCompletionWebhookRequest) HasErrorCount() bool`

HasErrorCount returns a boolean if a field has been set.

### GetWarningCount

`func (o *JobCompletionWebhookRequest) GetWarningCount() int32`

GetWarningCount returns the WarningCount field if non-nil, zero value otherwise.

### GetWarningCountOk

`func (o *JobCompletionWebhookRequest) GetWarningCountOk() (*int32, bool)`

GetWarningCountOk returns a tuple with the WarningCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWarningCount

`func (o *JobCompletionWebhookRequest) SetWarningCount(v int32)`

SetWarningCount sets WarningCount field to given value.

### HasWarningCount

`func (o *JobCompletionWebhookRequest) HasWarningCount() bool`

HasWarningCount returns a boolean if a field has been set.

### GetErrorMessage

`func (o *JobCompletionWebhookRequest) GetErrorMessage() string`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *JobCompletionWebhookRequest) GetErrorMessageOk() (*string, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *JobCompletionWebhookRequest) SetErrorMessage(v string)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *JobCompletionWebhookRequest) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.

### GetAdditionalMetrics

`func (o *JobCompletionWebhookRequest) GetAdditionalMetrics() map[string]map[string]interface{}`

GetAdditionalMetrics returns the AdditionalMetrics field if non-nil, zero value otherwise.

### GetAdditionalMetricsOk

`func (o *JobCompletionWebhookRequest) GetAdditionalMetricsOk() (*map[string]map[string]interface{}, bool)`

GetAdditionalMetricsOk returns a tuple with the AdditionalMetrics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalMetrics

`func (o *JobCompletionWebhookRequest) SetAdditionalMetrics(v map[string]map[string]interface{})`

SetAdditionalMetrics sets AdditionalMetrics field to given value.

### HasAdditionalMetrics

`func (o *JobCompletionWebhookRequest) HasAdditionalMetrics() bool`

HasAdditionalMetrics returns a boolean if a field has been set.

### GetStartedAt

`func (o *JobCompletionWebhookRequest) GetStartedAt() string`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *JobCompletionWebhookRequest) GetStartedAtOk() (*string, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *JobCompletionWebhookRequest) SetStartedAt(v string)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *JobCompletionWebhookRequest) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### GetCompletedAt

`func (o *JobCompletionWebhookRequest) GetCompletedAt() string`

GetCompletedAt returns the CompletedAt field if non-nil, zero value otherwise.

### GetCompletedAtOk

`func (o *JobCompletionWebhookRequest) GetCompletedAtOk() (*string, bool)`

GetCompletedAtOk returns a tuple with the CompletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompletedAt

`func (o *JobCompletionWebhookRequest) SetCompletedAt(v string)`

SetCompletedAt sets CompletedAt field to given value.

### HasCompletedAt

`func (o *JobCompletionWebhookRequest) HasCompletedAt() bool`

HasCompletedAt returns a boolean if a field has been set.

### GetSparkUiUrl

`func (o *JobCompletionWebhookRequest) GetSparkUiUrl() string`

GetSparkUiUrl returns the SparkUiUrl field if non-nil, zero value otherwise.

### GetSparkUiUrlOk

`func (o *JobCompletionWebhookRequest) GetSparkUiUrlOk() (*string, bool)`

GetSparkUiUrlOk returns a tuple with the SparkUiUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSparkUiUrl

`func (o *JobCompletionWebhookRequest) SetSparkUiUrl(v string)`

SetSparkUiUrl sets SparkUiUrl field to given value.

### HasSparkUiUrl

`func (o *JobCompletionWebhookRequest) HasSparkUiUrl() bool`

HasSparkUiUrl returns a boolean if a field has been set.

### GetMetrics

`func (o *JobCompletionWebhookRequest) GetMetrics() map[string]map[string]interface{}`

GetMetrics returns the Metrics field if non-nil, zero value otherwise.

### GetMetricsOk

`func (o *JobCompletionWebhookRequest) GetMetricsOk() (*map[string]map[string]interface{}, bool)`

GetMetricsOk returns a tuple with the Metrics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetrics

`func (o *JobCompletionWebhookRequest) SetMetrics(v map[string]map[string]interface{})`

SetMetrics sets Metrics field to given value.

### HasMetrics

`func (o *JobCompletionWebhookRequest) HasMetrics() bool`

HasMetrics returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


