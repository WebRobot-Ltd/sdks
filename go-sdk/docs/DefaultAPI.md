# \DefaultAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddJobToProject**](DefaultAPI.md#AddJobToProject) | **Post** /webrobot/api/projects/id/{projectId}/jobs | 
[**CancelTraining**](DefaultAPI.md#CancelTraining) | **Delete** /webrobot/api/ai-providers/providers/{provider}/training/{jobId} | 
[**CreateAgent**](DefaultAPI.md#CreateAgent) | **Post** /webrobot/api/agents | 
[**CreateCategory**](DefaultAPI.md#CreateCategory) | **Post** /webrobot/api/categories | 
[**CreateProject**](DefaultAPI.md#CreateProject) | **Post** /webrobot/api/projects | 
[**CreateTask**](DefaultAPI.md#CreateTask) | **Post** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks | 
[**Delete**](DefaultAPI.md#Delete) | **Delete** /api/strapi-tables/{table}/{id} | 
[**DeleteAgent**](DefaultAPI.md#DeleteAgent) | **Delete** /webrobot/api/agents/{agentId} | 
[**DeleteCategory**](DefaultAPI.md#DeleteCategory) | **Delete** /webrobot/api/categories/id/{categoryId} | 
[**DeleteDataset**](DefaultAPI.md#DeleteDataset) | **Delete** /webrobot/api/datasets/{projectId}/{botId}/{datasetId} | 
[**DeleteDatasetVersion**](DefaultAPI.md#DeleteDatasetVersion) | **Delete** /webrobot/api/datasets/version/id/{versionsetId} | 
[**DeleteProject**](DefaultAPI.md#DeleteProject) | **Delete** /webrobot/api/projects/id/{projectId} | 
[**DeleteTask**](DefaultAPI.md#DeleteTask) | **Delete** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
[**DownloadModel**](DefaultAPI.md#DownloadModel) | **Get** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/download | 
[**EstimateCost**](DefaultAPI.md#EstimateCost) | **Post** /webrobot/api/ai-providers/providers/{provider}/cost-estimate | 
[**FindAll**](DefaultAPI.md#FindAll) | **Get** /api/strapi-tables/{table} | 
[**GetAgent**](DefaultAPI.md#GetAgent) | **Get** /webrobot/api/agents/{categoryId}/{agentId} | 
[**GetAgentFromName**](DefaultAPI.md#GetAgentFromName) | **Get** /webrobot/api/agents/{categoryId}/name/{agentName} | 
[**GetAllAgents**](DefaultAPI.md#GetAllAgents) | **Get** /webrobot/api/agents/{categoryId} | 
[**GetAllCategories**](DefaultAPI.md#GetAllCategories) | **Get** /webrobot/api/categories | 
[**GetAllDatasetVersions**](DefaultAPI.md#GetAllDatasetVersions) | **Get** /webrobot/api/datasets/{projectId}/{botId}/versions | 
[**GetAllDatasets**](DefaultAPI.md#GetAllDatasets) | **Get** /webrobot/api/datasets/datasets | 
[**GetAllProjects**](DefaultAPI.md#GetAllProjects) | **Get** /webrobot/api/projects | 
[**GetAllTasks**](DefaultAPI.md#GetAllTasks) | **Get** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks | 
[**GetAllVersionsets**](DefaultAPI.md#GetAllVersionsets) | **Get** /webrobot/api/datasets/{datasetId}/versions | 
[**GetById**](DefaultAPI.md#GetById) | **Get** /api/strapi-tables/{table}/{id} | 
[**GetCategory**](DefaultAPI.md#GetCategory) | **Get** /webrobot/api/categories/id/{categoryId} | 
[**GetCategoryFromName**](DefaultAPI.md#GetCategoryFromName) | **Get** /webrobot/api/categories/{categoryName} | 
[**GetDataset**](DefaultAPI.md#GetDataset) | **Get** /webrobot/api/datasets/{projectId}/{botId}/{datasetId} | 
[**GetDatasetInputFile**](DefaultAPI.md#GetDatasetInputFile) | **Get** /webrobot/api/datasets/{projectId}/{botId}/{datasetId}/input/url | 
[**GetDatasetInputFilePagination**](DefaultAPI.md#GetDatasetInputFilePagination) | **Get** /webrobot/api/datasets/{projectId}/{botId}/{datasetId}/input/{offset}/{limit} | 
[**GetDatasetInputFileSize**](DefaultAPI.md#GetDatasetInputFileSize) | **Get** /webrobot/api/datasets/{datasetId}/input/size | 
[**GetDatasetStatus**](DefaultAPI.md#GetDatasetStatus) | **Get** /webrobot/api/datasets/datasets/{datasetId}/status | 
[**GetDatasetVersionInputFile**](DefaultAPI.md#GetDatasetVersionInputFile) | **Get** /webrobot/api/datasets/{categoryId}/{jobId}/{datasetId}/versions/{versionsetId}/input/url | 
[**GetDatasetVersionInputFilePagination**](DefaultAPI.md#GetDatasetVersionInputFilePagination) | **Get** /webrobot/api/datasets/{datasetId}/versions/{versionsetId}/input/{offset}/{limit} | 
[**GetHealth**](DefaultAPI.md#GetHealth) | **Get** /health | 
[**GetHtml**](DefaultAPI.md#GetHtml) | **Get** /webrobot/api/html/{url}/{protocol} | 
[**GetProject**](DefaultAPI.md#GetProject) | **Get** /webrobot/api/projects/id/{projectId} | 
[**GetProjectFromName**](DefaultAPI.md#GetProjectFromName) | **Get** /webrobot/api/projects/{projectName} | 
[**GetProjectJobs**](DefaultAPI.md#GetProjectJobs) | **Get** /webrobot/api/projects/id/{projectId}/jobs | 
[**GetProjectSchedule**](DefaultAPI.md#GetProjectSchedule) | **Get** /webrobot/api/projects/id/{projectId}/schedule | 
[**GetSupportedModels**](DefaultAPI.md#GetSupportedModels) | **Get** /webrobot/api/ai-providers/providers/{provider}/models | 
[**GetSupportedProviders**](DefaultAPI.md#GetSupportedProviders) | **Get** /webrobot/api/ai-providers/providers | 
[**GetTask**](DefaultAPI.md#GetTask) | **Get** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
[**GetTaskStatus**](DefaultAPI.md#GetTaskStatus) | **Get** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/status | 
[**GetTrainingLogs**](DefaultAPI.md#GetTrainingLogs) | **Get** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/logs | 
[**GetTrainingStatus**](DefaultAPI.md#GetTrainingStatus) | **Get** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/status | 
[**GetUploadFileUrl**](DefaultAPI.md#GetUploadFileUrl) | **Get** /webrobot/api/datasets/{categoryId}/{jobId}/upload/{attachmentName} | 
[**GetUrlDownload**](DefaultAPI.md#GetUrlDownload) | **Get** /webrobot/api/package/download | 
[**GetUrlUpload**](DefaultAPI.md#GetUrlUpload) | **Get** /webrobot/api/package/upload | 
[**GetVersionset**](DefaultAPI.md#GetVersionset) | **Get** /webrobot/api/datasets/version/id/{versionsetId} | 
[**GetVersionsetFromVersion**](DefaultAPI.md#GetVersionsetFromVersion) | **Post** /webrobot/api/datasets/{datasetId}/versions/version/{version} | 
[**GetVersionsetFromVersionBase**](DefaultAPI.md#GetVersionsetFromVersionBase) | **Get** /webrobot/api/datasets/{datasetId}/versions/version/{version}/base | 
[**Insert**](DefaultAPI.md#Insert) | **Post** /api/strapi-tables/{table} | 
[**PublishModel**](DefaultAPI.md#PublishModel) | **Post** /webrobot/api/ai-providers/providers/huggingface/models/publish | 
[**RemoveJobFromProject**](DefaultAPI.md#RemoveJobFromProject) | **Delete** /webrobot/api/projects/id/{projectId}/jobs/{jobId} | 
[**SetProjectSchedule**](DefaultAPI.md#SetProjectSchedule) | **Put** /webrobot/api/projects/id/{projectId}/schedule | 
[**StartExportAll**](DefaultAPI.md#StartExportAll) | **Get** /webrobot/api/package/export/all | 
[**StartExportProject**](DefaultAPI.md#StartExportProject) | **Get** /webrobot/api/package/export/id/{projectId} | 
[**StartImportAll**](DefaultAPI.md#StartImportAll) | **Get** /webrobot/api/package/import/all | 
[**StartImportProject**](DefaultAPI.md#StartImportProject) | **Get** /webrobot/api/package/import/id/{projectId} | 
[**StartTask**](DefaultAPI.md#StartTask) | **Post** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/start | 
[**StartTraining**](DefaultAPI.md#StartTraining) | **Post** /webrobot/api/ai-providers/providers/{provider}/training | 
[**StopTask**](DefaultAPI.md#StopTask) | **Post** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/stop | 
[**Test**](DefaultAPI.md#Test) | **Get** /webrobot/api/categories/test | 
[**Test1**](DefaultAPI.md#Test1) | **Get** /webrobot/api/projects/test | 
[**Update**](DefaultAPI.md#Update) | **Put** /api/strapi-tables/{table}/{id} | 
[**UpdateAgent**](DefaultAPI.md#UpdateAgent) | **Put** /webrobot/api/agents/{categoryId}/{agentId} | 
[**UpdateCategory**](DefaultAPI.md#UpdateCategory) | **Put** /webrobot/api/categories/id/{categoryId} | 
[**UpdateProject**](DefaultAPI.md#UpdateProject) | **Put** /webrobot/api/projects/id/{projectId} | 
[**UpdateTask**](DefaultAPI.md#UpdateTask) | **Put** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
[**UploadDataset**](DefaultAPI.md#UploadDataset) | **Post** /webrobot/api/ai-providers/providers/{provider}/datasets | 
[**UploadDataset1**](DefaultAPI.md#UploadDataset1) | **Post** /webrobot/api/datasets/{projectId}/{botId} | 



## AddJobToProject

> AddJobToProject(ctx, projectId).XRapidAPIUser(xRapidAPIUser).JobDto(jobDto).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	jobDto := *openapiclient.NewJobDto() // JobDto |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.AddJobToProject(context.Background(), projectId).XRapidAPIUser(xRapidAPIUser).JobDto(jobDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.AddJobToProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddJobToProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 
 **jobDto** | [**JobDto**](JobDto.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CancelTraining

> CancelTraining(ctx, provider, jobId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	provider := "provider_example" // string | 
	jobId := "jobId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.CancelTraining(context.Background(), provider, jobId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CancelTraining``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**provider** | **string** |  | 
**jobId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCancelTrainingRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateAgent

> CreateAgent(ctx).XRapidAPIUser(xRapidAPIUser).AgentDto(agentDto).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	agentDto := *openapiclient.NewAgentDto() // AgentDto |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.CreateAgent(context.Background()).XRapidAPIUser(xRapidAPIUser).AgentDto(agentDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateAgent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateAgentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 
 **agentDto** | [**AgentDto**](AgentDto.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateCategory

> CreateCategory(ctx).XRapidAPIUser(xRapidAPIUser).JobCategoryDto(jobCategoryDto).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	jobCategoryDto := *openapiclient.NewJobCategoryDto() // JobCategoryDto |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.CreateCategory(context.Background()).XRapidAPIUser(xRapidAPIUser).JobCategoryDto(jobCategoryDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateCategory``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateCategoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 
 **jobCategoryDto** | [**JobCategoryDto**](JobCategoryDto.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateProject

> CreateProject(ctx).XRapidAPIUser(xRapidAPIUser).JobProjectDto(jobProjectDto).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	jobProjectDto := *openapiclient.NewJobProjectDto() // JobProjectDto |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.CreateProject(context.Background()).XRapidAPIUser(xRapidAPIUser).JobProjectDto(jobProjectDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 
 **jobProjectDto** | [**JobProjectDto**](JobProjectDto.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateTask

> CreateTask(ctx, projectId, jobId).XRapidAPIUser(xRapidAPIUser).TaskDto(taskDto).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	jobId := "jobId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	taskDto := *openapiclient.NewTaskDto() // TaskDto |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.CreateTask(context.Background(), projectId, jobId).XRapidAPIUser(xRapidAPIUser).TaskDto(taskDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateTask``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 
**jobId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateTaskRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xRapidAPIUser** | **string** |  | 
 **taskDto** | [**TaskDto**](TaskDto.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Delete

> Delete(ctx, table, id).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	table := "table_example" // string | 
	id := "id_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.Delete(context.Background(), table, id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.Delete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**table** | **string** |  | 
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteAgent

> DeleteAgent(ctx, agentId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	agentId := "agentId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.DeleteAgent(context.Background(), agentId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteAgent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**agentId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteAgentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteCategory

> DeleteCategory(ctx, categoryId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	categoryId := "categoryId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.DeleteCategory(context.Background(), categoryId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteCategory``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**categoryId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteCategoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteDataset

> DeleteDataset(ctx, datasetId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	datasetId := "datasetId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.DeleteDataset(context.Background(), datasetId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteDataset``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**datasetId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteDatasetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteDatasetVersion

> DeleteDatasetVersion(ctx, versionsetId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	versionsetId := "versionsetId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.DeleteDatasetVersion(context.Background(), versionsetId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteDatasetVersion``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**versionsetId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteDatasetVersionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteProject

> DeleteProject(ctx, projectId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.DeleteProject(context.Background(), projectId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteTask

> DeleteTask(ctx, projectId, jobId, taskId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	jobId := "jobId_example" // string | 
	taskId := "taskId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.DeleteTask(context.Background(), projectId, jobId, taskId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteTask``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 
**jobId** | **string** |  | 
**taskId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteTaskRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadModel

> DownloadModel(ctx, provider, jobId).XRapidAPIUser(xRapidAPIUser).OutputPath(outputPath).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	provider := "provider_example" // string | 
	jobId := "jobId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	outputPath := "outputPath_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.DownloadModel(context.Background(), provider, jobId).XRapidAPIUser(xRapidAPIUser).OutputPath(outputPath).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DownloadModel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**provider** | **string** |  | 
**jobId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadModelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xRapidAPIUser** | **string** |  | 
 **outputPath** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## EstimateCost

> EstimateCost(ctx, provider).XRapidAPIUser(xRapidAPIUser).TrainingRequestBean(trainingRequestBean).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	provider := "provider_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	trainingRequestBean := *openapiclient.NewTrainingRequestBean() // TrainingRequestBean |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.EstimateCost(context.Background(), provider).XRapidAPIUser(xRapidAPIUser).TrainingRequestBean(trainingRequestBean).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.EstimateCost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**provider** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiEstimateCostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 
 **trainingRequestBean** | [**TrainingRequestBean**](TrainingRequestBean.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FindAll

> FindAll(ctx, table).Page(page).PageSize(pageSize).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	table := "table_example" // string | 
	page := int32(56) // int32 |  (optional) (default to 0)
	pageSize := int32(56) // int32 |  (optional) (default to 50)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.FindAll(context.Background(), table).Page(page).PageSize(pageSize).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.FindAll``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**table** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiFindAllRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **page** | **int32** |  | [default to 0]
 **pageSize** | **int32** |  | [default to 50]

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAgent

> GetAgent(ctx, categoryId, agentId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	categoryId := "categoryId_example" // string | 
	agentId := "agentId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetAgent(context.Background(), categoryId, agentId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetAgent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**categoryId** | **string** |  | 
**agentId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAgentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAgentFromName

> GetAgentFromName(ctx, categoryId, agentName).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	categoryId := "categoryId_example" // string | 
	agentName := "agentName_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetAgentFromName(context.Background(), categoryId, agentName).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetAgentFromName``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**categoryId** | **string** |  | 
**agentName** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAgentFromNameRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAllAgents

> GetAllAgents(ctx, categoryId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	categoryId := "categoryId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetAllAgents(context.Background(), categoryId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetAllAgents``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**categoryId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAllAgentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAllCategories

> GetAllCategories(ctx).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetAllCategories(context.Background()).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetAllCategories``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetAllCategoriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAllDatasetVersions

> GetAllDatasetVersions(ctx).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetAllDatasetVersions(context.Background()).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetAllDatasetVersions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetAllDatasetVersionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAllDatasets

> GetAllDatasets(ctx).XRapidAPIUser(xRapidAPIUser).Status(status).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	status := "status_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetAllDatasets(context.Background()).XRapidAPIUser(xRapidAPIUser).Status(status).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetAllDatasets``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetAllDatasetsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 
 **status** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAllProjects

> GetAllProjects(ctx).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetAllProjects(context.Background()).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetAllProjects``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetAllProjectsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAllTasks

> GetAllTasks(ctx, projectId, jobId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	jobId := "jobId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetAllTasks(context.Background(), projectId, jobId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetAllTasks``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 
**jobId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAllTasksRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAllVersionsets

> GetAllVersionsets(ctx, datasetId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	datasetId := "datasetId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetAllVersionsets(context.Background(), datasetId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetAllVersionsets``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**datasetId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAllVersionsetsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetById

> GetById(ctx, table, id).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	table := "table_example" // string | 
	id := "id_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetById(context.Background(), table, id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetById``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**table** | **string** |  | 
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCategory

> GetCategory(ctx, categoryId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	categoryId := "categoryId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetCategory(context.Background(), categoryId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetCategory``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**categoryId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetCategoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCategoryFromName

> GetCategoryFromName(ctx, categoryName).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	categoryName := "categoryName_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetCategoryFromName(context.Background(), categoryName).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetCategoryFromName``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**categoryName** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetCategoryFromNameRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDataset

> GetDataset(ctx, datasetId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	datasetId := "datasetId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetDataset(context.Background(), datasetId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetDataset``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**datasetId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDatasetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDatasetInputFile

> GetDatasetInputFile(ctx, datasetId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	datasetId := "datasetId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetDatasetInputFile(context.Background(), datasetId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetDatasetInputFile``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**datasetId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDatasetInputFileRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDatasetInputFilePagination

> GetDatasetInputFilePagination(ctx, offset, datasetId, limit).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	offset := int32(56) // int32 | 
	datasetId := "datasetId_example" // string | 
	limit := int32(56) // int32 | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetDatasetInputFilePagination(context.Background(), offset, datasetId, limit).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetDatasetInputFilePagination``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**offset** | **int32** |  | 
**datasetId** | **string** |  | 
**limit** | **int32** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDatasetInputFilePaginationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDatasetInputFileSize

> GetDatasetInputFileSize(ctx, datasetId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	datasetId := "datasetId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetDatasetInputFileSize(context.Background(), datasetId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetDatasetInputFileSize``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**datasetId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDatasetInputFileSizeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDatasetStatus

> GetDatasetStatus(ctx, datasetId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	datasetId := "datasetId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetDatasetStatus(context.Background(), datasetId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetDatasetStatus``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**datasetId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDatasetStatusRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDatasetVersionInputFile

> GetDatasetVersionInputFile(ctx, categoryId, jobId, versionsetId, datasetId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	categoryId := "categoryId_example" // string | 
	jobId := "jobId_example" // string | 
	versionsetId := "versionsetId_example" // string | 
	datasetId := "datasetId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetDatasetVersionInputFile(context.Background(), categoryId, jobId, versionsetId, datasetId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetDatasetVersionInputFile``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**categoryId** | **string** |  | 
**jobId** | **string** |  | 
**versionsetId** | **string** |  | 
**datasetId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDatasetVersionInputFileRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDatasetVersionInputFilePagination

> GetDatasetVersionInputFilePagination(ctx, projectId, botId, offset, limit, versionsetId, datasetId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	botId := "botId_example" // string | 
	offset := int32(56) // int32 | 
	limit := int32(56) // int32 | 
	versionsetId := "versionsetId_example" // string | 
	datasetId := "datasetId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetDatasetVersionInputFilePagination(context.Background(), projectId, botId, offset, limit, versionsetId, datasetId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetDatasetVersionInputFilePagination``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 
**botId** | **string** |  | 
**offset** | **int32** |  | 
**limit** | **int32** |  | 
**versionsetId** | **string** |  | 
**datasetId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDatasetVersionInputFilePaginationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------






 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetHealth

> GetHealth(ctx).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetHealth(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetHealth``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetHealthRequest struct via the builder pattern


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetHtml

> GetHtml(ctx, protocol, url).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	protocol := "protocol_example" // string | 
	url := "url_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetHtml(context.Background(), protocol, url).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetHtml``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**protocol** | **string** |  | 
**url** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetHtmlRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProject

> GetProject(ctx, projectId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetProject(context.Background(), projectId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProjectFromName

> GetProjectFromName(ctx, projectName).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectName := "projectName_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetProjectFromName(context.Background(), projectName).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetProjectFromName``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectName** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetProjectFromNameRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProjectJobs

> GetProjectJobs(ctx, projectId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetProjectJobs(context.Background(), projectId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetProjectJobs``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetProjectJobsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProjectSchedule

> GetProjectSchedule(ctx, projectId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetProjectSchedule(context.Background(), projectId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetProjectSchedule``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetProjectScheduleRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSupportedModels

> GetSupportedModels(ctx, provider).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	provider := "provider_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetSupportedModels(context.Background(), provider).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetSupportedModels``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**provider** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSupportedModelsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSupportedProviders

> GetSupportedProviders(ctx).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetSupportedProviders(context.Background()).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetSupportedProviders``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSupportedProvidersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTask

> GetTask(ctx, projectId, jobId, taskId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	jobId := "jobId_example" // string | 
	taskId := "taskId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetTask(context.Background(), projectId, jobId, taskId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetTask``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 
**jobId** | **string** |  | 
**taskId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTaskRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTaskStatus

> GetTaskStatus(ctx, projectId, jobId, taskId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	jobId := "jobId_example" // string | 
	taskId := "taskId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetTaskStatus(context.Background(), projectId, jobId, taskId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetTaskStatus``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 
**jobId** | **string** |  | 
**taskId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTaskStatusRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTrainingLogs

> GetTrainingLogs(ctx, provider, jobId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	provider := "provider_example" // string | 
	jobId := "jobId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetTrainingLogs(context.Background(), provider, jobId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetTrainingLogs``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**provider** | **string** |  | 
**jobId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTrainingLogsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTrainingStatus

> GetTrainingStatus(ctx, provider, jobId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	provider := "provider_example" // string | 
	jobId := "jobId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetTrainingStatus(context.Background(), provider, jobId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetTrainingStatus``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**provider** | **string** |  | 
**jobId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTrainingStatusRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetUploadFileUrl

> GetUploadFileUrl(ctx, projectId, botId, attachmentName).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	botId := "botId_example" // string | 
	attachmentName := "attachmentName_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetUploadFileUrl(context.Background(), projectId, botId, attachmentName).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetUploadFileUrl``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 
**botId** | **string** |  | 
**attachmentName** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetUploadFileUrlRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetUrlDownload

> GetUrlDownload(ctx).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetUrlDownload(context.Background()).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetUrlDownload``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetUrlDownloadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetUrlUpload

> GetUrlUpload(ctx).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetUrlUpload(context.Background()).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetUrlUpload``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetUrlUploadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetVersionset

> GetVersionset(ctx, versionsetId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	versionsetId := "versionsetId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetVersionset(context.Background(), versionsetId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetVersionset``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**versionsetId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetVersionsetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetVersionsetFromVersion

> GetVersionsetFromVersion(ctx, datasetId, version).XRapidAPIUser(xRapidAPIUser).TimePeriod(timePeriod).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	datasetId := "datasetId_example" // string | 
	version := "version_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	timePeriod := *openapiclient.NewTimePeriod() // TimePeriod |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetVersionsetFromVersion(context.Background(), datasetId, version).XRapidAPIUser(xRapidAPIUser).TimePeriod(timePeriod).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetVersionsetFromVersion``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**datasetId** | **string** |  | 
**version** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetVersionsetFromVersionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xRapidAPIUser** | **string** |  | 
 **timePeriod** | [**TimePeriod**](TimePeriod.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetVersionsetFromVersionBase

> GetVersionsetFromVersionBase(ctx, datasetId, version).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	datasetId := "datasetId_example" // string | 
	version := "version_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.GetVersionsetFromVersionBase(context.Background(), datasetId, version).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetVersionsetFromVersionBase``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**datasetId** | **string** |  | 
**version** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetVersionsetFromVersionBaseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Insert

> Insert(ctx, table).RequestBody(requestBody).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	table := "table_example" // string | 
	requestBody := map[string]map[string]interface{}{"key": map[string]interface{}(123)} // map[string]map[string]interface{} |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.Insert(context.Background(), table).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.Insert``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**table** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiInsertRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **requestBody** | **map[string]map[string]interface{}** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PublishModel

> PublishModel(ctx).XRapidAPIUser(xRapidAPIUser).ModelPublishRequest(modelPublishRequest).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	modelPublishRequest := *openapiclient.NewModelPublishRequest() // ModelPublishRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.PublishModel(context.Background()).XRapidAPIUser(xRapidAPIUser).ModelPublishRequest(modelPublishRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PublishModel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPublishModelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 
 **modelPublishRequest** | [**ModelPublishRequest**](ModelPublishRequest.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RemoveJobFromProject

> RemoveJobFromProject(ctx, projectId, jobId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	jobId := "jobId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.RemoveJobFromProject(context.Background(), projectId, jobId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RemoveJobFromProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 
**jobId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRemoveJobFromProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SetProjectSchedule

> SetProjectSchedule(ctx, projectId).XRapidAPIUser(xRapidAPIUser).ProjectScheduleRequest(projectScheduleRequest).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	projectScheduleRequest := *openapiclient.NewProjectScheduleRequest() // ProjectScheduleRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.SetProjectSchedule(context.Background(), projectId).XRapidAPIUser(xRapidAPIUser).ProjectScheduleRequest(projectScheduleRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.SetProjectSchedule``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiSetProjectScheduleRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 
 **projectScheduleRequest** | [**ProjectScheduleRequest**](ProjectScheduleRequest.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StartExportAll

> StartExportAll(ctx).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.StartExportAll(context.Background()).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.StartExportAll``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiStartExportAllRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StartExportProject

> StartExportProject(ctx, projectId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.StartExportProject(context.Background(), projectId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.StartExportProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStartExportProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StartImportAll

> StartImportAll(ctx).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.StartImportAll(context.Background()).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.StartImportAll``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiStartImportAllRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StartImportProject

> StartImportProject(ctx, projectId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.StartImportProject(context.Background(), projectId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.StartImportProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStartImportProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StartTask

> StartTask(ctx, projectId, jobId, taskId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	jobId := "jobId_example" // string | 
	taskId := "taskId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.StartTask(context.Background(), projectId, jobId, taskId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.StartTask``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 
**jobId** | **string** |  | 
**taskId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStartTaskRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StartTraining

> StartTraining(ctx, provider).XRapidAPIUser(xRapidAPIUser).TrainingRequestBean(trainingRequestBean).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	provider := "provider_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	trainingRequestBean := *openapiclient.NewTrainingRequestBean() // TrainingRequestBean |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.StartTraining(context.Background(), provider).XRapidAPIUser(xRapidAPIUser).TrainingRequestBean(trainingRequestBean).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.StartTraining``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**provider** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStartTrainingRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 
 **trainingRequestBean** | [**TrainingRequestBean**](TrainingRequestBean.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StopTask

> StopTask(ctx, projectId, jobId, taskId).XRapidAPIUser(xRapidAPIUser).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	jobId := "jobId_example" // string | 
	taskId := "taskId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.StopTask(context.Background(), projectId, jobId, taskId).XRapidAPIUser(xRapidAPIUser).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.StopTask``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 
**jobId** | **string** |  | 
**taskId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStopTaskRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **xRapidAPIUser** | **string** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Test

> Test(ctx).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.Test(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.Test``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiTestRequest struct via the builder pattern


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Test1

> Test1(ctx).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.Test1(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.Test1``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiTest1Request struct via the builder pattern


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Update

> Update(ctx, table, id).RequestBody(requestBody).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	table := "table_example" // string | 
	id := "id_example" // string | 
	requestBody := map[string]map[string]interface{}{"key": map[string]interface{}(123)} // map[string]map[string]interface{} |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.Update(context.Background(), table, id).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.Update``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**table** | **string** |  | 
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **requestBody** | **map[string]map[string]interface{}** |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateAgent

> UpdateAgent(ctx, categoryId, agentId).XRapidAPIUser(xRapidAPIUser).AgentDto(agentDto).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	categoryId := "categoryId_example" // string | 
	agentId := "agentId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	agentDto := *openapiclient.NewAgentDto() // AgentDto |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.UpdateAgent(context.Background(), categoryId, agentId).XRapidAPIUser(xRapidAPIUser).AgentDto(agentDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.UpdateAgent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**categoryId** | **string** |  | 
**agentId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateAgentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xRapidAPIUser** | **string** |  | 
 **agentDto** | [**AgentDto**](AgentDto.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateCategory

> UpdateCategory(ctx, categoryId).XRapidAPIUser(xRapidAPIUser).JobCategoryDto(jobCategoryDto).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	categoryId := "categoryId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	jobCategoryDto := *openapiclient.NewJobCategoryDto() // JobCategoryDto |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.UpdateCategory(context.Background(), categoryId).XRapidAPIUser(xRapidAPIUser).JobCategoryDto(jobCategoryDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.UpdateCategory``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**categoryId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateCategoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 
 **jobCategoryDto** | [**JobCategoryDto**](JobCategoryDto.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateProject

> UpdateProject(ctx, projectId).XRapidAPIUser(xRapidAPIUser).JobProjectDto(jobProjectDto).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	jobProjectDto := *openapiclient.NewJobProjectDto() // JobProjectDto |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.UpdateProject(context.Background(), projectId).XRapidAPIUser(xRapidAPIUser).JobProjectDto(jobProjectDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.UpdateProject``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateProjectRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 
 **jobProjectDto** | [**JobProjectDto**](JobProjectDto.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateTask

> UpdateTask(ctx, projectId, jobId, taskId).XRapidAPIUser(xRapidAPIUser).TaskDto(taskDto).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	projectId := "projectId_example" // string | 
	jobId := "jobId_example" // string | 
	taskId := "taskId_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	taskDto := *openapiclient.NewTaskDto() // TaskDto |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.UpdateTask(context.Background(), projectId, jobId, taskId).XRapidAPIUser(xRapidAPIUser).TaskDto(taskDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.UpdateTask``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**projectId** | **string** |  | 
**jobId** | **string** |  | 
**taskId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateTaskRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **xRapidAPIUser** | **string** |  | 
 **taskDto** | [**TaskDto**](TaskDto.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UploadDataset

> UploadDataset(ctx, provider).XRapidAPIUser(xRapidAPIUser).DatasetUploadRequest(datasetUploadRequest).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	provider := "provider_example" // string | 
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	datasetUploadRequest := *openapiclient.NewDatasetUploadRequest() // DatasetUploadRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.UploadDataset(context.Background(), provider).XRapidAPIUser(xRapidAPIUser).DatasetUploadRequest(datasetUploadRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.UploadDataset``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**provider** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUploadDatasetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xRapidAPIUser** | **string** |  | 
 **datasetUploadRequest** | [**DatasetUploadRequest**](DatasetUploadRequest.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UploadDataset1

> UploadDataset1(ctx).XRapidAPIUser(xRapidAPIUser).DatasetUploadApiDto(datasetUploadApiDto).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	xRapidAPIUser := "xRapidAPIUser_example" // string |  (optional)
	datasetUploadApiDto := *openapiclient.NewDatasetUploadApiDto() // DatasetUploadApiDto |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.UploadDataset1(context.Background()).XRapidAPIUser(xRapidAPIUser).DatasetUploadApiDto(datasetUploadApiDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.UploadDataset1``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUploadDataset1Request struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRapidAPIUser** | **string** |  | 
 **datasetUploadApiDto** | [**DatasetUploadApiDto**](DatasetUploadApiDto.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

