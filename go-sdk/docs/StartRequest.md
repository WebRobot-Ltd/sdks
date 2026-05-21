# StartRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProfileId** | Pointer to **int32** |  | [optional] 
**ProfileName** | Pointer to **string** |  | [optional] 
**ProfileUrl** | Pointer to **string** |  | [optional] 
**Inputs** | Pointer to **map[string]string** |  | [optional] 
**LlmProvider** | Pointer to **string** |  | [optional] 
**Namespace** | Pointer to **string** |  | [optional] 
**ClusterSelector** | Pointer to **string** |  | [optional] 
**Image** | Pointer to **string** |  | [optional] 
**WorkingDir** | Pointer to **string** |  | [optional] 
**Entrypoint** | Pointer to **string** |  | [optional] 
**RuntimeEnvYaml** | Pointer to **string** |  | [optional] 
**TtlSeconds** | Pointer to **int32** |  | [optional] 
**ActiveDeadlineSeconds** | Pointer to **int32** |  | [optional] 
**EnvPassthrough** | Pointer to **map[string]string** |  | [optional] 
**OrganizationId** | Pointer to **string** |  | [optional] 
**ProjectId** | Pointer to **string** |  | [optional] 
**UserId** | Pointer to **string** |  | [optional] 

## Methods

### NewStartRequest

`func NewStartRequest() *StartRequest`

NewStartRequest instantiates a new StartRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStartRequestWithDefaults

`func NewStartRequestWithDefaults() *StartRequest`

NewStartRequestWithDefaults instantiates a new StartRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProfileId

`func (o *StartRequest) GetProfileId() int32`

GetProfileId returns the ProfileId field if non-nil, zero value otherwise.

### GetProfileIdOk

`func (o *StartRequest) GetProfileIdOk() (*int32, bool)`

GetProfileIdOk returns a tuple with the ProfileId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProfileId

`func (o *StartRequest) SetProfileId(v int32)`

SetProfileId sets ProfileId field to given value.

### HasProfileId

`func (o *StartRequest) HasProfileId() bool`

HasProfileId returns a boolean if a field has been set.

### GetProfileName

`func (o *StartRequest) GetProfileName() string`

GetProfileName returns the ProfileName field if non-nil, zero value otherwise.

### GetProfileNameOk

`func (o *StartRequest) GetProfileNameOk() (*string, bool)`

GetProfileNameOk returns a tuple with the ProfileName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProfileName

`func (o *StartRequest) SetProfileName(v string)`

SetProfileName sets ProfileName field to given value.

### HasProfileName

`func (o *StartRequest) HasProfileName() bool`

HasProfileName returns a boolean if a field has been set.

### GetProfileUrl

`func (o *StartRequest) GetProfileUrl() string`

GetProfileUrl returns the ProfileUrl field if non-nil, zero value otherwise.

### GetProfileUrlOk

`func (o *StartRequest) GetProfileUrlOk() (*string, bool)`

GetProfileUrlOk returns a tuple with the ProfileUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProfileUrl

`func (o *StartRequest) SetProfileUrl(v string)`

SetProfileUrl sets ProfileUrl field to given value.

### HasProfileUrl

`func (o *StartRequest) HasProfileUrl() bool`

HasProfileUrl returns a boolean if a field has been set.

### GetInputs

`func (o *StartRequest) GetInputs() map[string]string`

GetInputs returns the Inputs field if non-nil, zero value otherwise.

### GetInputsOk

`func (o *StartRequest) GetInputsOk() (*map[string]string, bool)`

GetInputsOk returns a tuple with the Inputs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInputs

`func (o *StartRequest) SetInputs(v map[string]string)`

SetInputs sets Inputs field to given value.

### HasInputs

`func (o *StartRequest) HasInputs() bool`

HasInputs returns a boolean if a field has been set.

### GetLlmProvider

`func (o *StartRequest) GetLlmProvider() string`

GetLlmProvider returns the LlmProvider field if non-nil, zero value otherwise.

### GetLlmProviderOk

`func (o *StartRequest) GetLlmProviderOk() (*string, bool)`

GetLlmProviderOk returns a tuple with the LlmProvider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLlmProvider

`func (o *StartRequest) SetLlmProvider(v string)`

SetLlmProvider sets LlmProvider field to given value.

### HasLlmProvider

`func (o *StartRequest) HasLlmProvider() bool`

HasLlmProvider returns a boolean if a field has been set.

### GetNamespace

`func (o *StartRequest) GetNamespace() string`

GetNamespace returns the Namespace field if non-nil, zero value otherwise.

### GetNamespaceOk

`func (o *StartRequest) GetNamespaceOk() (*string, bool)`

GetNamespaceOk returns a tuple with the Namespace field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespace

`func (o *StartRequest) SetNamespace(v string)`

SetNamespace sets Namespace field to given value.

### HasNamespace

`func (o *StartRequest) HasNamespace() bool`

HasNamespace returns a boolean if a field has been set.

### GetClusterSelector

`func (o *StartRequest) GetClusterSelector() string`

GetClusterSelector returns the ClusterSelector field if non-nil, zero value otherwise.

### GetClusterSelectorOk

`func (o *StartRequest) GetClusterSelectorOk() (*string, bool)`

GetClusterSelectorOk returns a tuple with the ClusterSelector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClusterSelector

`func (o *StartRequest) SetClusterSelector(v string)`

SetClusterSelector sets ClusterSelector field to given value.

### HasClusterSelector

`func (o *StartRequest) HasClusterSelector() bool`

