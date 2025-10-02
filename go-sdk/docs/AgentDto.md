# AgentDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Enabled** | Pointer to **bool** |  | [optional] 
**ApiEndpoint** | Pointer to **string** |  | [optional] 
**ExecutionMode** | Pointer to **string** |  | [optional] 
**CategoryId** | Pointer to **string** |  | [optional] 
**Type** | Pointer to **string** |  | [optional] 
**Role** | Pointer to **string** |  | [optional] 
**Backstory** | Pointer to **string** |  | [optional] 
**DefaultPrompt** | Pointer to **string** |  | [optional] 
**Prompts** | Pointer to **string** |  | [optional] 
**Config** | Pointer to **string** |  | [optional] 
**Code** | Pointer to **string** |  | [optional] 
**CodeTypeId** | Pointer to **string** |  | [optional] 
**PysparkCode** | Pointer to **string** |  | [optional] 
**PythonExtensions** | Pointer to **string** |  | [optional] 
**GeneratedAt** | Pointer to **time.Time** |  | [optional] 
**ToolIds** | Pointer to **[]string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewAgentDto

`func NewAgentDto() *AgentDto`

NewAgentDto instantiates a new AgentDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgentDtoWithDefaults

`func NewAgentDtoWithDefaults() *AgentDto`

NewAgentDtoWithDefaults instantiates a new AgentDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *AgentDto) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AgentDto) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AgentDto) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *AgentDto) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *AgentDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AgentDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AgentDto) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *AgentDto) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *AgentDto) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *AgentDto) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *AgentDto) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *AgentDto) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetEnabled

`func (o *AgentDto) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *AgentDto) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *AgentDto) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *AgentDto) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetApiEndpoint

`func (o *AgentDto) GetApiEndpoint() string`

GetApiEndpoint returns the ApiEndpoint field if non-nil, zero value otherwise.

### GetApiEndpointOk

`func (o *AgentDto) GetApiEndpointOk() (*string, bool)`

GetApiEndpointOk returns a tuple with the ApiEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApiEndpoint

`func (o *AgentDto) SetApiEndpoint(v string)`

SetApiEndpoint sets ApiEndpoint field to given value.

### HasApiEndpoint

`func (o *AgentDto) HasApiEndpoint() bool`

HasApiEndpoint returns a boolean if a field has been set.

### GetExecutionMode

`func (o *AgentDto) GetExecutionMode() string`

GetExecutionMode returns the ExecutionMode field if non-nil, zero value otherwise.

### GetExecutionModeOk

`func (o *AgentDto) GetExecutionModeOk() (*string, bool)`

GetExecutionModeOk returns a tuple with the ExecutionMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExecutionMode

`func (o *AgentDto) SetExecutionMode(v string)`

SetExecutionMode sets ExecutionMode field to given value.

### HasExecutionMode

`func (o *AgentDto) HasExecutionMode() bool`

HasExecutionMode returns a boolean if a field has been set.

### GetCategoryId

`func (o *AgentDto) GetCategoryId() string`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *AgentDto) GetCategoryIdOk() (*string, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *AgentDto) SetCategoryId(v string)`

SetCategoryId sets CategoryId field to given value.

### HasCategoryId

`func (o *AgentDto) HasCategoryId() bool`

HasCategoryId returns a boolean if a field has been set.

### GetType

`func (o *AgentDto) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *AgentDto) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *AgentDto) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *AgentDto) HasType() bool`

HasType returns a boolean if a field has been set.

### GetRole

`func (o *AgentDto) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *AgentDto) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *AgentDto) SetRole(v string)`

SetRole sets Role field to given value.

### HasRole

