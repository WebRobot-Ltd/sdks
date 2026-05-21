# PrestoQueryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Sql** | Pointer to **string** |  | [optional] 
**Catalog** | Pointer to **string** |  | [optional] 
**Schema** | Pointer to **string** |  | [optional] 
**Limit** | Pointer to **int32** |  | [optional] 
**Offset** | Pointer to **int32** |  | [optional] 

## Methods

### NewPrestoQueryRequest

`func NewPrestoQueryRequest() *PrestoQueryRequest`

NewPrestoQueryRequest instantiates a new PrestoQueryRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPrestoQueryRequestWithDefaults

`func NewPrestoQueryRequestWithDefaults() *PrestoQueryRequest`

NewPrestoQueryRequestWithDefaults instantiates a new PrestoQueryRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSql

`func (o *PrestoQueryRequest) GetSql() string`

GetSql returns the Sql field if non-nil, zero value otherwise.

### GetSqlOk

`func (o *PrestoQueryRequest) GetSqlOk() (*string, bool)`

GetSqlOk returns a tuple with the Sql field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSql

`func (o *PrestoQueryRequest) SetSql(v string)`

SetSql sets Sql field to given value.

### HasSql

`func (o *PrestoQueryRequest) HasSql() bool`

HasSql returns a boolean if a field has been set.

### GetCatalog

`func (o *PrestoQueryRequest) GetCatalog() string`

GetCatalog returns the Catalog field if non-nil, zero value otherwise.

### GetCatalogOk

`func (o *PrestoQueryRequest) GetCatalogOk() (*string, bool)`

GetCatalogOk returns a tuple with the Catalog field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCatalog

`func (o *PrestoQueryRequest) SetCatalog(v string)`

SetCatalog sets Catalog field to given value.

### HasCatalog

`func (o *PrestoQueryRequest) HasCatalog() bool`

HasCatalog returns a boolean if a field has been set.

### GetSchema

`func (o *PrestoQueryRequest) GetSchema() string`

GetSchema returns the Schema field if non-nil, zero value otherwise.

### GetSchemaOk

`func (o *PrestoQueryRequest) GetSchemaOk() (*string, bool)`

GetSchemaOk returns a tuple with the Schema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSchema

`func (o *PrestoQueryRequest) SetSchema(v string)`

SetSchema sets Schema field to given value.

### HasSchema

`func (o *PrestoQueryRequest) HasSchema() bool`

HasSchema returns a boolean if a field has been set.

### GetLimit

`func (o *PrestoQueryRequest) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *PrestoQueryRequest) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *PrestoQueryRequest) SetLimit(v int32)`

SetLimit sets Limit field to given value.

### HasLimit

`func (o *PrestoQueryRequest) HasLimit() bool`

HasLimit returns a boolean if a field has been set.

### GetOffset

`func (o *PrestoQueryRequest) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *PrestoQueryRequest) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *PrestoQueryRequest) SetOffset(v int32)`

SetOffset sets Offset field to given value.

### HasOffset

`func (o *PrestoQueryRequest) HasOffset() bool`

HasOffset returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


