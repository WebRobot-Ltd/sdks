# ProjectScheduleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CronSchedule** | Pointer to **string** |  | [optional] 
**Enabled** | Pointer to **bool** |  | [optional] 
**Timezone** | Pointer to **string** |  | [optional] 
**JobId** | Pointer to **string** |  | [optional] 
**ExecutionRequestJson** | Pointer to **string** |  | [optional] 

## Methods

### NewProjectScheduleRequest

`func NewProjectScheduleRequest() *ProjectScheduleRequest`

NewProjectScheduleRequest instantiates a new ProjectScheduleRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectScheduleRequestWithDefaults

`func NewProjectScheduleRequestWithDefaults() *ProjectScheduleRequest`

NewProjectScheduleRequestWithDefaults instantiates a new ProjectScheduleRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCronSchedule

`func (o *ProjectScheduleRequest) GetCronSchedule() string`

GetCronSchedule returns the CronSchedule field if non-nil, zero value otherwise.

### GetCronScheduleOk

`func (o *ProjectScheduleRequest) GetCronScheduleOk() (*string, bool)`

GetCronScheduleOk returns a tuple with the CronSchedule field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCronSchedule

`func (o *ProjectScheduleRequest) SetCronSchedule(v string)`

SetCronSchedule sets CronSchedule field to given value.

### HasCronSchedule

`func (o *ProjectScheduleRequest) HasCronSchedule() bool`

HasCronSchedule returns a boolean if a field has been set.

### GetEnabled

`func (o *ProjectScheduleRequest) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *ProjectScheduleRequest) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *ProjectScheduleRequest) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *ProjectScheduleRequest) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetTimezone

`func (o *ProjectScheduleRequest) GetTimezone() string`

GetTimezone returns the Timezone field if non-nil, zero value otherwise.

### GetTimezoneOk

`func (o *ProjectScheduleRequest) GetTimezoneOk() (*string, bool)`

GetTimezoneOk returns a tuple with the Timezone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimezone

`func (o *ProjectScheduleRequest) SetTimezone(v string)`

SetTimezone sets Timezone field to given value.

### HasTimezone

`func (o *ProjectScheduleRequest) HasTimezone() bool`

HasTimezone returns a boolean if a field has been set.

### GetJobId

`func (o *ProjectScheduleRequest) GetJobId() string`

GetJobId returns the JobId field if non-nil, zero value otherwise.

### GetJobIdOk

`func (o *ProjectScheduleRequest) GetJobIdOk() (*string, bool)`

GetJobIdOk returns a tuple with the JobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobId

`func (o *ProjectScheduleRequest) SetJobId(v string)`

SetJobId sets JobId field to given value.

### HasJobId

`func (o *ProjectScheduleRequest) HasJobId() bool`

HasJobId returns a boolean if a field has been set.

### GetExecutionRequestJson

`func (o *ProjectScheduleRequest) GetExecutionRequestJson() string`

GetExecutionRequestJson returns the ExecutionRequestJson field if non-nil, zero value otherwise.

### GetExecutionRequestJsonOk

`func (o *ProjectScheduleRequest) GetExecutionRequestJsonOk() (*string, bool)`

GetExecutionRequestJsonOk returns a tuple with the ExecutionRequestJson field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecutionRequestJson

`func (o *ProjectScheduleRequest) SetExecutionRequestJson(v string)`

SetExecutionRequestJson sets ExecutionRequestJson field to given value.

### HasExecutionRequestJson

`func (o *ProjectScheduleRequest) HasExecutionRequestJson() bool`

HasExecutionRequestJson returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


