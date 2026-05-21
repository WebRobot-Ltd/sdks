# CloudCredential

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int32** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Provider** | Pointer to **string** |  | [optional] 
**ApiKey** | Pointer to **string** |  | [optional] 
**ApiSecret** | Pointer to **string** |  | [optional] 
**OrganizationId** | Pointer to **string** |  | [optional] 
**ProjectId** | Pointer to **string** |  | [optional] 
**Region** | Pointer to **string** |  | [optional] 
**Endpoint** | Pointer to **string** |  | [optional] 
**AccessKeyId** | Pointer to **string** |  | [optional] 
**SecretAccessKey** | Pointer to **string** |  | [optional] 
**SessionToken** | Pointer to **string** |  | [optional] 
**AccountId** | Pointer to **string** |  | [optional] 
**SubscriptionId** | Pointer to **string** |  | [optional] 
**ResourceGroup** | Pointer to **string** |  | [optional] 
**WorkspaceName** | Pointer to **string** |  | [optional] 
**HuggingFaceToken** | Pointer to **string** |  | [optional] 
**CohereApiKey** | Pointer to **string** |  | [optional] 
**AzureAiStudioEndpoint** | Pointer to **string** |  | [optional] 
**MosaicmlApiKey** | Pointer to **string** |  | [optional] 
**ReplicateApiToken** | Pointer to **string** |  | [optional] 
**TwitterBearerToken** | Pointer to **string** |  | [optional] 
**TwitterApiKey** | Pointer to **string** |  | [optional] 
**TwitterApiSecret** | Pointer to **string** |  | [optional] 
**RedditClientId** | Pointer to **string** |  | [optional] 
**RedditClientSecret** | Pointer to **string** |  | [optional] 
**RedditUserAgent** | Pointer to **string** |  | [optional] 
**FacebookAccessToken** | Pointer to **string** |  | [optional] 
**FacebookAppId** | Pointer to **string** |  | [optional] 
**FacebookAppSecret** | Pointer to **string** |  | [optional] 
**InstagramAccessToken** | Pointer to **string** |  | [optional] 
**LinkedinAccessToken** | Pointer to **string** |  | [optional] 
**LinkedinClientId** | Pointer to **string** |  | [optional] 
**LinkedinClientSecret** | Pointer to **string** |  | [optional] 
**TiktokClientKey** | Pointer to **string** |  | [optional] 
**TiktokClientSecret** | Pointer to **string** |  | [optional] 
**YoutubeApiKey** | Pointer to **string** |  | [optional] 
**DatabricksWorkspaceUrl** | Pointer to **string** |  | [optional] 
**DatabricksAccessToken** | Pointer to **string** |  | [optional] 
**DatabricksClusterId** | Pointer to **string** |  | [optional] 
**OauthAccessToken** | Pointer to **string** |  | [optional] 
**OauthRefreshToken** | Pointer to **string** |  | [optional] 
**OauthTokenExpiresAt** | Pointer to **time.Time** |  | [optional] 
**OauthTokenType** | Pointer to **string** |  | [optional] 
**AlphavantageApiKey** | Pointer to **string** |  | [optional] 
**PolygonApiKey** | Pointer to **string** |  | [optional] 
**TwelvedataApiKey** | Pointer to **string** |  | [optional] 
**MarketstackAccessKey** | Pointer to **string** |  | [optional] 
**FmpApiKey** | Pointer to **string** |  | [optional] 
**IexcloudToken** | Pointer to **string** |  | [optional] 
**CbondApiKey** | Pointer to **string** |  | [optional] 
**CbondClientId** | Pointer to **string** |  | [optional] 
**CbondClientSecret** | Pointer to **string** |  | [optional] 
**GoogleSearchEngineId** | Pointer to **string** |  | [optional] 
**BingSearchApiKey** | Pointer to **string** |  | [optional] 
**Enabled** | Pointer to **bool** |  | [optional] 

## Methods

### NewCloudCredential

`func NewCloudCredential() *CloudCredential`

NewCloudCredential instantiates a new CloudCredential object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCloudCredentialWithDefaults

`func NewCloudCredentialWithDefaults() *CloudCredential`

NewCloudCredentialWithDefaults instantiates a new CloudCredential object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *CloudCredential) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CloudCredential) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CloudCredential) SetId(v int32)`

SetId sets Id field to given value.

### HasId

`func (o *CloudCredential) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *CloudCredential) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CloudCredential) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CloudCredential) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *CloudCredential) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *CloudCredential) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CloudCredential) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CloudCredential) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CloudCredential) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetProvider

`func (o *CloudCredential) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *CloudCredential) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *CloudCredential) SetProvider(v string)`

SetProvider sets Provider field to given value.

### HasProvider

`func (o *CloudCredential) HasProvider() bool`

HasProvider returns a boolean if a field has been set.

### GetApiKey

`func (o *CloudCredential) GetApiKey() string`

GetApiKey returns the ApiKey field if non-nil, zero value otherwise.

### GetApiKeyOk

`func (o *CloudCredential) GetApiKeyOk() (*string, bool)`

GetApiKeyOk returns a tuple with the ApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApiKey

