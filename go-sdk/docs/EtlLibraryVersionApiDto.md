# EtlLibraryVersionApiDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int64** |  | [optional] 
**BuildType** | Pointer to **string** |  | [optional] 
**BuildNumber** | Pointer to **int32** |  | [optional] 
**Version** | Pointer to **string** |  | [optional] 
**JarPath** | Pointer to **string** |  | [optional] 
**JarPathObfuscated** | Pointer to **string** |  | [optional] 
**JarSizeBytes** | Pointer to **int64** |  | [optional] 
**UploadedAt** | Pointer to **time.Time** |  | [optional] 
**Active** | Pointer to **bool** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**ImageTag** | Pointer to **string** |  | [optional] 

## Methods

### NewEtlLibraryVersionApiDto

`func NewEtlLibraryVersionApiDto() *EtlLibraryVersionApiDto`

NewEtlLibraryVersionApiDto instantiates a new EtlLibraryVersionApiDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEtlLibraryVersionApiDtoWithDefaults

`func NewEtlLibraryVersionApiDtoWithDefaults() *EtlLibraryVersionApiDto`

NewEtlLibraryVersionApiDtoWithDefaults instantiates a new EtlLibraryVersionApiDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *EtlLibraryVersionApiDto) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *EtlLibraryVersionApiDto) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *EtlLibraryVersionApiDto) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *EtlLibraryVersionApiDto) HasId() bool`

HasId returns a boolean if a field has been set.

### GetBuildType

`func (o *EtlLibraryVersionApiDto) GetBuildType() string`

GetBuildType returns the BuildType field if non-nil, zero value otherwise.

### GetBuildTypeOk

`func (o *EtlLibraryVersionApiDto) GetBuildTypeOk() (*string, bool)`

GetBuildTypeOk returns a tuple with the BuildType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuildType

`func (o *EtlLibraryVersionApiDto) SetBuildType(v string)`

SetBuildType sets BuildType field to given value.

### HasBuildType

`func (o *EtlLibraryVersionApiDto) HasBuildType() bool`

HasBuildType returns a boolean if a field has been set.

### GetBuildNumber

`func (o *EtlLibraryVersionApiDto) GetBuildNumber() int32`

GetBuildNumber returns the BuildNumber field if non-nil, zero value otherwise.

### GetBuildNumberOk

`func (o *EtlLibraryVersionApiDto) GetBuildNumberOk() (*int32, bool)`

GetBuildNumberOk returns a tuple with the BuildNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuildNumber

`func (o *EtlLibraryVersionApiDto) SetBuildNumber(v int32)`

SetBuildNumber sets BuildNumber field to given value.

### HasBuildNumber

`func (o *EtlLibraryVersionApiDto) HasBuildNumber() bool`

HasBuildNumber returns a boolean if a field has been set.

### GetVersion

`func (o *EtlLibraryVersionApiDto) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *EtlLibraryVersionApiDto) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *EtlLibraryVersionApiDto) SetVersion(v string)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *EtlLibraryVersionApiDto) HasVersion() bool`

HasVersion returns a boolean if a field has been set.

### GetJarPath

`func (o *EtlLibraryVersionApiDto) GetJarPath() string`

GetJarPath returns the JarPath field if non-nil, zero value otherwise.

### GetJarPathOk

`func (o *EtlLibraryVersionApiDto) GetJarPathOk() (*string, bool)`

GetJarPathOk returns a tuple with the JarPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJarPath

`func (o *EtlLibraryVersionApiDto) SetJarPath(v string)`

SetJarPath sets JarPath field to given value.

### HasJarPath

`func (o *EtlLibraryVersionApiDto) HasJarPath() bool`

HasJarPath returns a boolean if a field has been set.

### GetJarPathObfuscated

`func (o *EtlLibraryVersionApiDto) GetJarPathObfuscated() string`

GetJarPathObfuscated returns the JarPathObfuscated field if non-nil, zero value otherwise.

### GetJarPathObfuscatedOk

`func (o *EtlLibraryVersionApiDto) GetJarPathObfuscatedOk() (*string, bool)`

GetJarPathObfuscatedOk returns a tuple with the JarPathObfuscated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJarPathObfuscated

`func (o *EtlLibraryVersionApiDto) SetJarPathObfuscated(v string)`

SetJarPathObfuscated sets JarPathObfuscated field to given value.

### HasJarPathObfuscated

`func (o *EtlLibraryVersionApiDto) HasJarPathObfuscated() bool`

HasJarPathObfuscated returns a boolean if a field has been set.

### GetJarSizeBytes

`func (o *EtlLibraryVersionApiDto) GetJarSizeBytes() int64`

GetJarSizeBytes returns the JarSizeBytes field if non-nil, zero value otherwise.

### GetJarSizeBytesOk

`func (o *EtlLibraryVersionApiDto) GetJarSizeBytesOk() (*int64, bool)`

GetJarSizeBytesOk returns a tuple with the JarSizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJarSizeBytes

`func (o *EtlLibraryVersionApiDto) SetJarSizeBytes(v int64)`

SetJarSizeBytes sets JarSizeBytes field to given value.

### HasJarSizeBytes

`func (o *EtlLibraryVersionApiDto) HasJarSizeBytes() bool`

HasJarSizeBytes returns a boolean if a field has been set.

### GetUploadedAt

`func (o *EtlLibraryVersionApiDto) GetUploadedAt() time.Time`

GetUploadedAt returns the UploadedAt field if non-nil, zero value otherwise.

### GetUploadedAtOk

`func (o *EtlLibraryVersionApiDto) GetUploadedAtOk() (*time.Time, bool)`

GetUploadedAtOk returns a tuple with the UploadedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUploadedAt

`func (o *EtlLibraryVersionApiDto) SetUploadedAt(v time.Time)`

SetUploadedAt sets UploadedAt field to given value.

### HasUploadedAt

`func (o *EtlLibraryVersionApiDto) HasUploadedAt() bool`

HasUploadedAt returns a boolean if a field has been set.

### GetActive

`func (o *EtlLibraryVersionApiDto) GetActive() bool`

GetActive returns the Active field if non-nil, zero value otherwise.

### GetActiveOk

`func (o *EtlLibraryVersionApiDto) GetActiveOk() (*bool, bool)`

GetActiveOk returns a tuple with the Active field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActive

`func (o *EtlLibraryVersionApiDto) SetActive(v bool)`

SetActive sets Active field to given value.

### HasActive

`func (o *EtlLibraryVersionApiDto) HasActive() bool`

HasActive returns a boolean if a field has been set.

### GetDescription

`func (o *EtlLibraryVersionApiDto) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *EtlLibraryVersionApiDto) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *EtlLibraryVersionApiDto) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *EtlLibraryVersionApiDto) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetImageTag

`func (o *EtlLibraryVersionApiDto) GetImageTag() string`

GetImageTag returns the ImageTag field if non-nil, zero value otherwise.

### GetImageTagOk

`func (o *EtlLibraryVersionApiDto) GetImageTagOk() (*string, bool)`

GetImageTagOk returns a tuple with the ImageTag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageTag

`func (o *EtlLibraryVersionApiDto) SetImageTag(v string)`

SetImageTag sets ImageTag field to given value.

### HasImageTag

`func (o *EtlLibraryVersionApiDto) HasImageTag() bool`

HasImageTag returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