HasClusterSelector returns a boolean if a field has been set.

### GetImage

`func (o *StartRequest) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *StartRequest) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *StartRequest) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *StartRequest) HasImage() bool`

HasImage returns a boolean if a field has been set.

### GetWorkingDir

`func (o *StartRequest) GetWorkingDir() string`

GetWorkingDir returns the WorkingDir field if non-nil, zero value otherwise.

### GetWorkingDirOk

`func (o *StartRequest) GetWorkingDirOk() (*string, bool)`

GetWorkingDirOk returns a tuple with the WorkingDir field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkingDir

`func (o *StartRequest) SetWorkingDir(v string)`

SetWorkingDir sets WorkingDir field to given value.

### HasWorkingDir

`func (o *StartRequest) HasWorkingDir() bool`

HasWorkingDir returns a boolean if a field has been set.

### GetEntrypoint

`func (o *StartRequest) GetEntrypoint() string`

GetEntrypoint returns the Entrypoint field if non-nil, zero value otherwise.

### GetEntrypointOk

`func (o *StartRequest) GetEntrypointOk() (*string, bool)`

GetEntrypointOk returns a tuple with the Entrypoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntrypoint

`func (o *StartRequest) SetEntrypoint(v string)`

SetEntrypoint sets Entrypoint field to given value.

### HasEntrypoint

`func (o *StartRequest) HasEntrypoint() bool`

HasEntrypoint returns a boolean if a field has been set.

### GetRuntimeEnvYaml

`func (o *StartRequest) GetRuntimeEnvYaml() string`

GetRuntimeEnvYaml returns the RuntimeEnvYaml field if non-nil, zero value otherwise.

### GetRuntimeEnvYamlOk

`func (o *StartRequest) GetRuntimeEnvYamlOk() (*string, bool)`

GetRuntimeEnvYamlOk returns a tuple with the RuntimeEnvYaml field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRuntimeEnvYaml

`func (o *StartRequest) SetRuntimeEnvYaml(v string)`

SetRuntimeEnvYaml sets RuntimeEnvYaml field to given value.

### HasRuntimeEnvYaml

`func (o *StartRequest) HasRuntimeEnvYaml() bool`

HasRuntimeEnvYaml returns a boolean if a field has been set.

### GetTtlSeconds

`func (o *StartRequest) GetTtlSeconds() int32`

GetTtlSeconds returns the TtlSeconds field if non-nil, zero value otherwise.

### GetTtlSecondsOk

`func (o *StartRequest) GetTtlSecondsOk() (*int32, bool)`

GetTtlSecondsOk returns a tuple with the TtlSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTtlSeconds

`func (o *StartRequest) SetTtlSeconds(v int32)`

SetTtlSeconds sets TtlSeconds field to given value.

### HasTtlSeconds

`func (o *StartRequest) HasTtlSeconds() bool`

HasTtlSeconds returns a boolean if a field has been set.

### GetActiveDeadlineSeconds

`func (o *StartRequest) GetActiveDeadlineSeconds() int32`

GetActiveDeadlineSeconds returns the ActiveDeadlineSeconds field if non-nil, zero value otherwise.

### GetActiveDeadlineSecondsOk

`func (o *StartRequest) GetActiveDeadlineSecondsOk() (*int32, bool)`

GetActiveDeadlineSecondsOk returns a tuple with the ActiveDeadlineSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActiveDeadlineSeconds

`func (o *StartRequest) SetActiveDeadlineSeconds(v int32)`

SetActiveDeadlineSeconds sets ActiveDeadlineSeconds field to given value.

### HasActiveDeadlineSeconds

`func (o *StartRequest) HasActiveDeadlineSeconds() bool`

HasActiveDeadlineSeconds returns a boolean if a field has been set.

### GetEnvPassthrough

`func (o *StartRequest) GetEnvPassthrough() map[string]string`

GetEnvPassthrough returns the EnvPassthrough field if non-nil, zero value otherwise.

### GetEnvPassthroughOk

`func (o *StartRequest) GetEnvPassthroughOk() (*map[string]string, bool)`

GetEnvPassthroughOk returns a tuple with the EnvPassthrough field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnvPassthrough

`func (o *StartRequest) SetEnvPassthrough(v map[string]string)`

SetEnvPassthrough sets EnvPassthrough field to given value.

### HasEnvPassthrough

`func (o *StartRequest) HasEnvPassthrough() bool`

HasEnvPassthrough returns a boolean if a field has been set.

### GetOrganizationId

`func (o *StartRequest) GetOrganizationId() string`

GetOrganizationId returns the OrganizationId field if non-nil, zero value otherwise.

### GetOrganizationIdOk

`func (o *StartRequest) GetOrganizationIdOk() (*string, bool)`

GetOrganizationIdOk returns a tuple with the OrganizationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganizationId

`func (o *StartRequest) SetOrganizationId(v string)`

SetOrganizationId sets OrganizationId field to given value.

### HasOrganizationId

`func (o *StartRequest) HasOrganizationId() bool`

HasOrganizationId returns a boolean if a field has been set.

### GetProjectId

`func (o *StartRequest) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *StartRequest) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *StartRequest) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.

### HasProjectId

`func (o *StartRequest) HasProjectId() bool`

HasProjectId returns a boolean if a field has been set.

### GetUserId

`func (o *StartRequest) GetUserId() string`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *StartRequest) GetUserIdOk() (*string, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *StartRequest) SetUserId(v string)`

SetUserId sets UserId field to given value.

### HasUserId

`func (o *StartRequest) HasUserId() bool`

HasUserId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


