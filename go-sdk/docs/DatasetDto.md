# DatasetDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**UserId** | Pointer to **string** |  | [optional] 
**SourceUrl** | Pointer to **string** |  | [optional] 
**SourceType** | Pointer to **string** |  | [optional] 
**FilePath** | Pointer to **string** |  | [optional] 
**FileFormat** | Pointer to **string** |  | [optional] 
**FileSize** | Pointer to **int64** |  | [optional] 
**Schema** | Pointer to **string** |  | [optional] 
**Metadata** | Pointer to **string** |  | [optional] 
**Enabled** | Pointer to **bool** |  | [optional] 
**FieldIds** | Pointer to **[]string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**StoragePath** | Pointer to **string** |  | [optional] 
**Format** | Pointer to **string** |  | [optional] 
**DatasetType** | Pointer to **string** |  | [optional] 
**TrinoSchema** | Pointer to **string** |  | [optional] 
**StorageType** | Pointer to **string** |  | [optional] 
**CloudCredentialId** | Pointer to **int32** |  | [optional] 

## Methods

### NewDatasetDto

`func NewDatasetDto() *DatasetDto`

NewDatasetDto instantiates a new DatasetDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDatasetDtoWithDefaults

`func NewDatasetDtoWithDefaults() *DatasetDto`

NewDatasetDtoWithDefaults instantiates a new DatasetDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *DatasetDto) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DatasetDto) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DatasetDto) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *DatasetDto) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *DatasetDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *DatasetDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *DatasetDto) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *DatasetDto) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *DatasetDto) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *DatasetDto) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *DatasetDto) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *DatasetDto) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetUserId

`func (o *DatasetDto) GetUserId() string`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *DatasetDto) GetUserIdOk() (*string, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *DatasetDto) SetUserId(v string)`

SetUserId sets UserId field to given value.

### HasUserId

`func (o *DatasetDto) HasUserId() bool`

HasUserId returns a boolean if a field has been set.

### GetSourceUrl

`func (o *DatasetDto) GetSourceUrl() string`

GetSourceUrl returns the SourceUrl field if non-nil, zero value otherwise.

### GetSourceUrlOk

`func (o *DatasetDto) GetSourceUrlOk() (*string, bool)`

GetSourceUrlOk returns a tuple with the SourceUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceUrl

`func (o *DatasetDto) SetSourceUrl(v string)`

SetSourceUrl sets SourceUrl field to given value.

### HasSourceUrl

`func (o *DatasetDto) HasSourceUrl() bool`

HasSourceUrl returns a boolean if a field has been set.

### GetSourceType

`func (o *DatasetDto) GetSourceType() string`

GetSourceType returns the SourceType field if non-nil, zero value otherwise.

### GetSourceTypeOk

`func (o *DatasetDto) GetSourceTypeOk() (*string, bool)`

GetSourceTypeOk returns a tuple with the SourceType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceType

`func (o *DatasetDto) SetSourceType(v string)`

SetSourceType sets SourceType field to given value.

### HasSourceType

`func (o *DatasetDto) HasSourceType() bool`

HasSourceType returns a boolean if a field has been set.

### GetFilePath

`func (o *DatasetDto) GetFilePath() string`

GetFilePath returns the FilePath field if non-nil, zero value otherwise.

### GetFilePathOk

`func (o *DatasetDto) GetFilePathOk() (*string, bool)`

GetFilePathOk returns a tuple with the FilePath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFilePath

`func (o *DatasetDto) SetFilePath(v string)`

SetFilePath sets FilePath field to given value.

### HasFilePath

`func (o *DatasetDto) HasFilePath() bool`

HasFilePath returns a boolean if a field has been set.

### GetFileFormat

`func (o *DatasetDto) GetFileFormat() string`

GetFileFormat returns the FileFormat field if non-nil, zero value otherwise.

### GetFileFormatOk

`func (o *DatasetDto) GetFileFormatOk() (*string, bool)`

GetFileFormatOk returns a tuple with the FileFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFileFormat

`func (o *DatasetDto) SetFileFormat(v string)`

SetFileFormat sets FileFormat field to given value.

### HasFileFormat

`func (o *DatasetDto) HasFileFormat() bool`

HasFileFormat returns a boolean if a field has been set.

### GetFileSize

`func (o *DatasetDto) GetFileSize() int64`

GetFileSize returns the FileSize field if non-nil, zero value otherwise.

### GetFileSizeOk

`func (o *DatasetDto) GetFileSizeOk() (*int64, bool)`

GetFileSizeOk returns a tuple with the FileSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFileSize

`func (o *DatasetDto) SetFileSize(v int64)`

SetFileSize sets FileSize field to given value.

### HasFileSize

`func (o *DatasetDto) HasFileSize() bool`

HasFileSize returns a boolean if a field has been set.

### GetSchema

`func (o *DatasetDto) GetSchema() string`

GetSchema returns the Schema field if non-nil, zero value otherwise.

### GetSchemaOk

`func (o *DatasetDto) GetSchemaOk() (*string, bool)`

GetSchemaOk returns a tuple with the Schema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSchema

`func (o *DatasetDto) SetSchema(v string)`

SetSchema sets Schema field to given value.

### HasSchema

`func (o *DatasetDto) HasSchema() bool`

HasSchema returns a boolean if a field has been set.

### GetMetadata

`func (o *DatasetDto) GetMetadata() string`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *DatasetDto) GetMetadataOk() (*string, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *DatasetDto) SetMetadata(v string)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *DatasetDto) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetEnabled

`func (o *DatasetDto) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *DatasetDto) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *DatasetDto) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *DatasetDto) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetFieldIds

