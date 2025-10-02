# webrobot

OpenAPI


## Installation & Usage

### Requirements

PHP 8.1 and later.

### Composer

To install the bindings via [Composer](https://getcomposer.org/), add the following to `composer.json`:

```json
{
  "repositories": [
    {
      "type": "vcs",
      "url": "https://github.com/GIT_USER_ID/GIT_REPO_ID.git"
    }
  ],
  "require": {
    "GIT_USER_ID/GIT_REPO_ID": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
<?php
require_once('/path/to/webrobot/vendor/autoload.php');
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**addJobToProject**](docs/Api/DefaultApi.md#addjobtoproject) | **POST** /webrobot/api/projects/id/{projectId}/jobs | 
*DefaultApi* | [**cancelTraining**](docs/Api/DefaultApi.md#canceltraining) | **DELETE** /webrobot/api/ai-providers/providers/{provider}/training/{jobId} | 
*DefaultApi* | [**createAgent**](docs/Api/DefaultApi.md#createagent) | **POST** /webrobot/api/agents | 
*DefaultApi* | [**createCategory**](docs/Api/DefaultApi.md#createcategory) | **POST** /webrobot/api/categories | 
*DefaultApi* | [**createProject**](docs/Api/DefaultApi.md#createproject) | **POST** /webrobot/api/projects | 
*DefaultApi* | [**createTask**](docs/Api/DefaultApi.md#createtask) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks | 
*DefaultApi* | [**delete**](docs/Api/DefaultApi.md#delete) | **DELETE** /api/strapi-tables/{table}/{id} | 
*DefaultApi* | [**deleteAgent**](docs/Api/DefaultApi.md#deleteagent) | **DELETE** /webrobot/api/agents/{agentId} | 
*DefaultApi* | [**deleteCategory**](docs/Api/DefaultApi.md#deletecategory) | **DELETE** /webrobot/api/categories/id/{categoryId} | 
*DefaultApi* | [**deleteDataset**](docs/Api/DefaultApi.md#deletedataset) | **DELETE** /webrobot/api/datasets/{projectId}/{botId}/{datasetId} | 
*DefaultApi* | [**deleteDatasetVersion**](docs/Api/DefaultApi.md#deletedatasetversion) | **DELETE** /webrobot/api/datasets/version/id/{versionsetId} | 
*DefaultApi* | [**deleteProject**](docs/Api/DefaultApi.md#deleteproject) | **DELETE** /webrobot/api/projects/id/{projectId} | 
*DefaultApi* | [**deleteTask**](docs/Api/DefaultApi.md#deletetask) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
*DefaultApi* | [**downloadModel**](docs/Api/DefaultApi.md#downloadmodel) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/download | 
*DefaultApi* | [**estimateCost**](docs/Api/DefaultApi.md#estimatecost) | **POST** /webrobot/api/ai-providers/providers/{provider}/cost-estimate | 
*DefaultApi* | [**findAll**](docs/Api/DefaultApi.md#findall) | **GET** /api/strapi-tables/{table} | 
*DefaultApi* | [**getAgent**](docs/Api/DefaultApi.md#getagent) | **GET** /webrobot/api/agents/{categoryId}/{agentId} | 
*DefaultApi* | [**getAgentFromName**](docs/Api/DefaultApi.md#getagentfromname) | **GET** /webrobot/api/agents/{categoryId}/name/{agentName} | 
*DefaultApi* | [**getAllAgents**](docs/Api/DefaultApi.md#getallagents) | **GET** /webrobot/api/agents/{categoryId} | 
*DefaultApi* | [**getAllCategories**](docs/Api/DefaultApi.md#getallcategories) | **GET** /webrobot/api/categories | 
*DefaultApi* | [**getAllDatasetVersions**](docs/Api/DefaultApi.md#getalldatasetversions) | **GET** /webrobot/api/datasets/{projectId}/{botId}/versions | 
*DefaultApi* | [**getAllDatasets**](docs/Api/DefaultApi.md#getalldatasets) | **GET** /webrobot/api/datasets/datasets | 
*DefaultApi* | [**getAllProjects**](docs/Api/DefaultApi.md#getallprojects) | **GET** /webrobot/api/projects | 
*DefaultApi* | [**getAllTasks**](docs/Api/DefaultApi.md#getalltasks) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks | 
*DefaultApi* | [**getAllVersionsets**](docs/Api/DefaultApi.md#getallversionsets) | **GET** /webrobot/api/datasets/{datasetId}/versions | 
*DefaultApi* | [**getById**](docs/Api/DefaultApi.md#getbyid) | **GET** /api/strapi-tables/{table}/{id} | 
*DefaultApi* | [**getCategory**](docs/Api/DefaultApi.md#getcategory) | **GET** /webrobot/api/categories/id/{categoryId} | 
*DefaultApi* | [**getCategoryFromName**](docs/Api/DefaultApi.md#getcategoryfromname) | **GET** /webrobot/api/categories/{categoryName} | 
*DefaultApi* | [**getDataset**](docs/Api/DefaultApi.md#getdataset) | **GET** /webrobot/api/datasets/{projectId}/{botId}/{datasetId} | 
*DefaultApi* | [**getDatasetInputFile**](docs/Api/DefaultApi.md#getdatasetinputfile) | **GET** /webrobot/api/datasets/{projectId}/{botId}/{datasetId}/input/url | 
*DefaultApi* | [**getDatasetInputFilePagination**](docs/Api/DefaultApi.md#getdatasetinputfilepagination) | **GET** /webrobot/api/datasets/{projectId}/{botId}/{datasetId}/input/{offset}/{limit} | 
*DefaultApi* | [**getDatasetInputFileSize**](docs/Api/DefaultApi.md#getdatasetinputfilesize) | **GET** /webrobot/api/datasets/{datasetId}/input/size | 
*DefaultApi* | [**getDatasetStatus**](docs/Api/DefaultApi.md#getdatasetstatus) | **GET** /webrobot/api/datasets/datasets/{datasetId}/status | 
*DefaultApi* | [**getDatasetVersionInputFile**](docs/Api/DefaultApi.md#getdatasetversioninputfile) | **GET** /webrobot/api/datasets/{categoryId}/{jobId}/{datasetId}/versions/{versionsetId}/input/url | 
*DefaultApi* | [**getDatasetVersionInputFilePagination**](docs/Api/DefaultApi.md#getdatasetversioninputfilepagination) | **GET** /webrobot/api/datasets/{datasetId}/versions/{versionsetId}/input/{offset}/{limit} | 
*DefaultApi* | [**getHealth**](docs/Api/DefaultApi.md#gethealth) | **GET** /health | 
*DefaultApi* | [**getHtml**](docs/Api/DefaultApi.md#gethtml) | **GET** /webrobot/api/html/{url}/{protocol} | 
*DefaultApi* | [**getProject**](docs/Api/DefaultApi.md#getproject) | **GET** /webrobot/api/projects/id/{projectId} | 
*DefaultApi* | [**getProjectFromName**](docs/Api/DefaultApi.md#getprojectfromname) | **GET** /webrobot/api/projects/{projectName} | 
*DefaultApi* | [**getProjectJobs**](docs/Api/DefaultApi.md#getprojectjobs) | **GET** /webrobot/api/projects/id/{projectId}/jobs | 
*DefaultApi* | [**getProjectSchedule**](docs/Api/DefaultApi.md#getprojectschedule) | **GET** /webrobot/api/projects/id/{projectId}/schedule | 
*DefaultApi* | [**getSupportedModels**](docs/Api/DefaultApi.md#getsupportedmodels) | **GET** /webrobot/api/ai-providers/providers/{provider}/models | 
*DefaultApi* | [**getSupportedProviders**](docs/Api/DefaultApi.md#getsupportedproviders) | **GET** /webrobot/api/ai-providers/providers | 
*DefaultApi* | [**getTask**](docs/Api/DefaultApi.md#gettask) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
*DefaultApi* | [**getTaskStatus**](docs/Api/DefaultApi.md#gettaskstatus) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/status | 
*DefaultApi* | [**getTrainingLogs**](docs/Api/DefaultApi.md#gettraininglogs) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/logs | 
*DefaultApi* | [**getTrainingStatus**](docs/Api/DefaultApi.md#gettrainingstatus) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/status | 
*DefaultApi* | [**getUploadFileUrl**](docs/Api/DefaultApi.md#getuploadfileurl) | **GET** /webrobot/api/datasets/{categoryId}/{jobId}/upload/{attachmentName} | 
*DefaultApi* | [**getUrlDownload**](docs/Api/DefaultApi.md#geturldownload) | **GET** /webrobot/api/package/download | 
*DefaultApi* | [**getUrlUpload**](docs/Api/DefaultApi.md#geturlupload) | **GET** /webrobot/api/package/upload | 
*DefaultApi* | [**getVersionset**](docs/Api/DefaultApi.md#getversionset) | **GET** /webrobot/api/datasets/version/id/{versionsetId} | 
*DefaultApi* | [**getVersionsetFromVersion**](docs/Api/DefaultApi.md#getversionsetfromversion) | **POST** /webrobot/api/datasets/{datasetId}/versions/version/{version} | 
*DefaultApi* | [**getVersionsetFromVersionBase**](docs/Api/DefaultApi.md#getversionsetfromversionbase) | **GET** /webrobot/api/datasets/{datasetId}/versions/version/{version}/base | 
*DefaultApi* | [**insert**](docs/Api/DefaultApi.md#insert) | **POST** /api/strapi-tables/{table} | 
*DefaultApi* | [**publishModel**](docs/Api/DefaultApi.md#publishmodel) | **POST** /webrobot/api/ai-providers/providers/huggingface/models/publish | 
*DefaultApi* | [**removeJobFromProject**](docs/Api/DefaultApi.md#removejobfromproject) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId} | 
*DefaultApi* | [**setProjectSchedule**](docs/Api/DefaultApi.md#setprojectschedule) | **PUT** /webrobot/api/projects/id/{projectId}/schedule | 
*DefaultApi* | [**startExportAll**](docs/Api/DefaultApi.md#startexportall) | **GET** /webrobot/api/package/export/all | 
*DefaultApi* | [**startExportProject**](docs/Api/DefaultApi.md#startexportproject) | **GET** /webrobot/api/package/export/id/{projectId} | 
*DefaultApi* | [**startImportAll**](docs/Api/DefaultApi.md#startimportall) | **GET** /webrobot/api/package/import/all | 
*DefaultApi* | [**startImportProject**](docs/Api/DefaultApi.md#startimportproject) | **GET** /webrobot/api/package/import/id/{projectId} | 
*DefaultApi* | [**startTask**](docs/Api/DefaultApi.md#starttask) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/start | 
*DefaultApi* | [**startTraining**](docs/Api/DefaultApi.md#starttraining) | **POST** /webrobot/api/ai-providers/providers/{provider}/training | 
*DefaultApi* | [**stopTask**](docs/Api/DefaultApi.md#stoptask) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/stop | 
*DefaultApi* | [**test**](docs/Api/DefaultApi.md#test) | **GET** /webrobot/api/categories/test | 
*DefaultApi* | [**test1**](docs/Api/DefaultApi.md#test1) | **GET** /webrobot/api/projects/test | 
*DefaultApi* | [**update**](docs/Api/DefaultApi.md#update) | **PUT** /api/strapi-tables/{table}/{id} | 
*DefaultApi* | [**updateAgent**](docs/Api/DefaultApi.md#updateagent) | **PUT** /webrobot/api/agents/{categoryId}/{agentId} | 
*DefaultApi* | [**updateCategory**](docs/Api/DefaultApi.md#updatecategory) | **PUT** /webrobot/api/categories/id/{categoryId} | 
*DefaultApi* | [**updateProject**](docs/Api/DefaultApi.md#updateproject) | **PUT** /webrobot/api/projects/id/{projectId} | 
*DefaultApi* | [**updateTask**](docs/Api/DefaultApi.md#updatetask) | **PUT** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
*DefaultApi* | [**uploadDataset**](docs/Api/DefaultApi.md#uploaddataset) | **POST** /webrobot/api/ai-providers/providers/{provider}/datasets | 
*DefaultApi* | [**uploadDataset1**](docs/Api/DefaultApi.md#uploaddataset1) | **POST** /webrobot/api/datasets/{projectId}/{botId} | 

## Models

- [AgentDto](docs/Model/AgentDto.md)
- [DatasetUploadApiDto](docs/Model/DatasetUploadApiDto.md)
- [DatasetUploadRequest](docs/Model/DatasetUploadRequest.md)
- [JobCategoryDto](docs/Model/JobCategoryDto.md)
- [JobDto](docs/Model/JobDto.md)
- [JobProjectDto](docs/Model/JobProjectDto.md)
- [ModelPublishRequest](docs/Model/ModelPublishRequest.md)
- [ProjectScheduleRequest](docs/Model/ProjectScheduleRequest.md)
- [TaskDto](docs/Model/TaskDto.md)
- [TimePeriod](docs/Model/TimePeriod.md)
- [TrainingRequestBean](docs/Model/TrainingRequestBean.md)

## Authorization
Endpoints do not require authorization.

## Tests

To run the tests, use:

```bash
composer install
vendor/bin/phpunit
```

## Author



## About this package

This PHP package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `0.0.1`
    - Generator version: `7.17.0-SNAPSHOT`
- Build package: `org.openapitools.codegen.languages.PhpClientCodegen`
