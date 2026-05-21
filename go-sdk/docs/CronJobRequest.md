# CronJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** |  | [optional] 
**Namespace** | Pointer to **string** |  | [optional] 
**Schedule** | Pointer to **string** |  | [optional] 
**WebhookUrl** | Pointer to **string** |  | [optional] 
**JobId** | Pointer to **string** |  | [optional] 
**ProjectId** | Pointer to **string** |  | [optional] 
**ClusterProvider** | Pointer to **string** |  | [optional] 
**ClusterConfigId** | Pointer to **string** |  | [optional] 
**SecretName** | Pointer to **string** |  | [optional] 
**SecretKey** | Pointer to **string** |  | [optional] 
**Image** | Pointer to **string** |  | [optional] 

## Methods

### NewCronJobRequest

`func NewCronJobRequest() *CronJobRequest`

NewCronJobRequest instantiates a new CronJobRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCronJobRequestWithDefaults

`func NewCronJobRequestWithDefaults() *CronJobRequest`

NewCronJobRequestWithDefaults instantiates a new CronJobRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CronJobRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CronJobRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CronJobRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *CronJobRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### GetNamespace

`func (o *CronJobRequest) GetNamespace() string`

GetNamespace returns the Namespace field if non-nil, zero value otherwise.

### GetNamespaceOk

`func (o *CronJobRequest) GetNamespaceOk() (*string, bool)`

GetNamespaceOk returns a tuple with the Namespace field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespace

`func (o *CronJobRequest) SetNamespace(v string)`

SetNamespace sets Namespace field to given value.

### HasNamespace

`func (o *CronJobRequest) HasNamespace() bool`

HasNamespace returns a boolean if a field has been set.

### GetSchedule

`func (o *CronJobRequest) GetSchedule() string`

GetSchedule returns the Schedule field if non-nil, zero value otherwise.

### GetScheduleOk

`func (o *CronJobRequest) GetScheduleOk() (*string, bool)`

GetScheduleOk returns a tuple with the Schedule field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSchedule

`func (o *CronJobRequest) SetSchedule(v string)`

SetSchedule sets Schedule field to given value.

### HasSchedule

`func (o *CronJobRequest) HasSchedule() bool`

HasSchedule returns a boolean if a field has been set.

### GetWebhookUrl

`func (o *CronJobRequest) GetWebhookUrl() string`

GetWebhookUrl returns the WebhookUrl field if non-nil, zero value otherwise.

### GetWebhookUrlOk

`func (o *CronJobRequest) GetWebhookUrlOk() (*string, bool)`

GetWebhookUrlOk returns a tuple with the WebhookUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebhookUrl

`func (o *CronJobRequest) SetWebhookUrl(v string)`

SetWebhookUrl sets WebhookUrl field to given value.

### HasWebhookUrl

`func (o *CronJobRequest) HasWebhookUrl() bool`

HasWebhookUrl returns a boolean if a field has been set.

### GetJobId

`func (o *CronJobRequest) GetJobId() string`

GetJobId returns the JobId field if non-nil, zero value otherwise.

### GetJobIdOk

`func (o *CronJobRequest) GetJobIdOk() (*string, bool)`

GetJobIdOk returns a tuple with the JobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobId

`func (o *CronJobRequest) SetJobId(v string)`

SetJobId sets JobId field to given value.

### HasJobId

`func (o *CronJobRequest) HasJobId() bool`

HasJobId returns a boolean if a field has been set.

### GetProjectId

`func (o *CronJobRequest) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *CronJobRequest) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *CronJobRequest) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.

### HasProjectId

`func (o *CronJobRequest) HasProjectId() bool`

HasProjectId returns a boolean if a field has been set.

### GetClusterProvider

`func (o *CronJobRequest) GetClusterProvider() string`

GetClusterProvider returns the ClusterProvider field if non-nil, zero value otherwise.

### GetClusterProviderOk

`func (o *CronJobRequest) GetClusterProviderOk() (*string, bool)`

GetClusterProviderOk returns a tuple with the ClusterProvider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClusterProvider

`func (o *CronJobRequest) SetClusterProvider(v string)`

SetClusterProvider sets ClusterProvider field to given value.

### HasClusterProvider

`func (o *CronJobRequest) HasClusterProvider() bool`

HasClusterProvider returns a boolean if a field has been set.

### GetClusterConfigId

`func (o *CronJobRequest) GetClusterConfigId() string`

GetClusterConfigId returns the ClusterConfigId field if non-nil, zero value otherwise.

### GetClusterConfigIdOk

`func (o *CronJobRequest) GetClusterConfigIdOk() (*string, bool)`

GetClusterConfigIdOk returns a tuple with the ClusterConfigId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClusterConfigId

`func (o *CronJobRequest) SetClusterConfigId(v string)`

SetClusterConfigId sets ClusterConfigId field to given value.

### HasClusterConfigId

`func (o *CronJobRequest) HasClusterConfigId() bool`

HasClusterConfigId returns a boolean if a field has been set.

### GetSecretName

`func (o *CronJobRequest) GetSecretName() string`

GetSecretName returns the SecretName field if non-nil, zero value otherwise.

### GetSecretNameOk

`func (o *CronJobRequest) GetSecretNameOk() (*string, bool)`

GetSecretNameOk returns a tuple with the SecretName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecretName

`func (o *CronJobRequest) SetSecretName(v string)`

SetSecretName sets SecretName field to given value.

### HasSecretName

`func (o *CronJobRequest) HasSecretName() bool`

HasSecretName returns a boolean if a field has been set.

### GetSecretKey

`func (o *CronJobRequest) GetSecretKey() string`

GetSecretKey returns the SecretKey field if non-nil, zero value otherwise.

### GetSecretKeyOk

`func (o *CronJobRequest) GetSecretKeyOk() (*string, bool)`

GetSecretKeyOk returns a tuple with the SecretKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecretKey

`func (o *CronJobRequest) SetSecretKey(v string)`

SetSecretKey sets SecretKey field to given value.

### HasSecretKey

`func (o *CronJobRequest) HasSecretKey() bool`

HasSecretKey returns a boolean if a field has been set.

### GetImage

`func (o *CronJobRequest) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *CronJobRequest) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *CronJobRequest) SetImage(v string)`

SetImage sets Image field to given value.

### HasImage

`func (o *CronJobRequest) HasImage() bool`

HasImage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


