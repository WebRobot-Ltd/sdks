# ImportOptionsDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TargetOrganizationId** | Pointer to **string** |  | [optional] 
**OverwriteExisting** | Pointer to **bool** |  | [optional] 
**ImportExistingProjects** | Pointer to **bool** |  | [optional] 
**ImportExistingAgents** | Pointer to **bool** |  | [optional] 
**ImportExistingJobs** | Pointer to **bool** |  | [optional] 
**ImportExistingTasks** | Pointer to **bool** |  | [optional] 
**ImportExistingDatasets** | Pointer to **bool** |  | [optional] 

## Methods

### NewImportOptionsDto

`func NewImportOptionsDto() *ImportOptionsDto`

NewImportOptionsDto instantiates a new ImportOptionsDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewImportOptionsDtoWithDefaults

`func NewImportOptionsDtoWithDefaults() *ImportOptionsDto`

NewImportOptionsDtoWithDefaults instantiates a new ImportOptionsDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTargetOrganizationId

`func (o *ImportOptionsDto) GetTargetOrganizationId() string`

GetTargetOrganizationId returns the TargetOrganizationId field if non-nil, zero value otherwise.

### GetTargetOrganizationIdOk

`func (o *ImportOptionsDto) GetTargetOrganizationIdOk() (*string, bool)`

GetTargetOrganizationIdOk returns a tuple with the TargetOrganizationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetOrganizationId

`func (o *ImportOptionsDto) SetTargetOrganizationId(v string)`

SetTargetOrganizationId sets TargetOrganizationId field to given value.

### HasTargetOrganizationId

`func (o *ImportOptionsDto) HasTargetOrganizationId() bool`

HasTargetOrganizationId returns a boolean if a field has been set.

### GetOverwriteExisting

`func (o *ImportOptionsDto) GetOverwriteExisting() bool`

GetOverwriteExisting returns the OverwriteExisting field if non-nil, zero value otherwise.

### GetOverwriteExistingOk

`func (o *ImportOptionsDto) GetOverwriteExistingOk() (*bool, bool)`

GetOverwriteExistingOk returns a tuple with the OverwriteExisting field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOverwriteExisting

`func (o *ImportOptionsDto) SetOverwriteExisting(v bool)`

SetOverwriteExisting sets OverwriteExisting field to given value.

### HasOverwriteExisting

`func (o *ImportOptionsDto) HasOverwriteExisting() bool`

HasOverwriteExisting returns a boolean if a field has been set.

### GetImportExistingProjects

`func (o *ImportOptionsDto) GetImportExistingProjects() bool`

GetImportExistingProjects returns the ImportExistingProjects field if non-nil, zero value otherwise.

### GetImportExistingProjectsOk

`func (o *ImportOptionsDto) GetImportExistingProjectsOk() (*bool, bool)`

GetImportExistingProjectsOk returns a tuple with the ImportExistingProjects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImportExistingProjects

`func (o *ImportOptionsDto) SetImportExistingProjects(v bool)`

SetImportExistingProjects sets ImportExistingProjects field to given value.

### HasImportExistingProjects

`func (o *ImportOptionsDto) HasImportExistingProjects() bool`

HasImportExistingProjects returns a boolean if a field has been set.

### GetImportExistingAgents

`func (o *ImportOptionsDto) GetImportExistingAgents() bool`

GetImportExistingAgents returns the ImportExistingAgents field if non-nil, zero value otherwise.

### GetImportExistingAgentsOk

`func (o *ImportOptionsDto) GetImportExistingAgentsOk() (*bool, bool)`

GetImportExistingAgentsOk returns a tuple with the ImportExistingAgents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImportExistingAgents

`func (o *ImportOptionsDto) SetImportExistingAgents(v bool)`

SetImportExistingAgents sets ImportExistingAgents field to given value.

### HasImportExistingAgents

`func (o *ImportOptionsDto) HasImportExistingAgents() bool`

HasImportExistingAgents returns a boolean if a field has been set.

### GetImportExistingJobs

`func (o *ImportOptionsDto) GetImportExistingJobs() bool`

GetImportExistingJobs returns the ImportExistingJobs field if non-nil, zero value otherwise.

### GetImportExistingJobsOk

`func (o *ImportOptionsDto) GetImportExistingJobsOk() (*bool, bool)`

GetImportExistingJobsOk returns a tuple with the ImportExistingJobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImportExistingJobs

`func (o *ImportOptionsDto) SetImportExistingJobs(v bool)`

SetImportExistingJobs sets ImportExistingJobs field to given value.

### HasImportExistingJobs

`func (o *ImportOptionsDto) HasImportExistingJobs() bool`

HasImportExistingJobs returns a boolean if a field has been set.

### GetImportExistingTasks

`func (o *ImportOptionsDto) GetImportExistingTasks() bool`

GetImportExistingTasks returns the ImportExistingTasks field if non-nil, zero value otherwise.

### GetImportExistingTasksOk

`func (o *ImportOptionsDto) GetImportExistingTasksOk() (*bool, bool)`

GetImportExistingTasksOk returns a tuple with the ImportExistingTasks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImportExistingTasks

`func (o *ImportOptionsDto) SetImportExistingTasks(v bool)`

SetImportExistingTasks sets ImportExistingTasks field to given value.

### HasImportExistingTasks

`func (o *ImportOptionsDto) HasImportExistingTasks() bool`

HasImportExistingTasks returns a boolean if a field has been set.

### GetImportExistingDatasets

`func (o *ImportOptionsDto) GetImportExistingDatasets() bool`

GetImportExistingDatasets returns the ImportExistingDatasets field if non-nil, zero value otherwise.

### GetImportExistingDatasetsOk

`func (o *ImportOptionsDto) GetImportExistingDatasetsOk() (*bool, bool)`

GetImportExistingDatasetsOk returns a tuple with the ImportExistingDatasets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImportExistingDatasets

`func (o *ImportOptionsDto) SetImportExistingDatasets(v bool)`

SetImportExistingDatasets sets ImportExistingDatasets field to given value.

### HasImportExistingDatasets

`func (o *ImportOptionsDto) HasImportExistingDatasets() bool`

HasImportExistingDatasets returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


