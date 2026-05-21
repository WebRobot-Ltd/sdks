# CompletionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | Pointer to **string** |  | [optional] 
**ErrorMessage** | Pointer to **string** |  | [optional] 
**Result** | Pointer to **map[string]map[string]interface{}** |  | [optional] 
**Tokens** | Pointer to **map[string]map[string]interface{}** |  | [optional] 

## Methods

### NewCompletionRequest

`func NewCompletionRequest() *CompletionRequest`

NewCompletionRequest instantiates a new CompletionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCompletionRequestWithDefaults

`func NewCompletionRequestWithDefaults() *CompletionRequest`

NewCompletionRequestWithDefaults instantiates a new CompletionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *CompletionRequest) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *CompletionRequest) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *CompletionRequest) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *CompletionRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetErrorMessage

`func (o *CompletionRequest) GetErrorMessage() string`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *CompletionRequest) GetErrorMessageOk() (*string, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *CompletionRequest) SetErrorMessage(v string)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *CompletionRequest) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.

### GetResult

`func (o *CompletionRequest) GetResult() map[string]map[string]interface{}`

GetResult returns the Result field if non-nil, zero value otherwise.

### GetResultOk

`func (o *CompletionRequest) GetResultOk() (*map[string]map[string]interface{}, bool)`

GetResultOk returns a tuple with the Result field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResult

`func (o *CompletionRequest) SetResult(v map[string]map[string]interface{})`

SetResult sets Result field to given value.

### HasResult

`func (o *CompletionRequest) HasResult() bool`

HasResult returns a boolean if a field has been set.

### GetTokens

`func (o *CompletionRequest) GetTokens() map[string]map[string]interface{}`

GetTokens returns the Tokens field if non-nil, zero value otherwise.

### GetTokensOk

`func (o *CompletionRequest) GetTokensOk() (*map[string]map[string]interface{}, bool)`

GetTokensOk returns a tuple with the Tokens field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokens

`func (o *CompletionRequest) SetTokens(v map[string]map[string]interface{})`

SetTokens sets Tokens field to given value.

### HasTokens

`func (o *CompletionRequest) HasTokens() bool`

HasTokens returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


