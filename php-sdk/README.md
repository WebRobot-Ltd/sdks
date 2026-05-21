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
$job_dto = new \OpenAPI\Client\Model\JobDto(); // \OpenAPI\Client\Model\JobDto

try {
    $apiInstance->addJobToProject($project_id, $job_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->addJobToProject: ', $e->getMessage(), PHP_EOL;
}

```

## API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**addJobToProject**](docs/Api/DefaultApi.md#addjobtoproject) | **POST** /webrobot/api/projects/id/{projectId}/jobs | 
*DefaultApi* | [**apply**](docs/Api/DefaultApi.md#apply) | **POST** /webrobot/api/manifest/apply | 
*DefaultApi* | [**applyMigrations**](docs/Api/DefaultApi.md#applymigrations) | **POST** /webrobot/api/admin/bundles/{id}/apply-migrations | 
*DefaultApi* | [**approveBundle**](docs/Api/DefaultApi.md#approvebundle) | **POST** /webrobot/api/admin/bundles/{id}/approve | 
*DefaultApi* | [**assignUserToOrganization**](docs/Api/DefaultApi.md#assignusertoorganization) | **POST** /webrobot/api/auth/organizations/{id}/assign-user | 
*DefaultApi* | [**bootstrapForOrganization**](docs/Api/DefaultApi.md#bootstrapfororganization) | **POST** /webrobot/api/ean-image-sourcing/bootstrap/organization/{organizationId} | 
*DefaultApi* | [**cancel**](docs/Api/DefaultApi.md#cancel) | **DELETE** /webrobot/api/agentic/{eid} | 
*DefaultApi* | [**cancelExecution**](docs/Api/DefaultApi.md#cancelexecution) | **DELETE** /webrobot/api/demo/executions/{executionId} | 
*DefaultApi* | [**cancelExecution1**](docs/Api/DefaultApi.md#cancelexecution1) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/executions/{executionId} | 
*DefaultApi* | [**cancelTraining**](docs/Api/DefaultApi.md#canceltraining) | **DELETE** /webrobot/api/ai-providers/providers/{provider}/training/{jobId} | 
*DefaultApi* | [**cmfClose**](docs/Api/DefaultApi.md#cmfclose) | **DELETE** /webrobot/api/demo/wizard/cmf/{sessionId} | 
*DefaultApi* | [**cmfOpen**](docs/Api/DefaultApi.md#cmfopen) | **POST** /webrobot/api/demo/wizard/cmf/open | 
*DefaultApi* | [**cmfStep**](docs/Api/DefaultApi.md#cmfstep) | **POST** /webrobot/api/demo/wizard/cmf/step | 
*DefaultApi* | [**completion**](docs/Api/DefaultApi.md#completion) | **POST** /webrobot/api/agentic/{eid}/completion | 
*DefaultApi* | [**copyAgent**](docs/Api/DefaultApi.md#copyagent) | **POST** /webrobot/api/agents/{agentId}/copy | 
*DefaultApi* | [**createAgent**](docs/Api/DefaultApi.md#createagent) | **POST** /webrobot/api/agents | 
*DefaultApi* | [**createApiKey**](docs/Api/DefaultApi.md#createapikey) | **POST** /webrobot/api/auth/api-keys | 
*DefaultApi* | [**createBillingPlan**](docs/Api/DefaultApi.md#createbillingplan) | **POST** /webrobot/api/billing/plans | 
*DefaultApi* | [**createCategory**](docs/Api/DefaultApi.md#createcategory) | **POST** /webrobot/api/categories | 
*DefaultApi* | [**createCloudCredential**](docs/Api/DefaultApi.md#createcloudcredential) | **POST** /webrobot/api/cloud-credentials | 
*DefaultApi* | [**createCronJob**](docs/Api/DefaultApi.md#createcronjob) | **POST** /webrobot/cloud/scheduler/cronjobs | 
*DefaultApi* | [**createCustomPlan**](docs/Api/DefaultApi.md#createcustomplan) | **POST** /webrobot/api/billing/custom-plan | 
*DefaultApi* | [**createDataset**](docs/Api/DefaultApi.md#createdataset) | **POST** /webrobot/api/datasets | 
*DefaultApi* | [**createOrUpdateVersion**](docs/Api/DefaultApi.md#createorupdateversion) | **POST** /webrobot/api/admin/etl-library-versions | 
*DefaultApi* | [**createOrganization**](docs/Api/DefaultApi.md#createorganization) | **POST** /webrobot/api/auth/organizations | 
*DefaultApi* | [**createProfile**](docs/Api/DefaultApi.md#createprofile) | **POST** /webrobot/api/agentic/profiles | 
*DefaultApi* | [**createProject**](docs/Api/DefaultApi.md#createproject) | **POST** /webrobot/api/projects | 
*DefaultApi* | [**createTask**](docs/Api/DefaultApi.md#createtask) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks | 
*DefaultApi* | [**decryptField**](docs/Api/DefaultApi.md#decryptfield) | **POST** /webrobot/api/cloud-credentials/id/{credentialId}/decrypt-field | 
*DefaultApi* | [**delete**](docs/Api/DefaultApi.md#delete) | **DELETE** /api/strapi-tables/{table}/{id} | 
*DefaultApi* | [**deleteAgent**](docs/Api/DefaultApi.md#deleteagent) | **DELETE** /webrobot/api/agents/{agentId} | 
*DefaultApi* | [**deleteApiKey**](docs/Api/DefaultApi.md#deleteapikey) | **DELETE** /webrobot/api/auth/api-keys/{key_id} | 
*DefaultApi* | [**deleteBillingPlan**](docs/Api/DefaultApi.md#deletebillingplan) | **DELETE** /webrobot/api/billing/plans/{id} | 
*DefaultApi* | [**deleteCategory**](docs/Api/DefaultApi.md#deletecategory) | **DELETE** /webrobot/api/categories/id/{categoryId} | 
*DefaultApi* | [**deleteCloudCredential**](docs/Api/DefaultApi.md#deletecloudcredential) | **DELETE** /webrobot/api/cloud-credentials/id/{credentialId} | 
*DefaultApi* | [**deleteCronJob**](docs/Api/DefaultApi.md#deletecronjob) | **DELETE** /webrobot/cloud/scheduler/cronjobs/{name} | 
*DefaultApi* | [**deleteDataset**](docs/Api/DefaultApi.md#deletedataset) | **DELETE** /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId} | 
*DefaultApi* | [**deleteDataset1**](docs/Api/DefaultApi.md#deletedataset1) | **DELETE** /webrobot/api/datasets/{datasetId} | 
*DefaultApi* | [**deleteDatasetVersion**](docs/Api/DefaultApi.md#deletedatasetversion) | **DELETE** /webrobot/api/datasets-legacy/version/id/{versionsetId} | 
*DefaultApi* | [**deleteInstallation**](docs/Api/DefaultApi.md#deleteinstallation) | **DELETE** /webrobot/api/admin/plugin-installations/{id} | 
*DefaultApi* | [**deleteProfile**](docs/Api/DefaultApi.md#deleteprofile) | **DELETE** /webrobot/api/agentic/profiles/{id} | 
*DefaultApi* | [**deleteProject**](docs/Api/DefaultApi.md#deleteproject) | **DELETE** /webrobot/api/projects/id/{projectId} | 
*DefaultApi* | [**deletePythonExtension**](docs/Api/DefaultApi.md#deletepythonextension) | **DELETE** /webrobot/api/python-extensions/python-extensions/{extensionId} | 
*DefaultApi* | [**deleteTask**](docs/Api/DefaultApi.md#deletetask) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
*DefaultApi* | [**deleteUserInvite**](docs/Api/DefaultApi.md#deleteuserinvite) | **DELETE** /webrobot/api/auth/user-invites/{id} | 
*DefaultApi* | [**deleteVersion**](docs/Api/DefaultApi.md#deleteversion) | **DELETE** /webrobot/api/admin/etl-library-versions/id/{id} | 
*DefaultApi* | [**deprecateBundle**](docs/Api/DefaultApi.md#deprecatebundle) | **POST** /webrobot/api/admin/bundles/{id}/deprecate | 
*DefaultApi* | [**disablePlugin**](docs/Api/DefaultApi.md#disableplugin) | **POST** /webrobot/api/admin/plugins/{pluginId}/disable | 
*DefaultApi* | [**disablePlugin1**](docs/Api/DefaultApi.md#disableplugin1) | **POST** /webrobot/api/admin/plugin-installations/{id}/disable | 
*DefaultApi* | [**disablePluginForOrganization**](docs/Api/DefaultApi.md#disablepluginfororganization) | **POST** /webrobot/api/admin/plugin-installations/{pluginInstallationId}/organizations/{organizationId}/disable | 
*DefaultApi* | [**downloadBundle**](docs/Api/DefaultApi.md#downloadbundle) | **GET** /webrobot/api/admin/bundles/{id}/download | 
*DefaultApi* | [**downloadCliPlugin**](docs/Api/DefaultApi.md#downloadcliplugin) | **GET** /webrobot/api/admin/bundles/cli-plugins/{pluginId} | 
*DefaultApi* | [**downloadModel**](docs/Api/DefaultApi.md#downloadmodel) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/download | 
*DefaultApi* | [**downloadUiZip**](docs/Api/DefaultApi.md#downloaduizip) | **GET** /webrobot/api/admin/plugin-installations/{pluginId}/ui/download | 
*DefaultApi* | [**enableByPluginIdForOrganization**](docs/Api/DefaultApi.md#enablebypluginidfororganization) | **POST** /webrobot/api/admin/plugin-installations/by-plugin-id/{pluginId}/organizations/{organizationId}/enable | 
*DefaultApi* | [**enablePlugin**](docs/Api/DefaultApi.md#enableplugin) | **POST** /webrobot/api/admin/plugins/{pluginId}/enable | 
*DefaultApi* | [**enablePlugin1**](docs/Api/DefaultApi.md#enableplugin1) | **POST** /webrobot/api/admin/plugin-installations/{id}/enable | 
*DefaultApi* | [**enablePluginForOrganization**](docs/Api/DefaultApi.md#enablepluginfororganization) | **POST** /webrobot/api/admin/plugin-installations/{pluginInstallationId}/organizations/{organizationId}/enable | 
*DefaultApi* | [**estimateCost**](docs/Api/DefaultApi.md#estimatecost) | **POST** /webrobot/api/ai-providers/providers/{provider}/cost-estimate | 
*DefaultApi* | [**executeDemo**](docs/Api/DefaultApi.md#executedemo) | **POST** /webrobot/api/demo/execute/{pipeline-name} | 
*DefaultApi* | [**executeJob**](docs/Api/DefaultApi.md#executejob) | **POST** /webrobot/api/ean-image-sourcing/{country}/execute | 
*DefaultApi* | [**executeJob1**](docs/Api/DefaultApi.md#executejob1) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/execute | 
*DefaultApi* | [**executeQuery**](docs/Api/DefaultApi.md#executequery) | **POST** /webrobot/api/datasets/query | 
*DefaultApi* | [**extractDirect**](docs/Api/DefaultApi.md#extractdirect) | **POST** /webrobot/api/extract/direct | 
*DefaultApi* | [**findAll**](docs/Api/DefaultApi.md#findall) | **GET** /api/strapi-tables/{table} | 
*DefaultApi* | [**generatePipeline**](docs/Api/DefaultApi.md#generatepipeline) | **POST** /webrobot/api/demo/generate-pipeline | 
*DefaultApi* | [**generatePysparkCode**](docs/Api/DefaultApi.md#generatepysparkcode) | **POST** /webrobot/api/python-extensions/python-extensions/{extensionId}/generate-pyspark | 
*DefaultApi* | [**getAgent**](docs/Api/DefaultApi.md#getagent) | **GET** /webrobot/api/agents/{categoryId}/{agentId} | 
*DefaultApi* | [**getAgentExtensions**](docs/Api/DefaultApi.md#getagentextensions) | **GET** /webrobot/api/python-extensions/agents/{agentId}/extensions | 
*DefaultApi* | [**getAgentFromName**](docs/Api/DefaultApi.md#getagentfromname) | **GET** /webrobot/api/agents/{categoryId}/name/{agentName} | 
*DefaultApi* | [**getAgentPythonExtensions**](docs/Api/DefaultApi.md#getagentpythonextensions) | **GET** /webrobot/api/python-extensions/agents/{agentId}/python-extensions | 
*DefaultApi* | [**getAllAgents**](docs/Api/DefaultApi.md#getallagents) | **GET** /webrobot/api/agents/{categoryId} | 
*DefaultApi* | [**getAllCategories**](docs/Api/DefaultApi.md#getallcategories) | **GET** /webrobot/api/categories | 
*DefaultApi* | [**getAllCloudCredentials**](docs/Api/DefaultApi.md#getallcloudcredentials) | **GET** /webrobot/api/cloud-credentials | 
*DefaultApi* | [**getAllDatasetVersions**](docs/Api/DefaultApi.md#getalldatasetversions) | **GET** /webrobot/api/datasets-legacy/{projectId}/{botId}/versions | 
*DefaultApi* | [**getAllDatasets**](docs/Api/DefaultApi.md#getalldatasets) | **GET** /webrobot/api/datasets-legacy/datasets | 
*DefaultApi* | [**getAllDatasets1**](docs/Api/DefaultApi.md#getalldatasets1) | **GET** /webrobot/api/datasets | 
*DefaultApi* | [**getAllInstallations**](docs/Api/DefaultApi.md#getallinstallations) | **GET** /webrobot/api/admin/plugin-installations | 
*DefaultApi* | [**getAllProjects**](docs/Api/DefaultApi.md#getallprojects) | **GET** /webrobot/api/projects | 
*DefaultApi* | [**getAllTasks**](docs/Api/DefaultApi.md#getalltasks) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks | 
*DefaultApi* | [**getAllVersions**](docs/Api/DefaultApi.md#getallversions) | **GET** /webrobot/api/admin/etl-library-versions | 
*DefaultApi* | [**getAllVersionsets**](docs/Api/DefaultApi.md#getallversionsets) | **GET** /webrobot/api/datasets-legacy/{datasetId}/versions | 
*DefaultApi* | [**getBillingPlans**](docs/Api/DefaultApi.md#getbillingplans) | **GET** /webrobot/api/billing/plans | 
*DefaultApi* | [**getBootstrapStatus**](docs/Api/DefaultApi.md#getbootstrapstatus) | **GET** /webrobot/api/ean-image-sourcing/bootstrap/status | 
*DefaultApi* | [**getBundleScan**](docs/Api/DefaultApi.md#getbundlescan) | **GET** /webrobot/api/admin/bundles/{id}/scan | 
*DefaultApi* | [**getById**](docs/Api/DefaultApi.md#getbyid) | **GET** /api/strapi-tables/{table}/{id} | 
*DefaultApi* | [**getCapabilities**](docs/Api/DefaultApi.md#getcapabilities) | **GET** /webrobot/cloud/spark/capabilities | 
*DefaultApi* | [**getCatalogStages**](docs/Api/DefaultApi.md#getcatalogstages) | **GET** /webrobot/api/demo/catalog/stages | 
*DefaultApi* | [**getCategory**](docs/Api/DefaultApi.md#getcategory) | **GET** /webrobot/api/categories/id/{categoryId} | 
*DefaultApi* | [**getCategoryFromName**](docs/Api/DefaultApi.md#getcategoryfromname) | **GET** /webrobot/api/categories/{categoryName} | 
*DefaultApi* | [**getCloudCredentialById**](docs/Api/DefaultApi.md#getcloudcredentialbyid) | **GET** /webrobot/api/cloud-credentials/id/{credentialId} | 
*DefaultApi* | [**getCloudCredentialsByProvider**](docs/Api/DefaultApi.md#getcloudcredentialsbyprovider) | **GET** /webrobot/api/cloud-credentials/provider/{provider} | 
*DefaultApi* | [**getCronJob**](docs/Api/DefaultApi.md#getcronjob) | **GET** /webrobot/cloud/scheduler/cronjobs/{name} | 
*DefaultApi* | [**getCurrentUser**](docs/Api/DefaultApi.md#getcurrentuser) | **GET** /webrobot/api/auth/me | 
*DefaultApi* | [**getDataset**](docs/Api/DefaultApi.md#getdataset) | **GET** /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId} | 
*DefaultApi* | [**getDataset1**](docs/Api/DefaultApi.md#getdataset1) | **GET** /webrobot/api/datasets/{datasetId} | 
*DefaultApi* | [**getDatasetFields**](docs/Api/DefaultApi.md#getdatasetfields) | **GET** /webrobot/api/datasets/{datasetId}/fields | 
*DefaultApi* | [**getDatasetInfoByTask**](docs/Api/DefaultApi.md#getdatasetinfobytask) | **GET** /webrobot/api/datasets/query/task/{taskId}/info | 
*DefaultApi* | [**getDatasetInputFile**](docs/Api/DefaultApi.md#getdatasetinputfile) | **GET** /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId}/input/url | 
*DefaultApi* | [**getDatasetInputFilePagination**](docs/Api/DefaultApi.md#getdatasetinputfilepagination) | **GET** /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId}/input/{offset}/{limit} | 
*DefaultApi* | [**getDatasetInputFileSize**](docs/Api/DefaultApi.md#getdatasetinputfilesize) | **GET** /webrobot/api/datasets-legacy/{datasetId}/input/size | 
*DefaultApi* | [**getDatasetStatus**](docs/Api/DefaultApi.md#getdatasetstatus) | **GET** /webrobot/api/datasets-legacy/datasets/{datasetId}/status | 
*DefaultApi* | [**getDatasetVersionInputFile**](docs/Api/DefaultApi.md#getdatasetversioninputfile) | **GET** /webrobot/api/datasets-legacy/{categoryId}/{jobId}/{datasetId}/versions/{versionsetId}/input/url | 
*DefaultApi* | [**getDatasetVersionInputFilePagination**](docs/Api/DefaultApi.md#getdatasetversioninputfilepagination) | **GET** /webrobot/api/datasets-legacy/{datasetId}/versions/{versionsetId}/input/{offset}/{limit} | 
*DefaultApi* | [**getEffectiveEntitlements**](docs/Api/DefaultApi.md#geteffectiveentitlements) | **GET** /webrobot/api/etl/entitlements | 
*DefaultApi* | [**getExecutionLogs**](docs/Api/DefaultApi.md#getexecutionlogs) | **GET** /webrobot/api/demo/executions/{executionId}/logs | 
*DefaultApi* | [**getExecutionLogs1**](docs/Api/DefaultApi.md#getexecutionlogs1) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/executions/{executionId}/logs | 
*DefaultApi* | [**getExecutionOutput**](docs/Api/DefaultApi.md#getexecutionoutput) | **GET** /webrobot/api/demo/executions/{executionId}/output | 
*DefaultApi* | [**getExecutionStatus**](docs/Api/DefaultApi.md#getexecutionstatus) | **GET** /webrobot/api/demo/executions/{executionId}/status | 
*DefaultApi* | [**getExecutionStatus1**](docs/Api/DefaultApi.md#getexecutionstatus1) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/executions/{executionId}/status | 
*DefaultApi* | [**getHealth**](docs/Api/DefaultApi.md#gethealth) | **GET** /health | 
*DefaultApi* | [**getHtml**](docs/Api/DefaultApi.md#gethtml) | **GET** /webrobot/api/html/{url}/{protocol} | 
*DefaultApi* | [**getImagesSimplified**](docs/Api/DefaultApi.md#getimagessimplified) | **POST** /webrobot/api/ean-image-sourcing/{country}/images | 
*DefaultApi* | [**getInfo**](docs/Api/DefaultApi.md#getinfo) | **GET** /webrobot/cloud/spark/info | 
*DefaultApi* | [**getInfo1**](docs/Api/DefaultApi.md#getinfo1) | **GET** /webrobot/cloud/training/info | 
*DefaultApi* | [**getInstallationById**](docs/Api/DefaultApi.md#getinstallationbyid) | **GET** /webrobot/api/admin/plugin-installations/{id} | 
*DefaultApi* | [**getJob**](docs/Api/DefaultApi.md#getjob) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId} | 
*DefaultApi* | [**getJobLogs**](docs/Api/DefaultApi.md#getjoblogs) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/logs | 
*DefaultApi* | [**getJobMetrics**](docs/Api/DefaultApi.md#getjobmetrics) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/metrics | 
*DefaultApi* | [**getOrganization**](docs/Api/DefaultApi.md#getorganization) | **GET** /webrobot/api/auth/organizations/{id} | 
*DefaultApi* | [**getOrganizationPlugins**](docs/Api/DefaultApi.md#getorganizationplugins) | **GET** /webrobot/api/admin/plugin-installations/../organizations/{organizationId}/plugin-installations | 
*DefaultApi* | [**getOrganizationUsers**](docs/Api/DefaultApi.md#getorganizationusers) | **GET** /webrobot/api/auth/organizations/{id}/users | 
*DefaultApi* | [**getPartnersByType**](docs/Api/DefaultApi.md#getpartnersbytype) | **GET** /webrobot/api/auth/partners/{type} | 
*DefaultApi* | [**getPluginInfo**](docs/Api/DefaultApi.md#getplugininfo) | **GET** /webrobot/api/demo/info | 
*DefaultApi* | [**getPluginInfo1**](docs/Api/DefaultApi.md#getplugininfo1) | **GET** /webrobot/api/ean-image-sourcing/info | 
*DefaultApi* | [**getPluginInfo2**](docs/Api/DefaultApi.md#getplugininfo2) | **GET** /webrobot/api/python-extensions/info | 
*DefaultApi* | [**getPluginOrganizations**](docs/Api/DefaultApi.md#getpluginorganizations) | **GET** /webrobot/api/admin/plugin-installations/{pluginInstallationId}/organizations | 
*DefaultApi* | [**getPluginUsage**](docs/Api/DefaultApi.md#getpluginusage) | **GET** /webrobot/api/admin/plugins/{pluginId}/usage | 
*DefaultApi* | [**getProfile**](docs/Api/DefaultApi.md#getprofile) | **GET** /webrobot/api/agentic/profiles/{id} | 
*DefaultApi* | [**getProject**](docs/Api/DefaultApi.md#getproject) | **GET** /webrobot/api/projects/id/{projectId} | 
*DefaultApi* | [**getProjectFromName**](docs/Api/DefaultApi.md#getprojectfromname) | **GET** /webrobot/api/projects/{projectName} | 
*DefaultApi* | [**getProjectJobs**](docs/Api/DefaultApi.md#getprojectjobs) | **GET** /webrobot/api/projects/id/{projectId}/jobs | 
*DefaultApi* | [**getProjectMetrics**](docs/Api/DefaultApi.md#getprojectmetrics) | **GET** /webrobot/api/projects/id/{projectId}/metrics | 
*DefaultApi* | [**getProjectSchedule**](docs/Api/DefaultApi.md#getprojectschedule) | **GET** /webrobot/api/projects/id/{projectId}/schedule | 
*DefaultApi* | [**getStage**](docs/Api/DefaultApi.md#getstage) | **GET** /webrobot/api/manifest/stages/{name} | 
*DefaultApi* | [**getStatus**](docs/Api/DefaultApi.md#getstatus) | **GET** /webrobot/api/ean-image-sourcing/{country}/status | 
*DefaultApi* | [**getSupportedExtensionTypes**](docs/Api/DefaultApi.md#getsupportedextensiontypes) | **GET** /webrobot/api/python-extensions/supported-types | 
*DefaultApi* | [**getSupportedModels**](docs/Api/DefaultApi.md#getsupportedmodels) | **GET** /webrobot/api/ai-providers/providers/{provider}/models | 
*DefaultApi* | [**getSupportedProviders**](docs/Api/DefaultApi.md#getsupportedproviders) | **GET** /webrobot/api/ai-providers/providers | 
*DefaultApi* | [**getSystemLogs**](docs/Api/DefaultApi.md#getsystemlogs) | **GET** /webrobot/api/projects/admin/system-logs | 
*DefaultApi* | [**getTableColumns**](docs/Api/DefaultApi.md#gettablecolumns) | **GET** /webrobot/api/datasets/query/columns | 
*DefaultApi* | [**getTask**](docs/Api/DefaultApi.md#gettask) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
*DefaultApi* | [**getTaskByOutputDataset**](docs/Api/DefaultApi.md#gettaskbyoutputdataset) | **GET** /webrobot/api/datasets/query/by-dataset/{datasetId}/task | 
*DefaultApi* | [**getTaskMetrics**](docs/Api/DefaultApi.md#gettaskmetrics) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/metrics | 
*DefaultApi* | [**getTaskStatus**](docs/Api/DefaultApi.md#gettaskstatus) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/status | 
*DefaultApi* | [**getTrainingLogs**](docs/Api/DefaultApi.md#gettraininglogs) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/logs | 
*DefaultApi* | [**getTrainingStatus**](docs/Api/DefaultApi.md#gettrainingstatus) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/status | 
*DefaultApi* | [**getUiDefinitions**](docs/Api/DefaultApi.md#getuidefinitions) | **GET** /webrobot/api/admin/plugin-installations/ui-definitions | 
*DefaultApi* | [**getUploadFileUrl**](docs/Api/DefaultApi.md#getuploadfileurl) | **GET** /webrobot/api/datasets-legacy/{categoryId}/{jobId}/upload/{attachmentName} | 
*DefaultApi* | [**getUrlDownload**](docs/Api/DefaultApi.md#geturldownload) | **GET** /webrobot/api/package/download | 
*DefaultApi* | [**getUrlUpload**](docs/Api/DefaultApi.md#geturlupload) | **GET** /webrobot/api/package/upload | 
*DefaultApi* | [**getUserInvites**](docs/Api/DefaultApi.md#getuserinvites) | **GET** /webrobot/api/auth/user-invites | 
*DefaultApi* | [**getVersionByBuildTypeAndBuildNumber**](docs/Api/DefaultApi.md#getversionbybuildtypeandbuildnumber) | **GET** /webrobot/api/admin/etl-library-versions/build-type/{buildType}/build-number/{buildNumber} | 
*DefaultApi* | [**getVersionById**](docs/Api/DefaultApi.md#getversionbyid) | **GET** /webrobot/api/admin/etl-library-versions/id/{id} | 
*DefaultApi* | [**getVersionset**](docs/Api/DefaultApi.md#getversionset) | **GET** /webrobot/api/datasets-legacy/version/id/{versionsetId} | 
*DefaultApi* | [**getVersionsetFromVersion**](docs/Api/DefaultApi.md#getversionsetfromversion) | **POST** /webrobot/api/datasets-legacy/{datasetId}/versions/version/{version} | 
*DefaultApi* | [**getVersionsetFromVersionBase**](docs/Api/DefaultApi.md#getversionsetfromversionbase) | **GET** /webrobot/api/datasets-legacy/{datasetId}/versions/version/{version}/base | 
*DefaultApi* | [**healthCheck**](docs/Api/DefaultApi.md#healthcheck) | **GET** /webrobot/cloud/spark/health | 
*DefaultApi* | [**healthCheck1**](docs/Api/DefaultApi.md#healthcheck1) | **GET** /webrobot/cloud/training/health | 
*DefaultApi* | [**indexDataset**](docs/Api/DefaultApi.md#indexdataset) | **POST** /webrobot/api/datasets/{datasetId}/index | 
*DefaultApi* | [**infer**](docs/Api/DefaultApi.md#infer) | **POST** /webrobot/api/llm/infer | 
*DefaultApi* | [**insert**](docs/Api/DefaultApi.md#insert) | **POST** /api/strapi-tables/{table} | 
*DefaultApi* | [**installBundle**](docs/Api/DefaultApi.md#installbundle) | **POST** /webrobot/api/admin/bundles/install | 
*DefaultApi* | [**jobCompletionWebhook**](docs/Api/DefaultApi.md#jobcompletionwebhook) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/completion | 
*DefaultApi* | [**listAdapters**](docs/Api/DefaultApi.md#listadapters) | **GET** /webrobot/api/admin/cloud-adapters | 
*DefaultApi* | [**listApiKeys**](docs/Api/DefaultApi.md#listapikeys) | **GET** /webrobot/api/auth/api-keys | 
*DefaultApi* | [**listAvailable**](docs/Api/DefaultApi.md#listavailable) | **GET** /webrobot/api/admin/cloud-adapters/available | 
*DefaultApi* | [**listBundles**](docs/Api/DefaultApi.md#listbundles) | **GET** /webrobot/api/admin/bundles | 
*DefaultApi* | [**listCharges**](docs/Api/DefaultApi.md#listcharges) | **GET** /webrobot/api/admin/marketplace-billing/charges | 
*DefaultApi* | [**listCliPlugins**](docs/Api/DefaultApi.md#listcliplugins) | **GET** /webrobot/api/admin/bundles/cli-plugins-list | 
*DefaultApi* | [**listCronJobs**](docs/Api/DefaultApi.md#listcronjobs) | **GET** /webrobot/cloud/scheduler/cronjobs | 
*DefaultApi* | [**listDemos**](docs/Api/DefaultApi.md#listdemos) | **GET** /webrobot/api/demo/list | 
*DefaultApi* | [**listExecutions**](docs/Api/DefaultApi.md#listexecutions) | **GET** /webrobot/api/agentic/executions | 
*DefaultApi* | [**listMyAdapters**](docs/Api/DefaultApi.md#listmyadapters) | **GET** /webrobot/api/admin/cloud-adapters/mine | 
*DefaultApi* | [**listPayouts**](docs/Api/DefaultApi.md#listpayouts) | **GET** /webrobot/api/admin/marketplace-billing/payouts | 
*DefaultApi* | [**listPlugins**](docs/Api/DefaultApi.md#listplugins) | **GET** /webrobot/api/admin/plugins | 
*DefaultApi* | [**listProfiles**](docs/Api/DefaultApi.md#listprofiles) | **GET** /webrobot/api/agentic/profiles | 
*DefaultApi* | [**listProviders**](docs/Api/DefaultApi.md#listproviders) | **GET** /webrobot/api/llm/providers | 
*DefaultApi* | [**listRevenueShare**](docs/Api/DefaultApi.md#listrevenueshare) | **GET** /webrobot/api/admin/agency-billing/revenue-share | 
*DefaultApi* | [**listStages**](docs/Api/DefaultApi.md#liststages) | **GET** /webrobot/api/catalog/stages | 
*DefaultApi* | [**listStages1**](docs/Api/DefaultApi.md#liststages1) | **GET** /webrobot/api/manifest/stages | 
*DefaultApi* | [**listTables**](docs/Api/DefaultApi.md#listtables) | **GET** /webrobot/api/datasets/query/tables | 
*DefaultApi* | [**markFailed**](docs/Api/DefaultApi.md#markfailed) | **POST** /webrobot/api/admin/marketplace-billing/charges/by-invoice/{invoiceId}/mark-failed | 
*DefaultApi* | [**markPaid**](docs/Api/DefaultApi.md#markpaid) | **POST** /webrobot/api/admin/marketplace-billing/charges/by-invoice/{invoiceId}/mark-paid | 
*DefaultApi* | [**markZombieTasks**](docs/Api/DefaultApi.md#markzombietasks) | **POST** /webrobot/api/projects/admin/tasks/mark-zombies | 
*DefaultApi* | [**probeAdapter**](docs/Api/DefaultApi.md#probeadapter) | **POST** /webrobot/api/admin/cloud-adapters/{providerKey}/probe | 
*DefaultApi* | [**processYamlExtensions**](docs/Api/DefaultApi.md#processyamlextensions) | **POST** /webrobot/api/python-extensions/process-yaml | 
*DefaultApi* | [**publishModel**](docs/Api/DefaultApi.md#publishmodel) | **POST** /webrobot/api/ai-providers/providers/huggingface/models/publish | 
*DefaultApi* | [**queryDatasetByTask**](docs/Api/DefaultApi.md#querydatasetbytask) | **POST** /webrobot/api/datasets/query/task/{taskId} | 
*DefaultApi* | [**queryImages**](docs/Api/DefaultApi.md#queryimages) | **POST** /webrobot/api/ean-image-sourcing/{country}/query | 
*DefaultApi* | [**refreshOrganizationsBillingStatus**](docs/Api/DefaultApi.md#refreshorganizationsbillingstatus) | **POST** /webrobot/api/auth/organizations/billing/refresh | 
*DefaultApi* | [**refund**](docs/Api/DefaultApi.md#refund) | **POST** /webrobot/api/admin/marketplace-billing/charges/{id}/refund | 
*DefaultApi* | [**registerPlugin**](docs/Api/DefaultApi.md#registerplugin) | **POST** /webrobot/api/admin/plugin-installations | 
*DefaultApi* | [**registerPythonExtension**](docs/Api/DefaultApi.md#registerpythonextension) | **POST** /webrobot/api/python-extensions/python-extensions/register | 
*DefaultApi* | [**rejectBundle**](docs/Api/DefaultApi.md#rejectbundle) | **POST** /webrobot/api/admin/bundles/{id}/reject | 
*DefaultApi* | [**reloadPipelines**](docs/Api/DefaultApi.md#reloadpipelines) | **POST** /webrobot/api/demo/reload-pipelines | 
*DefaultApi* | [**reloadPlugins**](docs/Api/DefaultApi.md#reloadplugins) | **POST** /webrobot/api/admin/plugin-installations/reload | 
*DefaultApi* | [**removeJobFromProject**](docs/Api/DefaultApi.md#removejobfromproject) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId} | 
*DefaultApi* | [**reportHealth**](docs/Api/DefaultApi.md#reporthealth) | **POST** /webrobot/api/admin/cloud-adapters/{providerKey}/health | 
*DefaultApi* | [**rescheduleEvents**](docs/Api/DefaultApi.md#rescheduleevents) | **POST** /webrobot/api/streaming/reschedule-events | 
*DefaultApi* | [**rollup**](docs/Api/DefaultApi.md#rollup) | **POST** /webrobot/api/admin/stage-usage/rollup | 
*DefaultApi* | [**runCharges**](docs/Api/DefaultApi.md#runcharges) | **POST** /webrobot/api/admin/marketplace-billing/run-charges | 
*DefaultApi* | [**runHealthCheck**](docs/Api/DefaultApi.md#runhealthcheck) | **POST** /webrobot/api/admin/cloud-adapters/run-health-check | 
*DefaultApi* | [**runOrchestrationCharges**](docs/Api/DefaultApi.md#runorchestrationcharges) | **POST** /webrobot/api/admin/marketplace-billing/run-orchestration-charges | 
*DefaultApi* | [**runPayouts**](docs/Api/DefaultApi.md#runpayouts) | **POST** /webrobot/api/admin/marketplace-billing/run-payouts | 
*DefaultApi* | [**runProviderEndpointCharges**](docs/Api/DefaultApi.md#runproviderendpointcharges) | **POST** /webrobot/api/admin/marketplace-billing/run-provider-endpoint-charges | 
*DefaultApi* | [**runRevenueShare**](docs/Api/DefaultApi.md#runrevenueshare) | **POST** /webrobot/api/admin/agency-billing/run-revenue-share | 
*DefaultApi* | [**saveGeneratedPipeline**](docs/Api/DefaultApi.md#savegeneratedpipeline) | **POST** /webrobot/api/demo/save-generated-pipeline | 
*DefaultApi* | [**scheduleJob**](docs/Api/DefaultApi.md#schedulejob) | **POST** /webrobot/api/ean-image-sourcing/{country}/schedule | 
*DefaultApi* | [**serveDemoApp**](docs/Api/DefaultApi.md#servedemoapp) | **GET** /webrobot/api/demo/app | 
*DefaultApi* | [**serveStaticFile**](docs/Api/DefaultApi.md#servestaticfile) | **GET** /webrobot/api/demo/app/{filename} | 
*DefaultApi* | [**setProjectSchedule**](docs/Api/DefaultApi.md#setprojectschedule) | **PUT** /webrobot/api/projects/id/{projectId}/schedule | 
*DefaultApi* | [**start**](docs/Api/DefaultApi.md#start) | **POST** /webrobot/api/agentic/start | 
*DefaultApi* | [**startExportAll**](docs/Api/DefaultApi.md#startexportall) | **GET** /webrobot/api/package/export/all | 
*DefaultApi* | [**startExportOrganization**](docs/Api/DefaultApi.md#startexportorganization) | **GET** /webrobot/api/package/export/organization/{organizationId} | 
*DefaultApi* | [**startExportOrganizationWithOptions**](docs/Api/DefaultApi.md#startexportorganizationwithoptions) | **POST** /webrobot/api/package/export/organization/{organizationId} | 
*DefaultApi* | [**startExportProject**](docs/Api/DefaultApi.md#startexportproject) | **GET** /webrobot/api/package/export/id/{projectId} | 
*DefaultApi* | [**startImportAll**](docs/Api/DefaultApi.md#startimportall) | **GET** /webrobot/api/package/import/all | 
*DefaultApi* | [**startImportAllWithOptions**](docs/Api/DefaultApi.md#startimportallwithoptions) | **POST** /webrobot/api/package/import/all | 
*DefaultApi* | [**startImportOrganization**](docs/Api/DefaultApi.md#startimportorganization) | **GET** /webrobot/api/package/import/organization/{organizationId} | 
*DefaultApi* | [**startImportOrganizationWithOptions**](docs/Api/DefaultApi.md#startimportorganizationwithoptions) | **POST** /webrobot/api/package/import/organization/{organizationId} | 
*DefaultApi* | [**startImportProject**](docs/Api/DefaultApi.md#startimportproject) | **GET** /webrobot/api/package/import/id/{projectId} | 
*DefaultApi* | [**startImportProjectWithOptions**](docs/Api/DefaultApi.md#startimportprojectwithoptions) | **POST** /webrobot/api/package/import/id/{projectId} | 
*DefaultApi* | [**startTask**](docs/Api/DefaultApi.md#starttask) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/start | 
*DefaultApi* | [**startTraining**](docs/Api/DefaultApi.md#starttraining) | **POST** /webrobot/api/ai-providers/providers/{provider}/training | 
*DefaultApi* | [**status**](docs/Api/DefaultApi.md#status) | **GET** /webrobot/api/agentic/{eid} | 
*DefaultApi* | [**stopJob**](docs/Api/DefaultApi.md#stopjob) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/stop | 
*DefaultApi* | [**stopTask**](docs/Api/DefaultApi.md#stoptask) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/stop | 
*DefaultApi* | [**suggestStages**](docs/Api/DefaultApi.md#suggeststages) | **POST** /webrobot/api/demo/wizard/suggest | 
*DefaultApi* | [**test**](docs/Api/DefaultApi.md#test) | **GET** /webrobot/api/categories/test | 
*DefaultApi* | [**test1**](docs/Api/DefaultApi.md#test1) | **GET** /webrobot/api/projects/test | 
*DefaultApi* | [**testCloudCredential**](docs/Api/DefaultApi.md#testcloudcredential) | **POST** /webrobot/api/cloud-credentials/test | 
*DefaultApi* | [**update**](docs/Api/DefaultApi.md#update) | **PUT** /api/strapi-tables/{table}/{id} | 
*DefaultApi* | [**updateAdapter**](docs/Api/DefaultApi.md#updateadapter) | **PUT** /webrobot/api/admin/cloud-adapters/{providerKey} | 
*DefaultApi* | [**updateAgent**](docs/Api/DefaultApi.md#updateagent) | **PUT** /webrobot/api/agents/{categoryId}/{agentId} | 
*DefaultApi* | [**updateAgentPythonExtensions**](docs/Api/DefaultApi.md#updateagentpythonextensions) | **POST** /webrobot/api/python-extensions/agents/{agentId}/python-extensions | 
*DefaultApi* | [**updateBillingPlan**](docs/Api/DefaultApi.md#updatebillingplan) | **PUT** /webrobot/api/billing/plans/{id} | 
*DefaultApi* | [**updateCategory**](docs/Api/DefaultApi.md#updatecategory) | **PUT** /webrobot/api/categories/id/{categoryId} | 
*DefaultApi* | [**updateCloudCredential**](docs/Api/DefaultApi.md#updatecloudcredential) | **PUT** /webrobot/api/cloud-credentials/id/{credentialId} | 
*DefaultApi* | [**updateDataset**](docs/Api/DefaultApi.md#updatedataset) | **PUT** /webrobot/api/datasets/{datasetId} | 
*DefaultApi* | [**updateInstallation**](docs/Api/DefaultApi.md#updateinstallation) | **PUT** /webrobot/api/admin/plugin-installations/{id} | 
*DefaultApi* | [**updateJob**](docs/Api/DefaultApi.md#updatejob) | **PUT** /webrobot/api/projects/id/{projectId}/jobs/{jobId} | 
*DefaultApi* | [**updateOrganization**](docs/Api/DefaultApi.md#updateorganization) | **PUT** /webrobot/api/auth/organizations/{id} | 
*DefaultApi* | [**updateProfile**](docs/Api/DefaultApi.md#updateprofile) | **PUT** /webrobot/api/agentic/profiles/{id} | 
*DefaultApi* | [**updateProject**](docs/Api/DefaultApi.md#updateproject) | **PUT** /webrobot/api/projects/id/{projectId} | 
*DefaultApi* | [**updatePythonExtension**](docs/Api/DefaultApi.md#updatepythonextension) | **PUT** /webrobot/api/python-extensions/python-extensions/{extensionId} | 
*DefaultApi* | [**updateTask**](docs/Api/DefaultApi.md#updatetask) | **PUT** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
*DefaultApi* | [**updateVersion**](docs/Api/DefaultApi.md#updateversion) | **PUT** /webrobot/api/admin/etl-library-versions/id/{id} | 
*DefaultApi* | [**uploadCsv**](docs/Api/DefaultApi.md#uploadcsv) | **POST** /webrobot/api/ean-image-sourcing/{country}/upload | 
*DefaultApi* | [**uploadDataset**](docs/Api/DefaultApi.md#uploaddataset) | **POST** /webrobot/api/demo/upload-dataset/{pipeline-name} | 
*DefaultApi* | [**uploadDataset1**](docs/Api/DefaultApi.md#uploaddataset1) | **POST** /webrobot/api/ai-providers/providers/{provider}/datasets | 
*DefaultApi* | [**uploadDataset2**](docs/Api/DefaultApi.md#uploaddataset2) | **POST** /webrobot/api/datasets-legacy/{projectId}/{botId} | 
*DefaultApi* | [**uploadDatasetFile**](docs/Api/DefaultApi.md#uploaddatasetfile) | **POST** /webrobot/api/datasets/upload | 
*DefaultApi* | [**uploadFile**](docs/Api/DefaultApi.md#uploadfile) | **POST** /webrobot/api/package/upload | 
*DefaultApi* | [**uploadPlugin**](docs/Api/DefaultApi.md#uploadplugin) | **POST** /webrobot/api/admin/plugins/upload | 
*DefaultApi* | [**validate**](docs/Api/DefaultApi.md#validate) | **POST** /webrobot/api/manifest/validate | 
*DefaultApi* | [**validatePythonExtension**](docs/Api/DefaultApi.md#validatepythonextension) | **POST** /webrobot/api/python-extensions/validate | 
*DefaultApi* | [**wizardInferActions**](docs/Api/DefaultApi.md#wizardinferactions) | **POST** /webrobot/api/demo/wizard/infer-actions | 
*DefaultApi* | [**wizardInferFields**](docs/Api/DefaultApi.md#wizardinferfields) | **POST** /webrobot/api/demo/wizard/infer-fields | 
*DefaultApi* | [**wizardInferSegment**](docs/Api/DefaultApi.md#wizardinfersegment) | **POST** /webrobot/api/demo/wizard/infer-segment | 
*DefaultApi* | [**wizardInferSelector**](docs/Api/DefaultApi.md#wizardinferselector) | **POST** /webrobot/api/demo/wizard/infer-selector | 
*DefaultApi* | [**wizardProxy**](docs/Api/DefaultApi.md#wizardproxy) | **GET** /webrobot/api/demo/wizard/proxy | 
*DefaultApi* | [**wizardSuggestFieldNames**](docs/Api/DefaultApi.md#wizardsuggestfieldnames) | **POST** /webrobot/api/demo/wizard/suggest-field-names | 
*DefaultApi* | [**wizardValidate**](docs/Api/DefaultApi.md#wizardvalidate) | **POST** /webrobot/api/demo/wizard/validate | 

## Models

- [AgentDto](docs/Model/AgentDto.md)
- [AgenticProfile](docs/Model/AgenticProfile.md)
- [BodyPart](docs/Model/BodyPart.md)
- [BodyPartMediaType](docs/Model/BodyPartMediaType.md)
- [CloudCredential](docs/Model/CloudCredential.md)
- [CompletionRequest](docs/Model/CompletionRequest.md)
- [ContentDisposition](docs/Model/ContentDisposition.md)
- [CopyToOrganizationsDto](docs/Model/CopyToOrganizationsDto.md)
- [CronJobRequest](docs/Model/CronJobRequest.md)
- [DatasetDto](docs/Model/DatasetDto.md)
- [DatasetUploadApiDto](docs/Model/DatasetUploadApiDto.md)
- [DatasetUploadRequest](docs/Model/DatasetUploadRequest.md)
- [EtlLibraryVersionApiDto](docs/Model/EtlLibraryVersionApiDto.md)
- [ExportOptionsDto](docs/Model/ExportOptionsDto.md)
- [FormDataBodyPart](docs/Model/FormDataBodyPart.md)
- [FormDataContentDisposition](docs/Model/FormDataContentDisposition.md)
- [ImportOptionsDto](docs/Model/ImportOptionsDto.md)
- [InferRequest](docs/Model/InferRequest.md)
- [JobCategoryDto](docs/Model/JobCategoryDto.md)
- [JobCompletionWebhookRequest](docs/Model/JobCompletionWebhookRequest.md)
- [JobDto](docs/Model/JobDto.md)
- [JobProjectDto](docs/Model/JobProjectDto.md)
- [ModelPublishRequest](docs/Model/ModelPublishRequest.md)
- [MultiPart](docs/Model/MultiPart.md)
- [ParameterizedHeader](docs/Model/ParameterizedHeader.md)
- [PluginInstallation](docs/Model/PluginInstallation.md)
- [PrestoQueryRequest](docs/Model/PrestoQueryRequest.md)
- [ProjectScheduleRequest](docs/Model/ProjectScheduleRequest.md)
- [RescheduleEventsRequest](docs/Model/RescheduleEventsRequest.md)
- [StartRequest](docs/Model/StartRequest.md)
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
    - Generator version: `7.17.0`
- Build package: `org.openapitools.codegen.languages.PhpClientCodegen`