`func (o *CloudCredential) SetApiKey(v string)`

SetApiKey sets ApiKey field to given value.

### HasApiKey

`func (o *CloudCredential) HasApiKey() bool`

HasApiKey returns a boolean if a field has been set.

### GetApiSecret

`func (o *CloudCredential) GetApiSecret() string`

GetApiSecret returns the ApiSecret field if non-nil, zero value otherwise.

### GetApiSecretOk

`func (o *CloudCredential) GetApiSecretOk() (*string, bool)`

GetApiSecretOk returns a tuple with the ApiSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApiSecret

`func (o *CloudCredential) SetApiSecret(v string)`

SetApiSecret sets ApiSecret field to given value.

### HasApiSecret

`func (o *CloudCredential) HasApiSecret() bool`

HasApiSecret returns a boolean if a field has been set.

### GetOrganizationId

`func (o *CloudCredential) GetOrganizationId() string`

GetOrganizationId returns the OrganizationId field if non-nil, zero value otherwise.

### GetOrganizationIdOk

`func (o *CloudCredential) GetOrganizationIdOk() (*string, bool)`

GetOrganizationIdOk returns a tuple with the OrganizationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganizationId

`func (o *CloudCredential) SetOrganizationId(v string)`

SetOrganizationId sets OrganizationId field to given value.

### HasOrganizationId

`func (o *CloudCredential) HasOrganizationId() bool`

HasOrganizationId returns a boolean if a field has been set.

### GetProjectId

`func (o *CloudCredential) GetProjectId() string`

GetProjectId returns the ProjectId field if non-nil, zero value otherwise.

### GetProjectIdOk

`func (o *CloudCredential) GetProjectIdOk() (*string, bool)`

GetProjectIdOk returns a tuple with the ProjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProjectId

`func (o *CloudCredential) SetProjectId(v string)`

SetProjectId sets ProjectId field to given value.

### HasProjectId

`func (o *CloudCredential) HasProjectId() bool`

HasProjectId returns a boolean if a field has been set.

### GetRegion

`func (o *CloudCredential) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *CloudCredential) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *CloudCredential) SetRegion(v string)`

SetRegion sets Region field to given value.

### HasRegion

`func (o *CloudCredential) HasRegion() bool`

HasRegion returns a boolean if a field has been set.

### GetEndpoint

`func (o *CloudCredential) GetEndpoint() string`

GetEndpoint returns the Endpoint field if non-nil, zero value otherwise.

### GetEndpointOk

`func (o *CloudCredential) GetEndpointOk() (*string, bool)`

GetEndpointOk returns a tuple with the Endpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndpoint

`func (o *CloudCredential) SetEndpoint(v string)`

SetEndpoint sets Endpoint field to given value.

### HasEndpoint

`func (o *CloudCredential) HasEndpoint() bool`

HasEndpoint returns a boolean if a field has been set.

### GetAccessKeyId

`func (o *CloudCredential) GetAccessKeyId() string`

GetAccessKeyId returns the AccessKeyId field if non-nil, zero value otherwise.

### GetAccessKeyIdOk

`func (o *CloudCredential) GetAccessKeyIdOk() (*string, bool)`

GetAccessKeyIdOk returns a tuple with the AccessKeyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccessKeyId

`func (o *CloudCredential) SetAccessKeyId(v string)`

SetAccessKeyId sets AccessKeyId field to given value.

### HasAccessKeyId

`func (o *CloudCredential) HasAccessKeyId() bool`

HasAccessKeyId returns a boolean if a field has been set.

### GetSecretAccessKey

`func (o *CloudCredential) GetSecretAccessKey() string`

GetSecretAccessKey returns the SecretAccessKey field if non-nil, zero value otherwise.

### GetSecretAccessKeyOk

`func (o *CloudCredential) GetSecretAccessKeyOk() (*string, bool)`

GetSecretAccessKeyOk returns a tuple with the SecretAccessKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecretAccessKey

`func (o *CloudCredential) SetSecretAccessKey(v string)`

SetSecretAccessKey sets SecretAccessKey field to given value.

### HasSecretAccessKey

`func (o *CloudCredential) HasSecretAccessKey() bool`

HasSecretAccessKey returns a boolean if a field has been set.

### GetSessionToken

`func (o *CloudCredential) GetSessionToken() string`

GetSessionToken returns the SessionToken field if non-nil, zero value otherwise.

### GetSessionTokenOk

`func (o *CloudCredential) GetSessionTokenOk() (*string, bool)`

GetSessionTokenOk returns a tuple with the SessionToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSessionToken

`func (o *CloudCredential) SetSessionToken(v string)`

SetSessionToken sets SessionToken field to given value.

### HasSessionToken

`func (o *CloudCredential) HasSessionToken() bool`

HasSessionToken returns a boolean if a field has been set.

### GetAccountId