`func (o *DatasetDto) GetFieldIds() []string`

GetFieldIds returns the FieldIds field if non-nil, zero value otherwise.

### GetFieldIdsOk

`func (o *DatasetDto) GetFieldIdsOk() (*[]string, bool)`

GetFieldIdsOk returns a tuple with the FieldIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFieldIds

`func (o *DatasetDto) SetFieldIds(v []string)`

SetFieldIds sets FieldIds field to given value.

### HasFieldIds

`func (o *DatasetDto) HasFieldIds() bool`

HasFieldIds returns a boolean if a field has been set.

### GetCreatedAt

`func (o *DatasetDto) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *DatasetDto) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *DatasetDto) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *DatasetDto) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *DatasetDto) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *DatasetDto) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *DatasetDto) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *DatasetDto) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetStoragePath

`func (o *DatasetDto) GetStoragePath() string`

GetStoragePath returns the StoragePath field if non-nil, zero value otherwise.

### GetStoragePathOk

`func (o *DatasetDto) GetStoragePathOk() (*string, bool)`

GetStoragePathOk returns a tuple with the StoragePath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStoragePath

`func (o *DatasetDto) SetStoragePath(v string)`

SetStoragePath sets StoragePath field to given value.

### HasStoragePath

`func (o *DatasetDto) HasStoragePath() bool`

HasStoragePath returns a boolean if a field has been set.

### GetFormat

`func (o *DatasetDto) GetFormat() string`

GetFormat returns the Format field if non-nil, zero value otherwise.

### GetFormatOk

`func (o *DatasetDto) GetFormatOk() (*string, bool)`

GetFormatOk returns a tuple with the Format field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormat

`func (o *DatasetDto) SetFormat(v string)`

SetFormat sets Format field to given value.

### HasFormat

`func (o *DatasetDto) HasFormat() bool`

HasFormat returns a boolean if a field has been set.

### GetDatasetType

`func (o *DatasetDto) GetDatasetType() string`

GetDatasetType returns the DatasetType field if non-nil, zero value otherwise.

### GetDatasetTypeOk

`func (o *DatasetDto) GetDatasetTypeOk() (*string, bool)`

GetDatasetTypeOk returns a tuple with the DatasetType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatasetType

`func (o *DatasetDto) SetDatasetType(v string)`

SetDatasetType sets DatasetType field to given value.

### HasDatasetType

`func (o *DatasetDto) HasDatasetType() bool`

HasDatasetType returns a boolean if a field has been set.

### GetTrinoSchema

`func (o *DatasetDto) GetTrinoSchema() string`

GetTrinoSchema returns the TrinoSchema field if non-nil, zero value otherwise.

### GetTrinoSchemaOk

`func (o *DatasetDto) GetTrinoSchemaOk() (*string, bool)`

GetTrinoSchemaOk returns a tuple with the TrinoSchema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrinoSchema

`func (o *DatasetDto) SetTrinoSchema(v string)`

SetTrinoSchema sets TrinoSchema field to given value.

### HasTrinoSchema

`func (o *DatasetDto) HasTrinoSchema() bool`

HasTrinoSchema returns a boolean if a field has been set.

### GetStorageType

`func (o *DatasetDto) GetStorageType() string`

GetStorageType returns the StorageType field if non-nil, zero value otherwise.

### GetStorageTypeOk

`func (o *DatasetDto) GetStorageTypeOk() (*string, bool)`

GetStorageTypeOk returns a tuple with the StorageType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStorageType

`func (o *DatasetDto) SetStorageType(v string)`

SetStorageType sets StorageType field to given value.

### HasStorageType

`func (o *DatasetDto) HasStorageType() bool`

HasStorageType returns a boolean if a field has been set.

### GetCloudCredentialId

`func (o *DatasetDto) GetCloudCredentialId() int32`

GetCloudCredentialId returns the CloudCredentialId field if non-nil, zero value otherwise.

### GetCloudCredentialIdOk

`func (o *DatasetDto) GetCloudCredentialIdOk() (*int32, bool)`

GetCloudCredentialIdOk returns a tuple with the CloudCredentialId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCloudCredentialId

`func (o *DatasetDto) SetCloudCredentialId(v int32)`

SetCloudCredentialId sets CloudCredentialId field to given value.

### HasCloudCredentialId

`func (o *DatasetDto) HasCloudCredentialId() bool`

HasCloudCredentialId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


