# JobProjectDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**CronSchedule** | Pointer to **string** |  | [optional] 
**Enabled** | Pointer to **bool** |  | [optional] 
**JobIds** | Pointer to **[]string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewJobProjectDto

`func NewJobProjectDto() *JobProjectDto`

NewJobProjectDto instantiates a new JobProjectDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewJobProjectDtoWithDefaults

`func NewJobProjectDtoWithDefaults() *JobProjectDto`

NewJobProjectDtoWithDefaults instantiates a new JobProjectDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *JobProjectDto) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *JobProjectDto) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *JobProjectDto) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *JobProjectDto) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *JobProjectDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *JobProjectDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *JobProjectDto) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *JobProjectDto) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *JobProjectDto) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *JobProjectDto) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *JobProjectDto) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *JobProjectDto) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetCronSchedule

`func (o *JobProjectDto) GetCronSchedule() string`

GetCronSchedule returns the CronSchedule field if non-nil, zero value otherwise.

### GetCronScheduleOk

`func (o *JobProjectDto) GetCronScheduleOk() (*string, bool)`

GetCronScheduleOk returns a tuple with the CronSchedule field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCronSchedule

`func (o *JobProjectDto) SetCronSchedule(v string)`

SetCronSchedule sets CronSchedule field to given value.

### HasCronSchedule

`func (o *JobProjectDto) HasCronSchedule() bool`

HasCronSchedule returns a boolean if a field has been set.

### GetEnabled

`func (o *JobProjectDto) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *JobProjectDto) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *JobProjectDto) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *JobProjectDto) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetJobIds

`func (o *JobProjectDto) GetJobIds() []string`

GetJobIds returns the JobIds field if non-nil, zero value otherwise.

### GetJobIdsOk

`func (o *JobProjectDto) GetJobIdsOk() (*[]string, bool)`

GetJobIdsOk returns a tuple with the JobIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobIds

`func (o *JobProjectDto) SetJobIds(v []string)`

SetJobIds sets JobIds field to given value.

### HasJobIds

`func (o *JobProjectDto) HasJobIds() bool`

HasJobIds returns a boolean if a field has been set.

### GetCreatedAt

`func (o *JobProjectDto) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *JobProjectDto) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *JobProjectDto) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *JobProjectDto) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *JobProjectDto) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *JobProjectDto) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *JobProjectDto) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *JobProjectDto) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


