# AgenticProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int32** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Version** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**OrganizationId** | Pointer to **string** |  | [optional] 
**Enabled** | Pointer to **bool** |  | [optional] 
**Spec** | Pointer to **string** |  | [optional] 
**SpecYaml** | Pointer to **string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**CreatedById** | Pointer to **int32** |  | [optional] 

## Methods

### NewAgenticProfile

`func NewAgenticProfile() *AgenticProfile`

NewAgenticProfile instantiates a new AgenticProfile object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgenticProfileWithDefaults

`func NewAgenticProfileWithDefaults() *AgenticProfile`

NewAgenticProfileWithDefaults instantiates a new AgenticProfile object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *AgenticProfile) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AgenticProfile) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AgenticProfile) SetId(v int32)`

SetId sets Id field to given value.

### HasId

`func (o *AgenticProfile) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *AgenticProfile) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AgenticProfile) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AgenticProfile) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *AgenticProfile) HasName() bool`

HasName returns a boolean if a field has been set.

### GetVersion

`func (o *AgenticProfile) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *AgenticProfile) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *AgenticProfile) SetVersion(v string)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *AgenticProfile) HasVersion() bool`

HasVersion returns a boolean if a field has been set.

### GetDescription

`func (o *AgenticProfile) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *AgenticProfile) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *AgenticProfile) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *AgenticProfile) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetOrganizationId

`func (o *AgenticProfile) GetOrganizationId() string`

GetOrganizationId returns the OrganizationId field if non-nil, zero value otherwise.

### GetOrganizationIdOk

`func (o *AgenticProfile) GetOrganizationIdOk() (*string, bool)`

GetOrganizationIdOk returns a tuple with the OrganizationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganizationId

`func (o *AgenticProfile) SetOrganizationId(v string)`

SetOrganizationId sets OrganizationId field to given value.

### HasOrganizationId

`func (o *AgenticProfile) HasOrganizationId() bool`

HasOrganizationId returns a boolean if a field has been set.

### GetEnabled

`func (o *AgenticProfile) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *AgenticProfile) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *AgenticProfile) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *AgenticProfile) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetSpec

`func (o *AgenticProfile) GetSpec() string`

GetSpec returns the Spec field if non-nil, zero value otherwise.

### GetSpecOk

`func (o *AgenticProfile) GetSpecOk() (*string, bool)`

GetSpecOk returns a tuple with the Spec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpec

`func (o *AgenticProfile) SetSpec(v string)`

SetSpec sets Spec field to given value.

### HasSpec

`func (o *AgenticProfile) HasSpec() bool`

HasSpec returns a boolean if a field has been set.

### GetSpecYaml

`func (o *AgenticProfile) GetSpecYaml() string`

GetSpecYaml returns the SpecYaml field if non-nil, zero value otherwise.

### GetSpecYamlOk

`func (o *AgenticProfile) GetSpecYamlOk() (*string, bool)`

GetSpecYamlOk returns a tuple with the SpecYaml field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecYaml

`func (o *AgenticProfile) SetSpecYaml(v string)`

SetSpecYaml sets SpecYaml field to given value.

### HasSpecYaml

`func (o *AgenticProfile) HasSpecYaml() bool`

HasSpecYaml returns a boolean if a field has been set.

### GetCreatedAt

`func (o *AgenticProfile) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *AgenticProfile) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *AgenticProfile) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *AgenticProfile) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *AgenticProfile) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *AgenticProfile) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *AgenticProfile) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *AgenticProfile) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetCreatedById

`func (o *AgenticProfile) GetCreatedById() int32`

GetCreatedById returns the CreatedById field if non-nil, zero value otherwise.

### GetCreatedByIdOk

`func (o *AgenticProfile) GetCreatedByIdOk() (*int32, bool)`

GetCreatedByIdOk returns a tuple with the CreatedById field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedById

`func (o *AgenticProfile) SetCreatedById(v int32)`

SetCreatedById sets CreatedById field to given value.

### HasCreatedById

`func (o *AgenticProfile) HasCreatedById() bool`

HasCreatedById returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


