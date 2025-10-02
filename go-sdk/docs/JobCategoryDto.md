# JobCategoryDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Icon** | Pointer to **string** |  | [optional] 
**Visibility** | Pointer to **string** |  | [optional] 
**Enabled** | Pointer to **bool** |  | [optional] 
**AgentIds** | Pointer to **[]string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewJobCategoryDto

`func NewJobCategoryDto() *JobCategoryDto`

NewJobCategoryDto instantiates a new JobCategoryDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewJobCategoryDtoWithDefaults

`func NewJobCategoryDtoWithDefaults() *JobCategoryDto`

NewJobCategoryDtoWithDefaults instantiates a new JobCategoryDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *JobCategoryDto) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *JobCategoryDto) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *JobCategoryDto) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *JobCategoryDto) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *JobCategoryDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *JobCategoryDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *JobCategoryDto) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *JobCategoryDto) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *JobCategoryDto) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *JobCategoryDto) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *JobCategoryDto) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *JobCategoryDto) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetIcon

`func (o *JobCategoryDto) GetIcon() string`

GetIcon returns the Icon field if non-nil, zero value otherwise.

### GetIconOk

`func (o *JobCategoryDto) GetIconOk() (*string, bool)`

GetIconOk returns a tuple with the Icon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIcon

`func (o *JobCategoryDto) SetIcon(v string)`

SetIcon sets Icon field to given value.

### HasIcon

`func (o *JobCategoryDto) HasIcon() bool`

HasIcon returns a boolean if a field has been set.

### GetVisibility

`func (o *JobCategoryDto) GetVisibility() string`

GetVisibility returns the Visibility field if non-nil, zero value otherwise.

### GetVisibilityOk

`func (o *JobCategoryDto) GetVisibilityOk() (*string, bool)`

GetVisibilityOk returns a tuple with the Visibility field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVisibility

`func (o *JobCategoryDto) SetVisibility(v string)`

SetVisibility sets Visibility field to given value.

### HasVisibility

`func (o *JobCategoryDto) HasVisibility() bool`

HasVisibility returns a boolean if a field has been set.

### GetEnabled

`func (o *JobCategoryDto) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *JobCategoryDto) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *JobCategoryDto) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *JobCategoryDto) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetAgentIds

`func (o *JobCategoryDto) GetAgentIds() []string`

GetAgentIds returns the AgentIds field if non-nil, zero value otherwise.

### GetAgentIdsOk

`func (o *JobCategoryDto) GetAgentIdsOk() (*[]string, bool)`

GetAgentIdsOk returns a tuple with the AgentIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAgentIds

`func (o *JobCategoryDto) SetAgentIds(v []string)`

SetAgentIds sets AgentIds field to given value.

### HasAgentIds

`func (o *JobCategoryDto) HasAgentIds() bool`

HasAgentIds returns a boolean if a field has been set.

### GetCreatedAt

`func (o *JobCategoryDto) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *JobCategoryDto) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *JobCategoryDto) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *JobCategoryDto) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *JobCategoryDto) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *JobCategoryDto) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *JobCategoryDto) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *JobCategoryDto) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


