# TaskDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**JobId** | Pointer to **string** |  | [optional] 
**BotId** | Pointer to **string** |  | [optional] 
**OutputDatasetId** | Pointer to **string** |  | [optional] 
**TaskType** | Pointer to **string** |  | [optional] 
**ExecutionReferenceId** | Pointer to **string** |  | [optional] 
**ExecutionStatus** | Pointer to **string** |  | [optional] 
**ExecutionLog** | Pointer to **string** |  | [optional] 
**ScheduledTime** | Pointer to **time.Time** |  | [optional] 
**ExecutionMode** | Pointer to **string** |  | [optional] 
**Enabled** | Pointer to **bool** |  | [optional] 
**ApiKey** | Pointer to **string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewTaskDto

`func NewTaskDto() *TaskDto`

NewTaskDto instantiates a new TaskDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTaskDtoWithDefaults

`func NewTaskDtoWithDefaults() *TaskDto`

NewTaskDtoWithDefaults instantiates a new TaskDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *TaskDto) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TaskDto) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TaskDto) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *TaskDto) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *TaskDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *TaskDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *TaskDto) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *TaskDto) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *TaskDto) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *TaskDto) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *TaskDto) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *TaskDto) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetJobId

`func (o *TaskDto) GetJobId() string`

GetJobId returns the JobId field if non-nil, zero value otherwise.

### GetJobIdOk

`func (o *TaskDto) GetJobIdOk() (*string, bool)`

GetJobIdOk returns a tuple with the JobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobId

`func (o *TaskDto) SetJobId(v string)`

SetJobId sets JobId field to given value.

### HasJobId

`func (o *TaskDto) HasJobId() bool`

HasJobId returns a boolean if a field has been set.

### GetBotId

`func (o *TaskDto) GetBotId() string`

GetBotId returns the BotId field if non-nil, zero value otherwise.

### GetBotIdOk

`func (o *TaskDto) GetBotIdOk() (*string, bool)`

GetBotIdOk returns a tuple with the BotId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBotId

`func (o *TaskDto) SetBotId(v string)`

SetBotId sets BotId field to given value.

### HasBotId

`func (o *TaskDto) HasBotId() bool`

HasBotId returns a boolean if a field has been set.

### GetOutputDatasetId

`func (o *TaskDto) GetOutputDatasetId() string`

GetOutputDatasetId returns the OutputDatasetId field if non-nil, zero value otherwise.

### GetOutputDatasetIdOk

`func (o *TaskDto) GetOutputDatasetIdOk() (*string, bool)`

GetOutputDatasetIdOk returns a tuple with the OutputDatasetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutputDatasetId

`func (o *TaskDto) SetOutputDatasetId(v string)`

SetOutputDatasetId sets OutputDatasetId field to given value.

### HasOutputDatasetId

`func (o *TaskDto) HasOutputDatasetId() bool`

HasOutputDatasetId returns a boolean if a field has been set.

### GetTaskType

`func (o *TaskDto) GetTaskType() string`

GetTaskType returns the TaskType field if non-nil, zero value otherwise.

### GetTaskTypeOk

`func (o *TaskDto) GetTaskTypeOk() (*string, bool)`

GetTaskTypeOk returns a tuple with the TaskType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTaskType

`func (o *TaskDto) SetTaskType(v string)`

SetTaskType sets TaskType field to given value.

### HasTaskType

`func (o *TaskDto) HasTaskType() bool`

HasTaskType returns a boolean if a field has been set.

### GetExecutionReferenceId

`func (o *TaskDto) GetExecutionReferenceId() string`

GetExecutionReferenceId returns the ExecutionReferenceId field if non-nil, zero value otherwise.

### GetExecutionReferenceIdOk

`func (o *TaskDto) GetExecutionReferenceIdOk() (*string, bool)`

GetExecutionReferenceIdOk returns a tuple with the ExecutionReferenceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecutionReferenceId

`func (o *TaskDto) SetExecutionReferenceId(v string)`

SetExecutionReferenceId sets ExecutionReferenceId field to given value.

### HasExecutionReferenceId

`func (o *TaskDto) HasExecutionReferenceId() bool`

HasExecutionReferenceId returns a boolean if a field has been set.

### GetExecutionStatus

`func (o *TaskDto) GetExecutionStatus() string`

GetExecutionStatus returns the ExecutionStatus field if non-nil, zero value otherwise.

### GetExecutionStatusOk

`func (o *TaskDto) GetExecutionStatusOk() (*string, bool)`

GetExecutionStatusOk returns a tuple with the ExecutionStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecutionStatus

`func (o *TaskDto) SetExecutionStatus(v string)`

SetExecutionStatus sets ExecutionStatus field to given value.

### HasExecutionStatus

`func (o *TaskDto) HasExecutionStatus() bool`

HasExecutionStatus returns a boolean if a field has been set.

### GetExecutionLog

`func (o *TaskDto) GetExecutionLog() string`

GetExecutionLog returns the ExecutionLog field if non-nil, zero value otherwise.

### GetExecutionLogOk

`func (o *TaskDto) GetExecutionLogOk() (*string, bool)`

GetExecutionLogOk returns a tuple with the ExecutionLog field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecutionLog

`func (o *TaskDto) SetExecutionLog(v string)`

SetExecutionLog sets ExecutionLog field to given value.

### HasExecutionLog

`func (o *TaskDto) HasExecutionLog() bool`

HasExecutionLog returns a boolean if a field has been set.

### GetScheduledTime

`func (o *TaskDto) GetScheduledTime() time.Time`

GetScheduledTime returns the ScheduledTime field if non-nil, zero value otherwise.

### GetScheduledTimeOk

`func (o *TaskDto) GetScheduledTimeOk() (*time.Time, bool)`

GetScheduledTimeOk returns a tuple with the ScheduledTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledTime

`func (o *TaskDto) SetScheduledTime(v time.Time)`

SetScheduledTime sets ScheduledTime field to given value.

### HasScheduledTime

`func (o *TaskDto) HasScheduledTime() bool`

HasScheduledTime returns a boolean if a field has been set.

### GetExecutionMode

`func (o *TaskDto) GetExecutionMode() string`

GetExecutionMode returns the ExecutionMode field if non-nil, zero value otherwise.

### GetExecutionModeOk

`func (o *TaskDto) GetExecutionModeOk() (*string, bool)`

GetExecutionModeOk returns a tuple with the ExecutionMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecutionMode

`func (o *TaskDto) SetExecutionMode(v string)`

SetExecutionMode sets ExecutionMode field to given value.

### HasExecutionMode

`func (o *TaskDto) HasExecutionMode() bool`

HasExecutionMode returns a boolean if a field has been set.

### GetEnabled

`func (o *TaskDto) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *TaskDto) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *TaskDto) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *TaskDto) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetApiKey

`func (o *TaskDto) GetApiKey() string`

GetApiKey returns the ApiKey field if non-nil, zero value otherwise.

### GetApiKeyOk

`func (o *TaskDto) GetApiKeyOk() (*string, bool)`

GetApiKeyOk returns a tuple with the ApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApiKey

`func (o *TaskDto) SetApiKey(v string)`

SetApiKey sets ApiKey field to given value.

### HasApiKey

`func (o *TaskDto) HasApiKey() bool`

HasApiKey returns a boolean if a field has been set.

### GetCreatedAt

`func (o *TaskDto) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *TaskDto) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *TaskDto) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *TaskDto) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *TaskDto) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *TaskDto) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *TaskDto) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *TaskDto) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