`func (o *AgentDto) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetBackstory

`func (o *AgentDto) GetBackstory() string`

GetBackstory returns the Backstory field if non-nil, zero value otherwise.

### GetBackstoryOk

`func (o *AgentDto) GetBackstoryOk() (*string, bool)`

GetBackstoryOk returns a tuple with the Backstory field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBackstory

`func (o *AgentDto) SetBackstory(v string)`

SetBackstory sets Backstory field to given value.

### HasBackstory

`func (o *AgentDto) HasBackstory() bool`

HasBackstory returns a boolean if a field has been set.

### GetDefaultPrompt

`func (o *AgentDto) GetDefaultPrompt() string`

GetDefaultPrompt returns the DefaultPrompt field if non-nil, zero value otherwise.

### GetDefaultPromptOk

`func (o *AgentDto) GetDefaultPromptOk() (*string, bool)`

GetDefaultPromptOk returns a tuple with the DefaultPrompt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultPrompt

`func (o *AgentDto) SetDefaultPrompt(v string)`

SetDefaultPrompt sets DefaultPrompt field to given value.

### HasDefaultPrompt

`func (o *AgentDto) HasDefaultPrompt() bool`

HasDefaultPrompt returns a boolean if a field has been set.

### GetPrompts

`func (o *AgentDto) GetPrompts() string`

GetPrompts returns the Prompts field if non-nil, zero value otherwise.

### GetPromptsOk

`func (o *AgentDto) GetPromptsOk() (*string, bool)`

GetPromptsOk returns a tuple with the Prompts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrompts

`func (o *AgentDto) SetPrompts(v string)`

SetPrompts sets Prompts field to given value.

### HasPrompts

`func (o *AgentDto) HasPrompts() bool`

HasPrompts returns a boolean if a field has been set.

### GetConfig

`func (o *AgentDto) GetConfig() string`

GetConfig returns the Config field if non-nil, zero value otherwise.

### GetConfigOk

`func (o *AgentDto) GetConfigOk() (*string, bool)`

GetConfigOk returns a tuple with the Config field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfig

`func (o *AgentDto) SetConfig(v string)`

SetConfig sets Config field to given value.

### HasConfig

`func (o *AgentDto) HasConfig() bool`

HasConfig returns a boolean if a field has been set.

### GetCode

`func (o *AgentDto) GetCode() string`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *AgentDto) GetCodeOk() (*string, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *AgentDto) SetCode(v string)`

SetCode sets Code field to given value.

### HasCode

`func (o *AgentDto) HasCode() bool`

HasCode returns a boolean if a field has been set.

### GetCodeTypeId

`func (o *AgentDto) GetCodeTypeId() string`

GetCodeTypeId returns the CodeTypeId field if non-nil, zero value otherwise.

### GetCodeTypeIdOk

`func (o *AgentDto) GetCodeTypeIdOk() (*string, bool)`

GetCodeTypeIdOk returns a tuple with the CodeTypeId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCodeTypeId

`func (o *AgentDto) SetCodeTypeId(v string)`

SetCodeTypeId sets CodeTypeId field to given value.

### HasCodeTypeId

`func (o *AgentDto) HasCodeTypeId() bool`

HasCodeTypeId returns a boolean if a field has been set.

### GetPysparkCode

`func (o *AgentDto) GetPysparkCode() string`

GetPysparkCode returns the PysparkCode field if non-nil, zero value otherwise.

### GetPysparkCodeOk

`func (o *AgentDto) GetPysparkCodeOk() (*string, bool)`

GetPysparkCodeOk returns a tuple with the PysparkCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPysparkCode

`func (o *AgentDto) SetPysparkCode(v string)`

SetPysparkCode sets PysparkCode field to given value.

### HasPysparkCode

`func (o *AgentDto) HasPysparkCode() bool`

HasPysparkCode returns a boolean if a field has been set.

### GetPythonExtensions

`func (o *AgentDto) GetPythonExtensions() string`

GetPythonExtensions returns the PythonExtensions field if non-nil, zero value otherwise.

### GetPythonExtensionsOk

`func (o *AgentDto) GetPythonExtensionsOk() (*string, bool)`

GetPythonExtensionsOk returns a tuple with the PythonExtensions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPythonExtensions

`func (o *AgentDto) SetPythonExtensions(v string)`

SetPythonExtensions sets PythonExtensions field to given value.

### HasPythonExtensions

`func (o *AgentDto) HasPythonExtensions() bool`

HasPythonExtensions returns a boolean if a field has been set.

### GetGeneratedAt

`func (o *AgentDto) GetGeneratedAt() time.Time`

GetGeneratedAt returns the GeneratedAt field if non-nil, zero value otherwise.

### GetGeneratedAtOk

`func (o *AgentDto) GetGeneratedAtOk() (*time.Time, bool)`

GetGeneratedAtOk returns a tuple with the GeneratedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeneratedAt

`func (o *AgentDto) SetGeneratedAt(v time.Time)`

SetGeneratedAt sets GeneratedAt field to given value.

### HasGeneratedAt

`func (o *AgentDto) HasGeneratedAt() bool`

HasGeneratedAt returns a boolean if a field has been set.

### GetToolIds

`func (o *AgentDto) GetToolIds() []string`

GetToolIds returns the ToolIds field if non-nil, zero value otherwise.

### GetToolIdsOk

`func (o *AgentDto) GetToolIdsOk() (*[]string, bool)`

GetToolIdsOk returns a tuple with the ToolIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolIds

`func (o *AgentDto) SetToolIds(v []string)`

SetToolIds sets ToolIds field to given value.

### HasToolIds

`func (o *AgentDto) HasToolIds() bool`

HasToolIds returns a boolean if a field has been set.

### GetCreatedAt

`func (o *AgentDto) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *AgentDto) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *AgentDto) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *AgentDto) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *AgentDto) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *AgentDto) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *AgentDto) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *AgentDto) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


