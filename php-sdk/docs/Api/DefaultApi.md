# OpenAPI\Client\DefaultApi

All URIs are relative to http://localhost, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addJobToProject()**](DefaultApi.md#addJobToProject) | **POST** /webrobot/api/projects/id/{projectId}/jobs |  |
| [**cancelTraining()**](DefaultApi.md#cancelTraining) | **DELETE** /webrobot/api/ai-providers/providers/{provider}/training/{jobId} |  |
| [**createAgent()**](DefaultApi.md#createAgent) | **POST** /webrobot/api/agents |  |
| [**createCategory()**](DefaultApi.md#createCategory) | **POST** /webrobot/api/categories |  |
| [**createProject()**](DefaultApi.md#createProject) | **POST** /webrobot/api/projects |  |
| [**createTask()**](DefaultApi.md#createTask) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks |  |
| [**delete()**](DefaultApi.md#delete) | **DELETE** /api/strapi-tables/{table}/{id} |  |
| [**deleteAgent()**](DefaultApi.md#deleteAgent) | **DELETE** /webrobot/api/agents/{agentId} |  |
| [**deleteCategory()**](DefaultApi.md#deleteCategory) | **DELETE** /webrobot/api/categories/id/{categoryId} |  |
| [**deleteDataset()**](DefaultApi.md#deleteDataset) | **DELETE** /webrobot/api/datasets/{projectId}/{botId}/{datasetId} |  |
| [**deleteDatasetVersion()**](DefaultApi.md#deleteDatasetVersion) | **DELETE** /webrobot/api/datasets/version/id/{versionsetId} |  |
| [**deleteProject()**](DefaultApi.md#deleteProject) | **DELETE** /webrobot/api/projects/id/{projectId} |  |
| [**deleteTask()**](DefaultApi.md#deleteTask) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} |  |
| [**downloadModel()**](DefaultApi.md#downloadModel) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/download |  |
| [**estimateCost()**](DefaultApi.md#estimateCost) | **POST** /webrobot/api/ai-providers/providers/{provider}/cost-estimate |  |
| [**findAll()**](DefaultApi.md#findAll) | **GET** /api/strapi-tables/{table} |  |
| [**getAgent()**](DefaultApi.md#getAgent) | **GET** /webrobot/api/agents/{categoryId}/{agentId} |  |
| [**getAgentFromName()**](DefaultApi.md#getAgentFromName) | **GET** /webrobot/api/agents/{categoryId}/name/{agentName} |  |
| [**getAllAgents()**](DefaultApi.md#getAllAgents) | **GET** /webrobot/api/agents/{categoryId} |  |
| [**getAllCategories()**](DefaultApi.md#getAllCategories) | **GET** /webrobot/api/categories |  |
| [**getAllDatasetVersions()**](DefaultApi.md#getAllDatasetVersions) | **GET** /webrobot/api/datasets/{projectId}/{botId}/versions |  |
| [**getAllDatasets()**](DefaultApi.md#getAllDatasets) | **GET** /webrobot/api/datasets/datasets |  |
| [**getAllProjects()**](DefaultApi.md#getAllProjects) | **GET** /webrobot/api/projects |  |
| [**getAllTasks()**](DefaultApi.md#getAllTasks) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks |  |
| [**getAllVersionsets()**](DefaultApi.md#getAllVersionsets) | **GET** /webrobot/api/datasets/{datasetId}/versions |  |
| [**getById()**](DefaultApi.md#getById) | **GET** /api/strapi-tables/{table}/{id} |  |
| [**getCategory()**](DefaultApi.md#getCategory) | **GET** /webrobot/api/categories/id/{categoryId} |  |
| [**getCategoryFromName()**](DefaultApi.md#getCategoryFromName) | **GET** /webrobot/api/categories/{categoryName} |  |
| [**getDataset()**](DefaultApi.md#getDataset) | **GET** /webrobot/api/datasets/{projectId}/{botId}/{datasetId} |  |
| [**getDatasetInputFile()**](DefaultApi.md#getDatasetInputFile) | **GET** /webrobot/api/datasets/{projectId}/{botId}/{datasetId}/input/url |  |
| [**getDatasetInputFilePagination()**](DefaultApi.md#getDatasetInputFilePagination) | **GET** /webrobot/api/datasets/{projectId}/{botId}/{datasetId}/input/{offset}/{limit} |  |
| [**getDatasetInputFileSize()**](DefaultApi.md#getDatasetInputFileSize) | **GET** /webrobot/api/datasets/{datasetId}/input/size |  |
| [**getDatasetStatus()**](DefaultApi.md#getDatasetStatus) | **GET** /webrobot/api/datasets/datasets/{datasetId}/status |  |
| [**getDatasetVersionInputFile()**](DefaultApi.md#getDatasetVersionInputFile) | **GET** /webrobot/api/datasets/{categoryId}/{jobId}/{datasetId}/versions/{versionsetId}/input/url |  |
| [**getDatasetVersionInputFilePagination()**](DefaultApi.md#getDatasetVersionInputFilePagination) | **GET** /webrobot/api/datasets/{datasetId}/versions/{versionsetId}/input/{offset}/{limit} |  |
| [**getHealth()**](DefaultApi.md#getHealth) | **GET** /health |  |
| [**getHtml()**](DefaultApi.md#getHtml) | **GET** /webrobot/api/html/{url}/{protocol} |  |
| [**getProject()**](DefaultApi.md#getProject) | **GET** /webrobot/api/projects/id/{projectId} |  |
| [**getProjectFromName()**](DefaultApi.md#getProjectFromName) | **GET** /webrobot/api/projects/{projectName} |  |
| [**getProjectJobs()**](DefaultApi.md#getProjectJobs) | **GET** /webrobot/api/projects/id/{projectId}/jobs |  |
| [**getProjectSchedule()**](DefaultApi.md#getProjectSchedule) | **GET** /webrobot/api/projects/id/{projectId}/schedule |  |
| [**getSupportedModels()**](DefaultApi.md#getSupportedModels) | **GET** /webrobot/api/ai-providers/providers/{provider}/models |  |
| [**getSupportedProviders()**](DefaultApi.md#getSupportedProviders) | **GET** /webrobot/api/ai-providers/providers |  |
| [**getTask()**](DefaultApi.md#getTask) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} |  |
| [**getTaskStatus()**](DefaultApi.md#getTaskStatus) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/status |  |
| [**getTrainingLogs()**](DefaultApi.md#getTrainingLogs) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/logs |  |
| [**getTrainingStatus()**](DefaultApi.md#getTrainingStatus) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/status |  |
| [**getUploadFileUrl()**](DefaultApi.md#getUploadFileUrl) | **GET** /webrobot/api/datasets/{categoryId}/{jobId}/upload/{attachmentName} |  |
| [**getUrlDownload()**](DefaultApi.md#getUrlDownload) | **GET** /webrobot/api/package/download |  |
| [**getUrlUpload()**](DefaultApi.md#getUrlUpload) | **GET** /webrobot/api/package/upload |  |
| [**getVersionset()**](DefaultApi.md#getVersionset) | **GET** /webrobot/api/datasets/version/id/{versionsetId} |  |
| [**getVersionsetFromVersion()**](DefaultApi.md#getVersionsetFromVersion) | **POST** /webrobot/api/datasets/{datasetId}/versions/version/{version} |  |
| [**getVersionsetFromVersionBase()**](DefaultApi.md#getVersionsetFromVersionBase) | **GET** /webrobot/api/datasets/{datasetId}/versions/version/{version}/base |  |
| [**insert()**](DefaultApi.md#insert) | **POST** /api/strapi-tables/{table} |  |
| [**publishModel()**](DefaultApi.md#publishModel) | **POST** /webrobot/api/ai-providers/providers/huggingface/models/publish |  |
| [**removeJobFromProject()**](DefaultApi.md#removeJobFromProject) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId} |  |
| [**setProjectSchedule()**](DefaultApi.md#setProjectSchedule) | **PUT** /webrobot/api/projects/id/{projectId}/schedule |  |
| [**startExportAll()**](DefaultApi.md#startExportAll) | **GET** /webrobot/api/package/export/all |  |
| [**startExportProject()**](DefaultApi.md#startExportProject) | **GET** /webrobot/api/package/export/id/{projectId} |  |
| [**startImportAll()**](DefaultApi.md#startImportAll) | **GET** /webrobot/api/package/import/all |  |
| [**startImportProject()**](DefaultApi.md#startImportProject) | **GET** /webrobot/api/package/import/id/{projectId} |  |
| [**startTask()**](DefaultApi.md#startTask) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/start |  |
| [**startTraining()**](DefaultApi.md#startTraining) | **POST** /webrobot/api/ai-providers/providers/{provider}/training |  |
| [**stopTask()**](DefaultApi.md#stopTask) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/stop |  |
| [**test()**](DefaultApi.md#test) | **GET** /webrobot/api/categories/test |  |
| [**test1()**](DefaultApi.md#test1) | **GET** /webrobot/api/projects/test |  |
| [**update()**](DefaultApi.md#update) | **PUT** /api/strapi-tables/{table}/{id} |  |
| [**updateAgent()**](DefaultApi.md#updateAgent) | **PUT** /webrobot/api/agents/{categoryId}/{agentId} |  |
| [**updateCategory()**](DefaultApi.md#updateCategory) | **PUT** /webrobot/api/categories/id/{categoryId} |  |
| [**updateProject()**](DefaultApi.md#updateProject) | **PUT** /webrobot/api/projects/id/{projectId} |  |
| [**updateTask()**](DefaultApi.md#updateTask) | **PUT** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} |  |
| [**uploadDataset()**](DefaultApi.md#uploadDataset) | **POST** /webrobot/api/ai-providers/providers/{provider}/datasets |  |
| [**uploadDataset1()**](DefaultApi.md#uploadDataset1) | **POST** /webrobot/api/datasets/{projectId}/{botId} |  |


## `addJobToProject()`

```php
addJobToProject($project_id, $x_rapid_api_user, $job_dto)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$job_dto = new \OpenAPI\Client\Model\JobDto(); // \OpenAPI\Client\Model\JobDto

try {
    $apiInstance->addJobToProject($project_id, $x_rapid_api_user, $job_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->addJobToProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |
| **job_dto** | [**\OpenAPI\Client\Model\JobDto**](../Model/JobDto.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `cancelTraining()`

```php
cancelTraining($provider, $job_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$provider = 'provider_example'; // string
$job_id = 'job_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->cancelTraining($provider, $job_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->cancelTraining: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
| **job_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createAgent()`

```php
createAgent($x_rapid_api_user, $agent_dto)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$agent_dto = new \OpenAPI\Client\Model\AgentDto(); // \OpenAPI\Client\Model\AgentDto

try {
    $apiInstance->createAgent($x_rapid_api_user, $agent_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createAgent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |
| **agent_dto** | [**\OpenAPI\Client\Model\AgentDto**](../Model/AgentDto.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createCategory()`

```php
createCategory($x_rapid_api_user, $job_category_dto)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$job_category_dto = new \OpenAPI\Client\Model\JobCategoryDto(); // \OpenAPI\Client\Model\JobCategoryDto

try {
    $apiInstance->createCategory($x_rapid_api_user, $job_category_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createCategory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |
| **job_category_dto** | [**\OpenAPI\Client\Model\JobCategoryDto**](../Model/JobCategoryDto.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createProject()`

```php
createProject($x_rapid_api_user, $job_project_dto)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$job_project_dto = new \OpenAPI\Client\Model\JobProjectDto(); // \OpenAPI\Client\Model\JobProjectDto

try {
    $apiInstance->createProject($x_rapid_api_user, $job_project_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |
| **job_project_dto** | [**\OpenAPI\Client\Model\JobProjectDto**](../Model/JobProjectDto.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createTask()`

```php
createTask($project_id, $job_id, $x_rapid_api_user, $task_dto)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$job_id = 'job_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$task_dto = new \OpenAPI\Client\Model\TaskDto(); // \OpenAPI\Client\Model\TaskDto

try {
    $apiInstance->createTask($project_id, $job_id, $x_rapid_api_user, $task_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createTask: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |
| **task_dto** | [**\OpenAPI\Client\Model\TaskDto**](../Model/TaskDto.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `delete()`

```php
delete($table, $id)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$table = 'table_example'; // string
$id = 'id_example'; // string

try {
    $apiInstance->delete($table, $id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->delete: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table** | **string**|  | |
| **id** | **string**|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteAgent()`

```php
deleteAgent($agent_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$agent_id = 'agent_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->deleteAgent($agent_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteAgent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **agent_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteCategory()`

```php
deleteCategory($category_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$category_id = 'category_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->deleteCategory($category_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteCategory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteDataset()`

```php
deleteDataset($dataset_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$dataset_id = 'dataset_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->deleteDataset($dataset_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteDatasetVersion()`

```php
deleteDatasetVersion($versionset_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$versionset_id = 'versionset_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->deleteDatasetVersion($versionset_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteDatasetVersion: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **versionset_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteProject()`

```php
deleteProject($project_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->deleteProject($project_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteTask()`

```php
deleteTask($project_id, $job_id, $task_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$job_id = 'job_id_example'; // string
$task_id = 'task_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->deleteTask($project_id, $job_id, $task_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteTask: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **task_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `downloadModel()`

```php
downloadModel($provider, $job_id, $x_rapid_api_user, $output_path)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$provider = 'provider_example'; // string
$job_id = 'job_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$output_path = 'output_path_example'; // string

try {
    $apiInstance->downloadModel($provider, $job_id, $x_rapid_api_user, $output_path);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->downloadModel: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
| **job_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |
| **output_path** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `estimateCost()`

```php
estimateCost($provider, $x_rapid_api_user, $training_request_bean)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$provider = 'provider_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$training_request_bean = new \OpenAPI\Client\Model\TrainingRequestBean(); // \OpenAPI\Client\Model\TrainingRequestBean

try {
    $apiInstance->estimateCost($provider, $x_rapid_api_user, $training_request_bean);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->estimateCost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |
| **training_request_bean** | [**\OpenAPI\Client\Model\TrainingRequestBean**](../Model/TrainingRequestBean.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `findAll()`

```php
findAll($table, $page, $page_size)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$table = 'table_example'; // string
$page = 0; // int
$page_size = 50; // int

try {
    $apiInstance->findAll($table, $page, $page_size);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->findAll: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table** | **string**|  | |
| **page** | **int**|  | [optional] [default to 0] |
| **page_size** | **int**|  | [optional] [default to 50] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAgent()`

```php
getAgent($category_id, $agent_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$category_id = 'category_id_example'; // string
$agent_id = 'agent_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getAgent($category_id, $agent_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAgent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |
| **agent_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAgentFromName()`

```php
getAgentFromName($category_id, $agent_name, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$category_id = 'category_id_example'; // string
$agent_name = 'agent_name_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getAgentFromName($category_id, $agent_name, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAgentFromName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |
| **agent_name** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAllAgents()`

```php
getAllAgents($category_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$category_id = 'category_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getAllAgents($category_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllAgents: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAllCategories()`

```php
getAllCategories($x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getAllCategories($x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllCategories: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAllDatasetVersions()`

```php
getAllDatasetVersions($x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getAllDatasetVersions($x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllDatasetVersions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAllDatasets()`

```php
getAllDatasets($x_rapid_api_user, $status)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$status = 'status_example'; // string

try {
    $apiInstance->getAllDatasets($x_rapid_api_user, $status);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllDatasets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |
| **status** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAllProjects()`

```php
getAllProjects($x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getAllProjects($x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllProjects: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAllTasks()`

```php
getAllTasks($project_id, $job_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$job_id = 'job_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getAllTasks($project_id, $job_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllTasks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAllVersionsets()`

```php
getAllVersionsets($dataset_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$dataset_id = 'dataset_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getAllVersionsets($dataset_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllVersionsets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getById()`

```php
getById($table, $id)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$table = 'table_example'; // string
$id = 'id_example'; // string

try {
    $apiInstance->getById($table, $id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table** | **string**|  | |
| **id** | **string**|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCategory()`

```php
getCategory($category_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$category_id = 'category_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getCategory($category_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getCategory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCategoryFromName()`

```php
getCategoryFromName($category_name, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$category_name = 'category_name_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getCategoryFromName($category_name, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getCategoryFromName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_name** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getDataset()`

```php
getDataset($dataset_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$dataset_id = 'dataset_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getDataset($dataset_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getDatasetInputFile()`

```php
getDatasetInputFile($dataset_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$dataset_id = 'dataset_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getDatasetInputFile($dataset_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDatasetInputFile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getDatasetInputFilePagination()`

```php
getDatasetInputFilePagination($offset, $dataset_id, $limit, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$offset = 56; // int
$dataset_id = 'dataset_id_example'; // string
$limit = 56; // int
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getDatasetInputFilePagination($offset, $dataset_id, $limit, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDatasetInputFilePagination: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **offset** | **int**|  | |
| **dataset_id** | **string**|  | |
| **limit** | **int**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getDatasetInputFileSize()`

```php
getDatasetInputFileSize($dataset_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$dataset_id = 'dataset_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getDatasetInputFileSize($dataset_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDatasetInputFileSize: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getDatasetStatus()`

```php
getDatasetStatus($dataset_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$dataset_id = 'dataset_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getDatasetStatus($dataset_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDatasetStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getDatasetVersionInputFile()`

```php
getDatasetVersionInputFile($category_id, $job_id, $versionset_id, $dataset_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$category_id = 'category_id_example'; // string
$job_id = 'job_id_example'; // string
$versionset_id = 'versionset_id_example'; // string
$dataset_id = 'dataset_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getDatasetVersionInputFile($category_id, $job_id, $versionset_id, $dataset_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDatasetVersionInputFile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |
| **job_id** | **string**|  | |
| **versionset_id** | **string**|  | |
| **dataset_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getDatasetVersionInputFilePagination()`

```php
getDatasetVersionInputFilePagination($project_id, $bot_id, $offset, $limit, $versionset_id, $dataset_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$bot_id = 'bot_id_example'; // string
$offset = 56; // int
$limit = 56; // int
$versionset_id = 'versionset_id_example'; // string
$dataset_id = 'dataset_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getDatasetVersionInputFilePagination($project_id, $bot_id, $offset, $limit, $versionset_id, $dataset_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDatasetVersionInputFilePagination: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **bot_id** | **string**|  | |
| **offset** | **int**|  | |
| **limit** | **int**|  | |
| **versionset_id** | **string**|  | |
| **dataset_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getHealth()`

```php
getHealth()
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $apiInstance->getHealth();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getHealth: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getHtml()`

```php
getHtml($protocol, $url)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$protocol = 'protocol_example'; // string
$url = 'url_example'; // string

try {
    $apiInstance->getHtml($protocol, $url);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getHtml: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **protocol** | **string**|  | |
| **url** | **string**|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getProject()`

```php
getProject($project_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getProject($project_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getProjectFromName()`

```php
getProjectFromName($project_name, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_name = 'project_name_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getProjectFromName($project_name, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getProjectFromName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_name** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getProjectJobs()`

```php
getProjectJobs($project_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getProjectJobs($project_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getProjectJobs: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getProjectSchedule()`

```php
getProjectSchedule($project_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getProjectSchedule($project_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getProjectSchedule: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getSupportedModels()`

```php
getSupportedModels($provider, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$provider = 'provider_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getSupportedModels($provider, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getSupportedModels: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getSupportedProviders()`

```php
getSupportedProviders($x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getSupportedProviders($x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getSupportedProviders: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getTask()`

```php
getTask($project_id, $job_id, $task_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$job_id = 'job_id_example'; // string
$task_id = 'task_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getTask($project_id, $job_id, $task_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getTask: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **task_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getTaskStatus()`

```php
getTaskStatus($project_id, $job_id, $task_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$job_id = 'job_id_example'; // string
$task_id = 'task_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getTaskStatus($project_id, $job_id, $task_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getTaskStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **task_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getTrainingLogs()`

```php
getTrainingLogs($provider, $job_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$provider = 'provider_example'; // string
$job_id = 'job_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getTrainingLogs($provider, $job_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getTrainingLogs: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
| **job_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getTrainingStatus()`

```php
getTrainingStatus($provider, $job_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$provider = 'provider_example'; // string
$job_id = 'job_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getTrainingStatus($provider, $job_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getTrainingStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
| **job_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getUploadFileUrl()`

```php
getUploadFileUrl($project_id, $bot_id, $attachment_name, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$bot_id = 'bot_id_example'; // string
$attachment_name = 'attachment_name_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getUploadFileUrl($project_id, $bot_id, $attachment_name, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getUploadFileUrl: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **bot_id** | **string**|  | |
| **attachment_name** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getUrlDownload()`

```php
getUrlDownload($x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getUrlDownload($x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getUrlDownload: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getUrlUpload()`

```php
getUrlUpload($x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getUrlUpload($x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getUrlUpload: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getVersionset()`

```php
getVersionset($versionset_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$versionset_id = 'versionset_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getVersionset($versionset_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getVersionset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **versionset_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getVersionsetFromVersion()`

```php
getVersionsetFromVersion($dataset_id, $version, $x_rapid_api_user, $time_period)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$dataset_id = 'dataset_id_example'; // string
$version = 'version_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$time_period = new \OpenAPI\Client\Model\TimePeriod(); // \OpenAPI\Client\Model\TimePeriod

try {
    $apiInstance->getVersionsetFromVersion($dataset_id, $version, $x_rapid_api_user, $time_period);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getVersionsetFromVersion: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |
| **version** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |
| **time_period** | [**\OpenAPI\Client\Model\TimePeriod**](../Model/TimePeriod.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getVersionsetFromVersionBase()`

```php
getVersionsetFromVersionBase($dataset_id, $version, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$dataset_id = 'dataset_id_example'; // string
$version = 'version_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->getVersionsetFromVersionBase($dataset_id, $version, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getVersionsetFromVersionBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |
| **version** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `insert()`

```php
insert($table, $request_body)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$table = 'table_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->insert($table, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->insert: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table** | **string**|  | |
| **request_body** | [**array<string,object>**](../Model/object.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `publishModel()`

```php
publishModel($x_rapid_api_user, $model_publish_request)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$model_publish_request = new \OpenAPI\Client\Model\ModelPublishRequest(); // \OpenAPI\Client\Model\ModelPublishRequest

try {
    $apiInstance->publishModel($x_rapid_api_user, $model_publish_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->publishModel: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |
| **model_publish_request** | [**\OpenAPI\Client\Model\ModelPublishRequest**](../Model/ModelPublishRequest.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `removeJobFromProject()`

```php
removeJobFromProject($project_id, $job_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$job_id = 'job_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->removeJobFromProject($project_id, $job_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->removeJobFromProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `setProjectSchedule()`

```php
setProjectSchedule($project_id, $x_rapid_api_user, $project_schedule_request)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$project_schedule_request = new \OpenAPI\Client\Model\ProjectScheduleRequest(); // \OpenAPI\Client\Model\ProjectScheduleRequest

try {
    $apiInstance->setProjectSchedule($project_id, $x_rapid_api_user, $project_schedule_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->setProjectSchedule: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |
| **project_schedule_request** | [**\OpenAPI\Client\Model\ProjectScheduleRequest**](../Model/ProjectScheduleRequest.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `startExportAll()`

```php
startExportAll($x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->startExportAll($x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startExportAll: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `startExportProject()`

```php
startExportProject($project_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->startExportProject($project_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startExportProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `startImportAll()`

```php
startImportAll($x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->startImportAll($x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startImportAll: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `startImportProject()`

```php
startImportProject($project_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->startImportProject($project_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startImportProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `startTask()`

```php
startTask($project_id, $job_id, $task_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$job_id = 'job_id_example'; // string
$task_id = 'task_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->startTask($project_id, $job_id, $task_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startTask: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **task_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `startTraining()`

```php
startTraining($provider, $x_rapid_api_user, $training_request_bean)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$provider = 'provider_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$training_request_bean = new \OpenAPI\Client\Model\TrainingRequestBean(); // \OpenAPI\Client\Model\TrainingRequestBean

try {
    $apiInstance->startTraining($provider, $x_rapid_api_user, $training_request_bean);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startTraining: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |
| **training_request_bean** | [**\OpenAPI\Client\Model\TrainingRequestBean**](../Model/TrainingRequestBean.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `stopTask()`

```php
stopTask($project_id, $job_id, $task_id, $x_rapid_api_user)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$job_id = 'job_id_example'; // string
$task_id = 'task_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string

try {
    $apiInstance->stopTask($project_id, $job_id, $task_id, $x_rapid_api_user);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->stopTask: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **task_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `test()`

```php
test()
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $apiInstance->test();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->test: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `test1()`

```php
test1()
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $apiInstance->test1();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->test1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `update()`

```php
update($table, $id, $request_body)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$table = 'table_example'; // string
$id = 'id_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->update($table, $id, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->update: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **table** | **string**|  | |
| **id** | **string**|  | |
| **request_body** | [**array<string,object>**](../Model/object.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateAgent()`

```php
updateAgent($category_id, $agent_id, $x_rapid_api_user, $agent_dto)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$category_id = 'category_id_example'; // string
$agent_id = 'agent_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$agent_dto = new \OpenAPI\Client\Model\AgentDto(); // \OpenAPI\Client\Model\AgentDto

try {
    $apiInstance->updateAgent($category_id, $agent_id, $x_rapid_api_user, $agent_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateAgent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |
| **agent_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |
| **agent_dto** | [**\OpenAPI\Client\Model\AgentDto**](../Model/AgentDto.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateCategory()`

```php
updateCategory($category_id, $x_rapid_api_user, $job_category_dto)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$category_id = 'category_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$job_category_dto = new \OpenAPI\Client\Model\JobCategoryDto(); // \OpenAPI\Client\Model\JobCategoryDto

try {
    $apiInstance->updateCategory($category_id, $x_rapid_api_user, $job_category_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateCategory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |
| **job_category_dto** | [**\OpenAPI\Client\Model\JobCategoryDto**](../Model/JobCategoryDto.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateProject()`

```php
updateProject($project_id, $x_rapid_api_user, $job_project_dto)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$job_project_dto = new \OpenAPI\Client\Model\JobProjectDto(); // \OpenAPI\Client\Model\JobProjectDto

try {
    $apiInstance->updateProject($project_id, $x_rapid_api_user, $job_project_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |
| **job_project_dto** | [**\OpenAPI\Client\Model\JobProjectDto**](../Model/JobProjectDto.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateTask()`

```php
updateTask($project_id, $job_id, $task_id, $x_rapid_api_user, $task_dto)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$project_id = 'project_id_example'; // string
$job_id = 'job_id_example'; // string
$task_id = 'task_id_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$task_dto = new \OpenAPI\Client\Model\TaskDto(); // \OpenAPI\Client\Model\TaskDto

try {
    $apiInstance->updateTask($project_id, $job_id, $task_id, $x_rapid_api_user, $task_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateTask: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **task_id** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |
| **task_dto** | [**\OpenAPI\Client\Model\TaskDto**](../Model/TaskDto.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `uploadDataset()`

```php
uploadDataset($provider, $x_rapid_api_user, $dataset_upload_request)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$provider = 'provider_example'; // string
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$dataset_upload_request = new \OpenAPI\Client\Model\DatasetUploadRequest(); // \OpenAPI\Client\Model\DatasetUploadRequest

try {
    $apiInstance->uploadDataset($provider, $x_rapid_api_user, $dataset_upload_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->uploadDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
| **x_rapid_api_user** | **string**|  | [optional] |
| **dataset_upload_request** | [**\OpenAPI\Client\Model\DatasetUploadRequest**](../Model/DatasetUploadRequest.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `uploadDataset1()`

```php
uploadDataset1($x_rapid_api_user, $dataset_upload_api_dto)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_rapid_api_user = 'x_rapid_api_user_example'; // string
$dataset_upload_api_dto = new \OpenAPI\Client\Model\DatasetUploadApiDto(); // \OpenAPI\Client\Model\DatasetUploadApiDto

try {
    $apiInstance->uploadDataset1($x_rapid_api_user, $dataset_upload_api_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->uploadDataset1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **x_rapid_api_user** | **string**|  | [optional] |
| **dataset_upload_api_dto** | [**\OpenAPI\Client\Model\DatasetUploadApiDto**](../Model/DatasetUploadApiDto.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