`func (o *CloudCredential) GetAccountId() string`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *CloudCredential) GetAccountIdOk() (*string, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *CloudCredential) SetAccountId(v string)`

SetAccountId sets AccountId field to given value.

### HasAccountId

`func (o *CloudCredential) HasAccountId() bool`

HasAccountId returns a boolean if a field has been set.

### GetSubscriptionId

`func (o *CloudCredential) GetSubscriptionId() string`

GetSubscriptionId returns the SubscriptionId field if non-nil, zero value otherwise.

### GetSubscriptionIdOk

`func (o *CloudCredential) GetSubscriptionIdOk() (*string, bool)`

GetSubscriptionIdOk returns a tuple with the SubscriptionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubscriptionId

`func (o *CloudCredential) SetSubscriptionId(v string)`

SetSubscriptionId sets SubscriptionId field to given value.

### HasSubscriptionId

`func (o *CloudCredential) HasSubscriptionId() bool`

HasSubscriptionId returns a boolean if a field has been set.

### GetResourceGroup

`func (o *CloudCredential) GetResourceGroup() string`

GetResourceGroup returns the ResourceGroup field if non-nil, zero value otherwise.

### GetResourceGroupOk

`func (o *CloudCredential) GetResourceGroupOk() (*string, bool)`

GetResourceGroupOk returns a tuple with the ResourceGroup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceGroup

`func (o *CloudCredential) SetResourceGroup(v string)`

SetResourceGroup sets ResourceGroup field to given value.

### HasResourceGroup

`func (o *CloudCredential) HasResourceGroup() bool`

HasResourceGroup returns a boolean if a field has been set.

### GetWorkspaceName

`func (o *CloudCredential) GetWorkspaceName() string`

GetWorkspaceName returns the WorkspaceName field if non-nil, zero value otherwise.

### GetWorkspaceNameOk

`func (o *CloudCredential) GetWorkspaceNameOk() (*string, bool)`

GetWorkspaceNameOk returns a tuple with the WorkspaceName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkspaceName

`func (o *CloudCredential) SetWorkspaceName(v string)`

SetWorkspaceName sets WorkspaceName field to given value.

### HasWorkspaceName

`func (o *CloudCredential) HasWorkspaceName() bool`

HasWorkspaceName returns a boolean if a field has been set.

### GetHuggingFaceToken

`func (o *CloudCredential) GetHuggingFaceToken() string`

GetHuggingFaceToken returns the HuggingFaceToken field if non-nil, zero value otherwise.

### GetHuggingFaceTokenOk

`func (o *CloudCredential) GetHuggingFaceTokenOk() (*string, bool)`

GetHuggingFaceTokenOk returns a tuple with the HuggingFaceToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHuggingFaceToken

`func (o *CloudCredential) SetHuggingFaceToken(v string)`

SetHuggingFaceToken sets HuggingFaceToken field to given value.

### HasHuggingFaceToken

`func (o *CloudCredential) HasHuggingFaceToken() bool`

HasHuggingFaceToken returns a boolean if a field has been set.

### GetCohereApiKey

`func (o *CloudCredential) GetCohereApiKey() string`

GetCohereApiKey returns the CohereApiKey field if non-nil, zero value otherwise.

### GetCohereApiKeyOk

`func (o *CloudCredential) GetCohereApiKeyOk() (*string, bool)`

GetCohereApiKeyOk returns a tuple with the CohereApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCohereApiKey

`func (o *CloudCredential) SetCohereApiKey(v string)`

SetCohereApiKey sets CohereApiKey field to given value.

### HasCohereApiKey

`func (o *CloudCredential) HasCohereApiKey() bool`

HasCohereApiKey returns a boolean if a field has been set.

### GetAzureAiStudioEndpoint

`func (o *CloudCredential) GetAzureAiStudioEndpoint() string`

GetAzureAiStudioEndpoint returns the AzureAiStudioEndpoint field if non-nil, zero value otherwise.

### GetAzureAiStudioEndpointOk

`func (o *CloudCredential) GetAzureAiStudioEndpointOk() (*string, bool)`

GetAzureAiStudioEndpointOk returns a tuple with the AzureAiStudioEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAzureAiStudioEndpoint

`func (o *CloudCredential) SetAzureAiStudioEndpoint(v string)`

SetAzureAiStudioEndpoint sets AzureAiStudioEndpoint field to given value.

### HasAzureAiStudioEndpoint

`func (o *CloudCredential) HasAzureAiStudioEndpoint() bool`

HasAzureAiStudioEndpoint returns a boolean if a field has been set.

### GetMosaicmlApiKey

`func (o *CloudCredential) GetMosaicmlApiKey() string`

GetMosaicmlApiKey returns the MosaicmlApiKey field if non-nil, zero value otherwise.

### GetMosaicmlApiKeyOk

`func (o *CloudCredential) GetMosaicmlApiKeyOk() (*string, bool)`

GetMosaicmlApiKeyOk returns a tuple with the MosaicmlApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMosaicmlApiKey

`func (o *CloudCredential) SetMosaicmlApiKey(v string)`

SetMosaicmlApiKey sets MosaicmlApiKey field to given value.

### HasMosaicmlApiKey

`func (o *CloudCredential) HasMosaicmlApiKey() bool`

HasMosaicmlApiKey returns a boolean if a field has been set.

### GetReplicateApiToken

`func (o *CloudCredential) GetReplicateApiToken() string`

GetReplicateApiToken returns the ReplicateApiToken field if non-nil, zero value otherwise.

### GetReplicateApiTokenOk

`func (o *CloudCredential) GetReplicateApiTokenOk() (*string, bool)`

GetReplicateApiTokenOk returns a tuple with the ReplicateApiToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReplicateApiToken

`func (o *CloudCredential) SetReplicateApiToken(v string)`

SetReplicateApiToken sets ReplicateApiToken field to given value.

### HasReplicateApiToken

`func (o *CloudCredential) HasReplicateApiToken() bool`

HasReplicateApiToken returns a boolean if a field has been set.

### GetTwitterBearerToken

`func (o *CloudCredential) GetTwitterBearerToken() string`

GetTwitterBearerToken returns the TwitterBearerToken field if non-nil, zero value otherwise.

### GetTwitterBearerTokenOk

`func (o *CloudCredential) GetTwitterBearerTokenOk() (*string, bool)`

GetTwitterBearerTokenOk returns a tuple with the TwitterBearerToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTwitterBearerToken

`func (o *CloudCredential) SetTwitterBearerToken(v string)`

SetTwitterBearerToken sets TwitterBearerToken field to given value.

### HasTwitterBearerToken

`func (o *CloudCredential) HasTwitterBearerToken() bool`

HasTwitterBearerToken returns a boolean if a field has been set.

### GetTwitterApiKey

`func (o *CloudCredential) GetTwitterApiKey() string`

GetTwitterApiKey returns the TwitterApiKey field if non-nil, zero value otherwise.

### GetTwitterApiKeyOk

`func (o *CloudCredential) GetTwitterApiKeyOk() (*string, bool)`

GetTwitterApiKeyOk returns a tuple with the TwitterApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTwitterApiKey

`func (o *CloudCredential) SetTwitterApiKey(v string)`

SetTwitterApiKey sets TwitterApiKey field to given value.

### HasTwitterApiKey

`func (o *CloudCredential) HasTwitterApiKey() bool`

HasTwitterApiKey returns a boolean if a field has been set.

### GetTwitterApiSecret

`func (o *CloudCredential) GetTwitterApiSecret() string`

GetTwitterApiSecret returns the TwitterApiSecret field if non-nil, zero value otherwise.

### GetTwitterApiSecretOk

`func (o *CloudCredential) GetTwitterApiSecretOk() (*string, bool)`

GetTwitterApiSecretOk returns a tuple with the TwitterApiSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTwitterApiSecret

`func (o *CloudCredential) SetTwitterApiSecret(v string)`

SetTwitterApiSecret sets TwitterApiSecret field to given value.

### HasTwitterApiSecret

`func (o *CloudCredential) HasTwitterApiSecret() bool`

HasTwitterApiSecret returns a boolean if a field has been set.

### GetRedditClientId

`func (o *CloudCredential) GetRedditClientId() string`

GetRedditClientId returns the RedditClientId field if non-nil, zero value otherwise.

### GetRedditClientIdOk

`func (o *CloudCredential) GetRedditClientIdOk() (*string, bool)`

GetRedditClientIdOk returns a tuple with the RedditClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedditClientId

`func (o *CloudCredential) SetRedditClientId(v string)`

SetRedditClientId sets RedditClientId field to given value.

### HasRedditClientId

`func (o *CloudCredential) HasRedditClientId() bool`

HasRedditClientId returns a boolean if a field has been set.

### GetRedditClientSecret

`func (o *CloudCredential) GetRedditClientSecret() string`

GetRedditClientSecret returns the RedditClientSecret field if non-nil, zero value otherwise.

### GetRedditClientSecretOk

`func (o *CloudCredential) GetRedditClientSecretOk() (*string, bool)`

GetRedditClientSecretOk returns a tuple with the RedditClientSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedditClientSecret

`func (o *CloudCredential) SetRedditClientSecret(v string)`

SetRedditClientSecret sets RedditClientSecret field to given value.

### HasRedditClientSecret

`func (o *CloudCredential) HasRedditClientSecret() bool`

HasRedditClientSecret returns a boolean if a field has been set.

### GetRedditUserAgent

`func (o *CloudCredential) GetRedditUserAgent() string`

GetRedditUserAgent returns the RedditUserAgent field if non-nil, zero value otherwise.

### GetRedditUserAgentOk

`func (o *CloudCredential) GetRedditUserAgentOk() (*string, bool)`

GetRedditUserAgentOk returns a tuple with the RedditUserAgent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedditUserAgent

`func (o *CloudCredential) SetRedditUserAgent(v string)`

SetRedditUserAgent sets RedditUserAgent field to given value.

### HasRedditUserAgent

`func (o *CloudCredential) HasRedditUserAgent() bool`

HasRedditUserAgent returns a boolean if a field has been set.

### GetFacebookAccessToken

`func (o *CloudCredential) GetFacebookAccessToken() string`

GetFacebookAccessToken returns the FacebookAccessToken field if non-nil, zero value otherwise.

### GetFacebookAccessTokenOk

`func (o *CloudCredential) GetFacebookAccessTokenOk() (*string, bool)`

GetFacebookAccessTokenOk returns a tuple with the FacebookAccessToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFacebookAccessToken

`func (o *CloudCredential) SetFacebookAccessToken(v string)`

SetFacebookAccessToken sets FacebookAccessToken field to given value.

### HasFacebookAccessToken

`func (o *CloudCredential) HasFacebookAccessToken() bool`

HasFacebookAccessToken returns a boolean if a field has been set.

### GetFacebookAppId

`func (o *CloudCredential) GetFacebookAppId() string`

GetFacebookAppId returns the FacebookAppId field if non-nil, zero value otherwise.

### GetFacebookAppIdOk

`func (o *CloudCredential) GetFacebookAppIdOk() (*string, bool)`

GetFacebookAppIdOk returns a tuple with the FacebookAppId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFacebookAppId

`func (o *CloudCredential) SetFacebookAppId(v string)`

SetFacebookAppId sets FacebookAppId field to given value.

### HasFacebookAppId

`func (o *CloudCredential) HasFacebookAppId() bool`

HasFacebookAppId returns a boolean if a field has been set.

### GetFacebookAppSecret

`func (o *CloudCredential) GetFacebookAppSecret() string`

GetFacebookAppSecret returns the FacebookAppSecret field if non-nil, zero value otherwise.

### GetFacebookAppSecretOk

`func (o *CloudCredential) GetFacebookAppSecretOk() (*string, bool)`

GetFacebookAppSecretOk returns a tuple with the FacebookAppSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFacebookAppSecret

`func (o *CloudCredential) SetFacebookAppSecret(v string)`

SetFacebookAppSecret sets FacebookAppSecret field to given value.

### HasFacebookAppSecret

`func (o *CloudCredential) HasFacebookAppSecret() bool`

HasFacebookAppSecret returns a boolean if a field has been set.

### GetInstagramAccessToken

`func (o *CloudCredential) GetInstagramAccessToken() string`

GetInstagramAccessToken returns the InstagramAccessToken field if non-nil, zero value otherwise.

### GetInstagramAccessTokenOk

`func (o *CloudCredential) GetInstagramAccessTokenOk() (*string, bool)`

GetInstagramAccessTokenOk returns a tuple with the InstagramAccessToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstagramAccessToken

`func (o *CloudCredential) SetInstagramAccessToken(v string)`

SetInstagramAccessToken sets InstagramAccessToken field to given value.

### HasInstagramAccessToken

`func (o *CloudCredential) HasInstagramAccessToken() bool`

HasInstagramAccessToken returns a boolean if a field has been set.

### GetLinkedinAccessToken

`func (o *CloudCredential) GetLinkedinAccessToken() string`

GetLinkedinAccessToken returns the LinkedinAccessToken field if non-nil, zero value otherwise.

### GetLinkedinAccessTokenOk

`func (o *CloudCredential) GetLinkedinAccessTokenOk() (*string, bool)`

GetLinkedinAccessTokenOk returns a tuple with the LinkedinAccessToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkedinAccessToken

`func (o *CloudCredential) SetLinkedinAccessToken(v string)`

SetLinkedinAccessToken sets LinkedinAccessToken field to given value.

### HasLinkedinAccessToken

`func (o *CloudCredential) HasLinkedinAccessToken() bool`

HasLinkedinAccessToken returns a boolean if a field has been set.

### GetLinkedinClientId

`func (o *CloudCredential) GetLinkedinClientId() string`

GetLinkedinClientId returns the LinkedinClientId field if non-nil, zero value otherwise.

### GetLinkedinClientIdOk

`func (o *CloudCredential) GetLinkedinClientIdOk() (*string, bool)`

GetLinkedinClientIdOk returns a tuple with the LinkedinClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkedinClientId

`func (o *CloudCredential) SetLinkedinClientId(v string)`

SetLinkedinClientId sets LinkedinClientId field to given value.

### HasLinkedinClientId

`func (o *CloudCredential) HasLinkedinClientId() bool`

HasLinkedinClientId returns a boolean if a field has been set.

### GetLinkedinClientSecret

`func (o *CloudCredential) GetLinkedinClientSecret() string`

GetLinkedinClientSecret returns the LinkedinClientSecret field if non-nil, zero value otherwise.

### GetLinkedinClientSecretOk

`func (o *CloudCredential) GetLinkedinClientSecretOk() (*string, bool)`

GetLinkedinClientSecretOk returns a tuple with the LinkedinClientSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkedinClientSecret

`func (o *CloudCredential) SetLinkedinClientSecret(v string)`

SetLinkedinClientSecret sets LinkedinClientSecret field to given value.

### HasLinkedinClientSecret

`func (o *CloudCredential) HasLinkedinClientSecret() bool`

HasLinkedinClientSecret returns a boolean if a field has been set.

### GetTiktokClientKey

`func (o *CloudCredential) GetTiktokClientKey() string`

GetTiktokClientKey returns the TiktokClientKey field if non-nil, zero value otherwise.

### GetTiktokClientKeyOk

`func (o *CloudCredential) GetTiktokClientKeyOk() (*string, bool)`

GetTiktokClientKeyOk returns a tuple with the TiktokClientKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTiktokClientKey

`func (o *CloudCredential) SetTiktokClientKey(v string)`

SetTiktokClientKey sets TiktokClientKey field to given value.

### HasTiktokClientKey

`func (o *CloudCredential) HasTiktokClientKey() bool`

HasTiktokClientKey returns a boolean if a field has been set.

### GetTiktokClientSecret

`func (o *CloudCredential) GetTiktokClientSecret() string`

GetTiktokClientSecret returns the TiktokClientSecret field if non-nil, zero value otherwise.

### GetTiktokClientSecretOk

`func (o *CloudCredential) GetTiktokClientSecretOk() (*string, bool)`

GetTiktokClientSecretOk returns a tuple with the TiktokClientSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTiktokClientSecret

`func (o *CloudCredential) SetTiktokClientSecret(v string)`

SetTiktokClientSecret sets TiktokClientSecret field to given value.

### HasTiktokClientSecret

`func (o *CloudCredential) HasTiktokClientSecret() bool`

HasTiktokClientSecret returns a boolean if a field has been set.

### GetYoutubeApiKey

`func (o *CloudCredential) GetYoutubeApiKey() string`

GetYoutubeApiKey returns the YoutubeApiKey field if non-nil, zero value otherwise.

### GetYoutubeApiKeyOk

`func (o *CloudCredential) GetYoutubeApiKeyOk() (*string, bool)`

GetYoutubeApiKeyOk returns a tuple with the YoutubeApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetYoutubeApiKey

`func (o *CloudCredential) SetYoutubeApiKey(v string)`

SetYoutubeApiKey sets YoutubeApiKey field to given value.

### HasYoutubeApiKey

`func (o *CloudCredential) HasYoutubeApiKey() bool`

HasYoutubeApiKey returns a boolean if a field has been set.

### GetDatabricksWorkspaceUrl

`func (o *CloudCredential) GetDatabricksWorkspaceUrl() string`

GetDatabricksWorkspaceUrl returns the DatabricksWorkspaceUrl field if non-nil, zero value otherwise.

### GetDatabricksWorkspaceUrlOk

`func (o *CloudCredential) GetDatabricksWorkspaceUrlOk() (*string, bool)`

GetDatabricksWorkspaceUrlOk returns a tuple with the DatabricksWorkspaceUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatabricksWorkspaceUrl

`func (o *CloudCredential) SetDatabricksWorkspaceUrl(v string)`

SetDatabricksWorkspaceUrl sets DatabricksWorkspaceUrl field to given value.

### HasDatabricksWorkspaceUrl

`func (o *CloudCredential) HasDatabricksWorkspaceUrl() bool`

HasDatabricksWorkspaceUrl returns a boolean if a field has been set.

### GetDatabricksAccessToken

`func (o *CloudCredential) GetDatabricksAccessToken() string`

GetDatabricksAccessToken returns the DatabricksAccessToken field if non-nil, zero value otherwise.

### GetDatabricksAccessTokenOk

`func (o *CloudCredential) GetDatabricksAccessTokenOk() (*string, bool)`

GetDatabricksAccessTokenOk returns a tuple with the DatabricksAccessToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatabricksAccessToken

`func (o *CloudCredential) SetDatabricksAccessToken(v string)`

SetDatabricksAccessToken sets DatabricksAccessToken field to given value.

### HasDatabricksAccessToken

`func (o *CloudCredential) HasDatabricksAccessToken() bool`

HasDatabricksAccessToken returns a boolean if a field has been set.

### GetDatabricksClusterId

`func (o *CloudCredential) GetDatabricksClusterId() string`

GetDatabricksClusterId returns the DatabricksClusterId field if non-nil, zero value otherwise.

### GetDatabricksClusterIdOk

`func (o *CloudCredential) GetDatabricksClusterIdOk() (*string, bool)`

GetDatabricksClusterIdOk returns a tuple with the DatabricksClusterId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatabricksClusterId

`func (o *CloudCredential) SetDatabricksClusterId(v string)`

SetDatabricksClusterId sets DatabricksClusterId field to given value.

### HasDatabricksClusterId

`func (o *CloudCredential) HasDatabricksClusterId() bool`

HasDatabricksClusterId returns a boolean if a field has been set.

### GetOauthAccessToken

`func (o *CloudCredential) GetOauthAccessToken() string`

GetOauthAccessToken returns the OauthAccessToken field if non-nil, zero value otherwise.

### GetOauthAccessTokenOk

`func (o *CloudCredential) GetOauthAccessTokenOk() (*string, bool)`

GetOauthAccessTokenOk returns a tuple with the OauthAccessToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOauthAccessToken

`func (o *CloudCredential) SetOauthAccessToken(v string)`

SetOauthAccessToken sets OauthAccessToken field to given value.

### HasOauthAccessToken

`func (o *CloudCredential) HasOauthAccessToken() bool`

HasOauthAccessToken returns a boolean if a field has been set.

### GetOauthRefreshToken

`func (o *CloudCredential) GetOauthRefreshToken() string`

GetOauthRefreshToken returns the OauthRefreshToken field if non-nil, zero value otherwise.

### GetOauthRefreshTokenOk

`func (o *CloudCredential) GetOauthRefreshTokenOk() (*string, bool)`

GetOauthRefreshTokenOk returns a tuple with the OauthRefreshToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOauthRefreshToken

`func (o *CloudCredential) SetOauthRefreshToken(v string)`

SetOauthRefreshToken sets OauthRefreshToken field to given value.

### HasOauthRefreshToken

`func (o *CloudCredential) HasOauthRefreshToken() bool`

HasOauthRefreshToken returns a boolean if a field has been set.

### GetOauthTokenExpiresAt

`func (o *CloudCredential) GetOauthTokenExpiresAt() time.Time`

GetOauthTokenExpiresAt returns the OauthTokenExpiresAt field if non-nil, zero value otherwise.

### GetOauthTokenExpiresAtOk

`func (o *CloudCredential) GetOauthTokenExpiresAtOk() (*time.Time, bool)`

GetOauthTokenExpiresAtOk returns a tuple with the OauthTokenExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOauthTokenExpiresAt

`func (o *CloudCredential) SetOauthTokenExpiresAt(v time.Time)`

SetOauthTokenExpiresAt sets OauthTokenExpiresAt field to given value.

### HasOauthTokenExpiresAt

`func (o *CloudCredential) HasOauthTokenExpiresAt() bool`

HasOauthTokenExpiresAt returns a boolean if a field has been set.

### GetOauthTokenType

`func (o *CloudCredential) GetOauthTokenType() string`

GetOauthTokenType returns the OauthTokenType field if non-nil, zero value otherwise.

### GetOauthTokenTypeOk

`func (o *CloudCredential) GetOauthTokenTypeOk() (*string, bool)`

GetOauthTokenTypeOk returns a tuple with the OauthTokenType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOauthTokenType

`func (o *CloudCredential) SetOauthTokenType(v string)`

SetOauthTokenType sets OauthTokenType field to given value.

### HasOauthTokenType

`func (o *CloudCredential) HasOauthTokenType() bool`

HasOauthTokenType returns a boolean if a field has been set.

### GetAlphavantageApiKey

`func (o *CloudCredential) GetAlphavantageApiKey() string`

GetAlphavantageApiKey returns the AlphavantageApiKey field if non-nil, zero value otherwise.

### GetAlphavantageApiKeyOk

`func (o *CloudCredential) GetAlphavantageApiKeyOk() (*string, bool)`

GetAlphavantageApiKeyOk returns a tuple with the AlphavantageApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlphavantageApiKey

`func (o *CloudCredential) SetAlphavantageApiKey(v string)`

SetAlphavantageApiKey sets AlphavantageApiKey field to given value.

### HasAlphavantageApiKey

`func (o *CloudCredential) HasAlphavantageApiKey() bool`

HasAlphavantageApiKey returns a boolean if a field has been set.

### GetPolygonApiKey

`func (o *CloudCredential) GetPolygonApiKey() string`

GetPolygonApiKey returns the PolygonApiKey field if non-nil, zero value otherwise.

### GetPolygonApiKeyOk

`func (o *CloudCredential) GetPolygonApiKeyOk() (*string, bool)`

GetPolygonApiKeyOk returns a tuple with the PolygonApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPolygonApiKey

`func (o *CloudCredential) SetPolygonApiKey(v string)`

SetPolygonApiKey sets PolygonApiKey field to given value.

### HasPolygonApiKey

`func (o *CloudCredential) HasPolygonApiKey() bool`

HasPolygonApiKey returns a boolean if a field has been set.

### GetTwelvedataApiKey

`func (o *CloudCredential) GetTwelvedataApiKey() string`

GetTwelvedataApiKey returns the TwelvedataApiKey field if non-nil, zero value otherwise.

### GetTwelvedataApiKeyOk

`func (o *CloudCredential) GetTwelvedataApiKeyOk() (*string, bool)`

GetTwelvedataApiKeyOk returns a tuple with the TwelvedataApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTwelvedataApiKey

`func (o *CloudCredential) SetTwelvedataApiKey(v string)`

SetTwelvedataApiKey sets TwelvedataApiKey field to given value.

### HasTwelvedataApiKey

`func (o *CloudCredential) HasTwelvedataApiKey() bool`

HasTwelvedataApiKey returns a boolean if a field has been set.

### GetMarketstackAccessKey

`func (o *CloudCredential) GetMarketstackAccessKey() string`

GetMarketstackAccessKey returns the MarketstackAccessKey field if non-nil, zero value otherwise.

### GetMarketstackAccessKeyOk

`func (o *CloudCredential) GetMarketstackAccessKeyOk() (*string, bool)`

GetMarketstackAccessKeyOk returns a tuple with the MarketstackAccessKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMarketstackAccessKey

`func (o *CloudCredential) SetMarketstackAccessKey(v string)`

SetMarketstackAccessKey sets MarketstackAccessKey field to given value.

### HasMarketstackAccessKey

`func (o *CloudCredential) HasMarketstackAccessKey() bool`

HasMarketstackAccessKey returns a boolean if a field has been set.

### GetFmpApiKey

`func (o *CloudCredential) GetFmpApiKey() string`

GetFmpApiKey returns the FmpApiKey field if non-nil, zero value otherwise.

### GetFmpApiKeyOk

`func (o *CloudCredential) GetFmpApiKeyOk() (*string, bool)`

GetFmpApiKeyOk returns a tuple with the FmpApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFmpApiKey

`func (o *CloudCredential) SetFmpApiKey(v string)`

SetFmpApiKey sets FmpApiKey field to given value.

### HasFmpApiKey

`func (o *CloudCredential) HasFmpApiKey() bool`

HasFmpApiKey returns a boolean if a field has been set.

### GetIexcloudToken

`func (o *CloudCredential) GetIexcloudToken() string`

GetIexcloudToken returns the IexcloudToken field if non-nil, zero value otherwise.

### GetIexcloudTokenOk

`func (o *CloudCredential) GetIexcloudTokenOk() (*string, bool)`

GetIexcloudTokenOk returns a tuple with the IexcloudToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIexcloudToken

`func (o *CloudCredential) SetIexcloudToken(v string)`

SetIexcloudToken sets IexcloudToken field to given value.

### HasIexcloudToken

`func (o *CloudCredential) HasIexcloudToken() bool`

HasIexcloudToken returns a boolean if a field has been set.

### GetCbondApiKey

`func (o *CloudCredential) GetCbondApiKey() string`

GetCbondApiKey returns the CbondApiKey field if non-nil, zero value otherwise.

### GetCbondApiKeyOk

`func (o *CloudCredential) GetCbondApiKeyOk() (*string, bool)`

GetCbondApiKeyOk returns a tuple with the CbondApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCbondApiKey

`func (o *CloudCredential) SetCbondApiKey(v string)`

SetCbondApiKey sets CbondApiKey field to given value.

### HasCbondApiKey

`func (o *CloudCredential) HasCbondApiKey() bool`

HasCbondApiKey returns a boolean if a field has been set.

### GetCbondClientId

`func (o *CloudCredential) GetCbondClientId() string`

GetCbondClientId returns the CbondClientId field if non-nil, zero value otherwise.

### GetCbondClientIdOk

`func (o *CloudCredential) GetCbondClientIdOk() (*string, bool)`

GetCbondClientIdOk returns a tuple with the CbondClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCbondClientId

`func (o *CloudCredential) SetCbondClientId(v string)`

SetCbondClientId sets CbondClientId field to given value.

### HasCbondClientId

`func (o *CloudCredential) HasCbondClientId() bool`

HasCbondClientId returns a boolean if a field has been set.

### GetCbondClientSecret

`func (o *CloudCredential) GetCbondClientSecret() string`

GetCbondClientSecret returns the CbondClientSecret field if non-nil, zero value otherwise.

### GetCbondClientSecretOk

`func (o *CloudCredential) GetCbondClientSecretOk() (*string, bool)`

GetCbondClientSecretOk returns a tuple with the CbondClientSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCbondClientSecret

`func (o *CloudCredential) SetCbondClientSecret(v string)`

SetCbondClientSecret sets CbondClientSecret field to given value.

### HasCbondClientSecret

`func (o *CloudCredential) HasCbondClientSecret() bool`

HasCbondClientSecret returns a boolean if a field has been set.

### GetGoogleSearchEngineId

`func (o *CloudCredential) GetGoogleSearchEngineId() string`

GetGoogleSearchEngineId returns the GoogleSearchEngineId field if non-nil, zero value otherwise.

### GetGoogleSearchEngineIdOk

`func (o *CloudCredential) GetGoogleSearchEngineIdOk() (*string, bool)`

GetGoogleSearchEngineIdOk returns a tuple with the GoogleSearchEngineId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoogleSearchEngineId

`func (o *CloudCredential) SetGoogleSearchEngineId(v string)`

SetGoogleSearchEngineId sets GoogleSearchEngineId field to given value.

### HasGoogleSearchEngineId

`func (o *CloudCredential) HasGoogleSearchEngineId() bool`

HasGoogleSearchEngineId returns a boolean if a field has been set.

### GetBingSearchApiKey

`func (o *CloudCredential) GetBingSearchApiKey() string`

GetBingSearchApiKey returns the BingSearchApiKey field if non-nil, zero value otherwise.

### GetBingSearchApiKeyOk

`func (o *CloudCredential) GetBingSearchApiKeyOk() (*string, bool)`

GetBingSearchApiKeyOk returns a tuple with the BingSearchApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBingSearchApiKey

`func (o *CloudCredential) SetBingSearchApiKey(v string)`

SetBingSearchApiKey sets BingSearchApiKey field to given value.

### HasBingSearchApiKey

`func (o *CloudCredential) HasBingSearchApiKey() bool`

HasBingSearchApiKey returns a boolean if a field has been set.

### GetEnabled

`func (o *CloudCredential) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *CloudCredential) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *CloudCredential) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *CloudCredential) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


