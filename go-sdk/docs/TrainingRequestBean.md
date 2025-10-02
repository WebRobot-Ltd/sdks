# TrainingRequestBean

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Model** | Pointer to **string** |  | [optional] 
**TrainingFile** | Pointer to **string** |  | [optional] 
**ValidationFile** | Pointer to **string** |  | [optional] 
**DatasetId** | Pointer to **string** |  | [optional] 
**Hyperparameters** | Pointer to **map[string]map[string]interface{}** |  | [optional] 

## Methods

### NewTrainingRequestBean

`func NewTrainingRequestBean() *TrainingRequestBean`

NewTrainingRequestBean instantiates a new TrainingRequestBean object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTrainingRequestBeanWithDefaults

`func NewTrainingRequestBeanWithDefaults() *TrainingRequestBean`

NewTrainingRequestBeanWithDefaults instantiates a new TrainingRequestBean object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetModel

`func (o *TrainingRequestBean) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *TrainingRequestBean) GetModelOk() (*string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModel

`func (o *TrainingRequestBean) SetModel(v string)`

SetModel sets Model field to given value.

### HasModel

`func (o *TrainingRequestBean) HasModel() bool`

HasModel returns a boolean if a field has been set.

### GetTrainingFile

`func (o *TrainingRequestBean) GetTrainingFile() string`

GetTrainingFile returns the TrainingFile field if non-nil, zero value otherwise.

### GetTrainingFileOk

`func (o *TrainingRequestBean) GetTrainingFileOk() (*string, bool)`

GetTrainingFileOk returns a tuple with the TrainingFile field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrainingFile

`func (o *TrainingRequestBean) SetTrainingFile(v string)`

SetTrainingFile sets TrainingFile field to given value.

### HasTrainingFile

`func (o *TrainingRequestBean) HasTrainingFile() bool`

HasTrainingFile returns a boolean if a field has been set.

### GetValidationFile

`func (o *TrainingRequestBean) GetValidationFile() string`

GetValidationFile returns the ValidationFile field if non-nil, zero value otherwise.

### GetValidationFileOk

`func (o *TrainingRequestBean) GetValidationFileOk() (*string, bool)`

GetValidationFileOk returns a tuple with the ValidationFile field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValidationFile

`func (o *TrainingRequestBean) SetValidationFile(v string)`

SetValidationFile sets ValidationFile field to given value.

### HasValidationFile

`func (o *TrainingRequestBean) HasValidationFile() bool`

HasValidationFile returns a boolean if a field has been set.

### GetDatasetId

`func (o *TrainingRequestBean) GetDatasetId() string`

GetDatasetId returns the DatasetId field if non-nil, zero value otherwise.

### GetDatasetIdOk

`func (o *TrainingRequestBean) GetDatasetIdOk() (*string, bool)`

GetDatasetIdOk returns a tuple with the DatasetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatasetId

`func (o *TrainingRequestBean) SetDatasetId(v string)`

SetDatasetId sets DatasetId field to given value.

### HasDatasetId

`func (o *TrainingRequestBean) HasDatasetId() bool`

HasDatasetId returns a boolean if a field has been set.

### GetHyperparameters

`func (o *TrainingRequestBean) GetHyperparameters() map[string]map[string]interface{}`

GetHyperparameters returns the Hyperparameters field if non-nil, zero value otherwise.

### GetHyperparametersOk

`func (o *TrainingRequestBean) GetHyperparametersOk() (*map[string]map[string]interface{}, bool)`

GetHyperparametersOk returns a tuple with the Hyperparameters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHyperparameters

`func (o *TrainingRequestBean) SetHyperparameters(v map[string]map[string]interface{})`

SetHyperparameters sets Hyperparameters field to given value.

### HasHyperparameters

`func (o *TrainingRequestBean) HasHyperparameters() bool`

HasHyperparameters returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


