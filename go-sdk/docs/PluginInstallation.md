# PluginInstallation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int64** |  | [optional] 
**PluginId** | Pointer to **string** |  | [optional] 
**PluginType** | Pointer to **string** |  | [optional] 
**BuildType** | Pointer to **string** |  | [optional] 
**BuildNumber** | Pointer to **int32** |  | [optional] 
**Version** | Pointer to **string** |  | [optional] 
**JarPath** | Pointer to **string** |  | [optional] 
**ManifestPath** | Pointer to **string** |  | [optional] 
**UiZipPath** | Pointer to **string** |  | [optional] 
**Enabled** | Pointer to **bool** |  | [optional] 
**OrganizationId** | Pointer to **string** |  | [optional] 
**OrganizationIdsJson** | Pointer to **string** |  | [optional] 
**MainClass** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**InstalledAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**EnabledAt** | Pointer to **time.Time** |  | [optional] 
**EnabledBy** | Pointer to **string** |  | [optional] 
**InstalledBy** | Pointer to **string** |  | [optional] 

## Methods

### NewPluginInstallation

`func NewPluginInstallation() *PluginInstallation`

NewPluginInstallation instantiates a new PluginInstallation object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPluginInstallationWithDefaults

`func NewPluginInstallationWithDefaults() *PluginInstallation`

NewPluginInstallationWithDefaults instantiates a new PluginInstallation object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *PluginInstallation) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PluginInstallation) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PluginInstallation) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *PluginInstallation) HasId() bool`

HasId returns a boolean if a field has been set.

### GetPluginId

`func (o *PluginInstallation) GetPluginId() string`

GetPluginId returns the PluginId field if non-nil, zero value otherwise.

### GetPluginIdOk

`func (o *PluginInstallation) GetPluginIdOk() (*string, bool)`

GetPluginIdOk returns a tuple with the PluginId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPluginId

`func (o *PluginInstallation) SetPluginId(v string)`

SetPluginId sets PluginId field to given value.

### HasPluginId

`func (o *PluginInstallation) HasPluginId() bool`

HasPluginId returns a boolean if a field has been set.

### GetPluginType

`func (o *PluginInstallation) GetPluginType() string`

GetPluginType returns the PluginType field if non-nil, zero value otherwise.

### GetPluginTypeOk

`func (o *PluginInstallation) GetPluginTypeOk() (*string, bool)`

GetPluginTypeOk returns a tuple with the PluginType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPluginType

`func (o *PluginInstallation) SetPluginType(v string)`

SetPluginType sets PluginType field to given value.

### HasPluginType

`func (o *PluginInstallation) HasPluginType() bool`

HasPluginType returns a boolean if a field has been set.

### GetBuildType

`func (o *PluginInstallation) GetBuildType() string`

GetBuildType returns the BuildType field if non-nil, zero value otherwise.

### GetBuildTypeOk

`func (o *PluginInstallation) GetBuildTypeOk() (*string, bool)`

GetBuildTypeOk returns a tuple with the BuildType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuildType

`func (o *PluginInstallation) SetBuildType(v string)`

SetBuildType sets BuildType field to given value.

### HasBuildType

`func (o *PluginInstallation) HasBuildType() bool`

HasBuildType returns a boolean if a field has been set.

### GetBuildNumber

`func (o *PluginInstallation) GetBuildNumber() int32`

GetBuildNumber returns the BuildNumber field if non-nil, zero value otherwise.

### GetBuildNumberOk

`func (o *PluginInstallation) GetBuildNumberOk() (*int32, bool)`

GetBuildNumberOk returns a tuple with the BuildNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuildNumber

`func (o *PluginInstallation) SetBuildNumber(v int32)`

SetBuildNumber sets BuildNumber field to given value.

### HasBuildNumber

`func (o *PluginInstallation) HasBuildNumber() bool`

HasBuildNumber returns a boolean if a field has been set.

### GetVersion

`func (o *PluginInstallation) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *PluginInstallation) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *PluginInstallation) SetVersion(v string)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *PluginInstallation) HasVersion() bool`

HasVersion returns a boolean if a field has been set.

### GetJarPath

`func (o *PluginInstallation) GetJarPath() string`

GetJarPath returns the JarPath field if non-nil, zero value otherwise.

### GetJarPathOk

`func (o *PluginInstallation) GetJarPathOk() (*string, bool)`

GetJarPathOk returns a tuple with the JarPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJarPath

`func (o *PluginInstallation) SetJarPath(v string)`

SetJarPath sets JarPath field to given value.

### HasJarPath

`func (o *PluginInstallation) HasJarPath() bool`

HasJarPath returns a boolean if a field has been set.

### GetManifestPath

`func (o *PluginInstallation) GetManifestPath() string`

GetManifestPath returns the ManifestPath field if non-nil, zero value otherwise.

### GetManifestPathOk

`func (o *PluginInstallation) GetManifestPathOk() (*string, bool)`

GetManifestPathOk returns a tuple with the ManifestPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManifestPath

`func (o *PluginInstallation) SetManifestPath(v string)`

SetManifestPath sets ManifestPath field to given value.

### HasManifestPath

`func (o *PluginInstallation) HasManifestPath() bool`

HasManifestPath returns a boolean if a field has been set.

### GetUiZipPath

`func (o *PluginInstallation) GetUiZipPath() string`

GetUiZipPath returns the UiZipPath field if non-nil, zero value otherwise.

### GetUiZipPathOk

`func (o *PluginInstallation) GetUiZipPathOk() (*string, bool)`

GetUiZipPathOk returns a tuple with the UiZipPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUiZipPath

`func (o *PluginInstallation) SetUiZipPath(v string)`

SetUiZipPath sets UiZipPath field to given value.

### HasUiZipPath

`func (o *PluginInstallation) HasUiZipPath() bool`

HasUiZipPath returns a boolean if a field has been set.

### GetEnabled

`func (o *PluginInstallation) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *PluginInstallation) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *PluginInstallation) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *PluginInstallation) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetOrganizationId

`func (o *PluginInstallation) GetOrganizationId() string`

GetOrganizationId returns the OrganizationId field if non-nil, zero value otherwise.

### GetOrganizationIdOk

`func (o *PluginInstallation) GetOrganizationIdOk() (*string, bool)`

GetOrganizationIdOk returns a tuple with the OrganizationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganizationId

`func (o *PluginInstallation) SetOrganizationId(v string)`

SetOrganizationId sets OrganizationId field to given value.

### HasOrganizationId

`func (o *PluginInstallation) HasOrganizationId() bool`

HasOrganizationId returns a boolean if a field has been set.

### GetOrganizationIdsJson

`func (o *PluginInstallation) GetOrganizationIdsJson() string`

GetOrganizationIdsJson returns the OrganizationIdsJson field if non-nil, zero value otherwise.

### GetOrganizationIdsJsonOk

`func (o *PluginInstallation) GetOrganizationIdsJsonOk() (*string, bool)`

GetOrganizationIdsJsonOk returns a tuple with the OrganizationIdsJson field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganizationIdsJson

`func (o *PluginInstallation) SetOrganizationIdsJson(v string)`

SetOrganizationIdsJson sets OrganizationIdsJson field to given value.

### HasOrganizationIdsJson

`func (o *PluginInstallation) HasOrganizationIdsJson() bool`

HasOrganizationIdsJson returns a boolean if a field has been set.

### GetMainClass

`func (o *PluginInstallation) GetMainClass() string`

GetMainClass returns the MainClass field if non-nil, zero value otherwise.

### GetMainClassOk

`func (o *PluginInstallation) GetMainClassOk() (*string, bool)`

GetMainClassOk returns a tuple with the MainClass field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMainClass

`func (o *PluginInstallation) SetMainClass(v string)`

SetMainClass sets MainClass field to given value.

### HasMainClass

`func (o *PluginInstallation) HasMainClass() bool`

HasMainClass returns a boolean if a field has been set.

### GetDescription

`func (o *PluginInstallation) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *PluginInstallation) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *PluginInstallation) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *PluginInstallation) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetInstalledAt

`func (o *PluginInstallation) GetInstalledAt() time.Time`

GetInstalledAt returns the InstalledAt field if non-nil, zero value otherwise.

### GetInstalledAtOk

`func (o *PluginInstallation) GetInstalledAtOk() (*time.Time, bool)`

GetInstalledAtOk returns a tuple with the InstalledAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstalledAt

`func (o *PluginInstallation) SetInstalledAt(v time.Time)`

SetInstalledAt sets InstalledAt field to given value.

### HasInstalledAt

`func (o *PluginInstallation) HasInstalledAt() bool`

HasInstalledAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *PluginInstallation) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *PluginInstallation) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *PluginInstallation) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *PluginInstallation) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetEnabledAt

`func (o *PluginInstallation) GetEnabledAt() time.Time`

GetEnabledAt returns the EnabledAt field if non-nil, zero value otherwise.

### GetEnabledAtOk

`func (o *PluginInstallation) GetEnabledAtOk() (*time.Time, bool)`

GetEnabledAtOk returns a tuple with the EnabledAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabledAt

`func (o *PluginInstallation) SetEnabledAt(v time.Time)`

SetEnabledAt sets EnabledAt field to given value.

### HasEnabledAt

`func (o *PluginInstallation) HasEnabledAt() bool`

HasEnabledAt returns a boolean if a field has been set.

### GetEnabledBy

`func (o *PluginInstallation) GetEnabledBy() string`

GetEnabledBy returns the EnabledBy field if non-nil, zero value otherwise.

### GetEnabledByOk

`func (o *PluginInstallation) GetEnabledByOk() (*string, bool)`

GetEnabledByOk returns a tuple with the EnabledBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabledBy

`func (o *PluginInstallation) SetEnabledBy(v string)`

SetEnabledBy sets EnabledBy field to given value.

### HasEnabledBy

`func (o *PluginInstallation) HasEnabledBy() bool`

HasEnabledBy returns a boolean if a field has been set.

### GetInstalledBy

`func (o *PluginInstallation) GetInstalledBy() string`

GetInstalledBy returns the InstalledBy field if non-nil, zero value otherwise.

### GetInstalledByOk

`func (o *PluginInstallation) GetInstalledByOk() (*string, bool)`

GetInstalledByOk returns a tuple with the InstalledBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstalledBy

`func (o *PluginInstallation) SetInstalledBy(v string)`

SetInstalledBy sets InstalledBy field to given value.

### HasInstalledBy

`func (o *PluginInstallation) HasInstalledBy() bool`

HasInstalledBy returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


