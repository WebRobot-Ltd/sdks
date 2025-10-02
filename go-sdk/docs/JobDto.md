# JobDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**ProjectId** | Pointer to **string** |  | [optional] 
**AgentId** | Pointer to **string** |  | [optional] 
**InputDatasetId** | Pointer to **string** |  | [optional] 
**ExecutionStatus** | Pointer to **string** |  | [optional] 
**ScheduledTime** | Pointer to **time.Time** |  | [optional] 
**Enabled** | Pointer to **bool** |  | [optional] 
**TaskIds** | Pointer to **[]string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewJobDto

`func NewJobDto() *JobDto`

NewJobDto instantiates a new JobDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewJobDtoWithDefaults

`func NewJobDtoWithDefaults() *JobDto`

NewJobDtoWithDefaults instantiates a new JobDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *JobDto) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *JobDto) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *JobDto) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *JobDto) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *JobDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *JobDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *JobDto) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *JobDto) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *JobDto) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *JobDto) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *JobDto) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *JobDto) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetProjectId

`func (o *JobDto) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *JobDto) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *JobDto) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.

### HasProjectId

`func (o *JobDto) HasProjectId() bool`

HasProjectId returns a boolean if a field has been set.

### GetAgentId

`func (o *JobDto) GetAgentId() string`

GetAgentId returns the AgentId field if non-nil, zero value otherwise.

### GetAgentIdOk

`func (o *JobDto) GetAgentIdOk() (*string, bool)`

GetAgentIdOk returns a tuple with the AgentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAgentId

`func (o *JobDto) SetAgentId(v string)`

SetAgentId sets AgentId field to given value.

### HasAgentId

`func (o *JobDto) HasAgentId() bool`

HasAgentId returns a boolean if a field has been set.

### GetInputDatasetId

`func (o *JobDto) GetInputDatasetId() string`

GetInputDatasetId returns the InputDatasetId field if non-nil, zero value otherwise.

### GetInputDatasetIdOk

`func (o *JobDto) GetInputDatasetIdOk() (*string, bool)`

GetInputDatasetIdOk returns a tuple with the InputDatasetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInputDatasetId

`func (o *JobDto) SetInputDatasetId(v string)`

SetInputDatasetId sets InputDatasetId field to given value.

### HasInputDatasetId

`func (o *JobDto) HasInputDatasetId() bool`

HasInputDatasetId returns a boolean if a field has been set.

### GetExecutionStatus

`func (o *JobDto) GetExecutionStatus() string`

GetExecutionStatus returns the ExecutionStatus field if non-nil, zero value otherwise.

### GetExecutionStatusOk

`func (o *JobDto) GetExecutionStatusOk() (*string, bool)`

GetExecutionStatusOk returns a tuple with the ExecutionStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecutionStatus

`func (o *JobDto) SetExecutionStatus(v string)`

SetExecutionStatus sets ExecutionStatus field to given value.

### HasExecutionStatus

`func (o *JobDto) HasExecutionStatus() bool`

HasExecutionStatus returns a boolean if a field has been set.

### GetScheduledTime

`func (o *JobDto) GetScheduledTime() time.Time`

GetScheduledTime returns the ScheduledTime field if non-nil, zero value otherwise.

### GetScheduledTimeOk

`func (o *JobDto) GetScheduledTimeOk() (*time.Time, bool)`

GetScheduledTimeOk returns a tuple with the ScheduledTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledTime

`func (o *JobDto) SetScheduledTime(v time.Time)`

SetScheduledTime sets ScheduledTime field to given value.

### HasScheduledTime

`func (o *JobDto) HasScheduledTime() bool`

HasScheduledTime returns a boolean if a field has been set.

### GetEnabled

`func (o *JobDto) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *JobDto) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *JobDto) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *JobDto) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetTaskIds

`func (o *JobDto) GetTaskIds() []string`

GetTaskIds returns the TaskIds field if non-nil, zero value otherwise.

### GetTaskIdsOk

`func (o *JobDto) GetTaskIdsOk() (*[]string, bool)`

GetTaskIdsOk returns a tuple with the TaskIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTaskIds

`func (o *JobDto) SetTaskIds(v []string)`

SetTaskIds sets TaskIds field to given value.

### HasTaskIds

`func (o *JobDto) HasTaskIds() bool`

HasTaskIds returns a boolean if a field has been set.

### GetCreatedAt

`func (o *JobDto) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *JobDto) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *JobDto) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *JobDto) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *JobDto) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *JobDto) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *JobDto) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *JobDto) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


