# OpenAPI\Client\DefaultApi



All URIs are relative to http://localhost, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addJobToProject()**](DefaultApi.md#addJobToProject) | **POST** /webrobot/api/projects/id/{projectId}/jobs |  |
| [**apply()**](DefaultApi.md#apply) | **POST** /webrobot/api/manifest/apply |  |
| [**applyMigrations()**](DefaultApi.md#applyMigrations) | **POST** /webrobot/api/admin/bundles/{id}/apply-migrations |  |
| [**approveBundle()**](DefaultApi.md#approveBundle) | **POST** /webrobot/api/admin/bundles/{id}/approve |  |
| [**assignUserToOrganization()**](DefaultApi.md#assignUserToOrganization) | **POST** /webrobot/api/auth/organizations/{id}/assign-user |  |
| [**bootstrapForOrganization()**](DefaultApi.md#bootstrapForOrganization) | **POST** /webrobot/api/ean-image-sourcing/bootstrap/organization/{organizationId} |  |
| [**cancel()**](DefaultApi.md#cancel) | **DELETE** /webrobot/api/agentic/{eid} |  |
| [**cancelExecution()**](DefaultApi.md#cancelExecution) | **DELETE** /webrobot/api/demo/executions/{executionId} |  |
| [**cancelExecution1()**](DefaultApi.md#cancelExecution1) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/executions/{executionId} |  |
| [**cancelTraining()**](DefaultApi.md#cancelTraining) | **DELETE** /webrobot/api/ai-providers/providers/{provider}/training/{jobId} |  |
| [**cmfClose()**](DefaultApi.md#cmfClose) | **DELETE** /webrobot/api/demo/wizard/cmf/{sessionId} |  |
| [**cmfOpen()**](DefaultApi.md#cmfOpen) | **POST** /webrobot/api/demo/wizard/cmf/open |  |
| [**cmfStep()**](DefaultApi.md#cmfStep) | **POST** /webrobot/api/demo/wizard/cmf/step |  |
| [**completion()**](DefaultApi.md#completion) | **POST** /webrobot/api/agentic/{eid}/completion |  |
| [**copyAgent()**](DefaultApi.md#copyAgent) | **POST** /webrobot/api/agents/{agentId}/copy |  |
| [**createAgent()**](DefaultApi.md#createAgent) | **POST** /webrobot/api/agents |  |
| [**createApiKey()**](DefaultApi.md#createApiKey) | **POST** /webrobot/api/auth/api-keys |  |
| [**createBillingPlan()**](DefaultApi.md#createBillingPlan) | **POST** /webrobot/api/billing/plans |  |
| [**createCategory()**](DefaultApi.md#createCategory) | **POST** /webrobot/api/categories |  |
| [**createCloudCredential()**](DefaultApi.md#createCloudCredential) | **POST** /webrobot/api/cloud-credentials |  |
| [**createCronJob()**](DefaultApi.md#createCronJob) | **POST** /webrobot/cloud/scheduler/cronjobs |  |
| [**createCustomPlan()**](DefaultApi.md#createCustomPlan) | **POST** /webrobot/api/billing/custom-plan |  |
| [**createDataset()**](DefaultApi.md#createDataset) | **POST** /webrobot/api/datasets |  |
| [**createOrUpdateVersion()**](DefaultApi.md#createOrUpdateVersion) | **POST** /webrobot/api/admin/etl-library-versions |  |
| [**createOrganization()**](DefaultApi.md#createOrganization) | **POST** /webrobot/api/auth/organizations |  |
| [**createProfile()**](DefaultApi.md#createProfile) | **POST** /webrobot/api/agentic/profiles |  |
| [**createProject()**](DefaultApi.md#createProject) | **POST** /webrobot/api/projects |  |
| [**createTask()**](DefaultApi.md#createTask) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks |  |
| [**decryptField()**](DefaultApi.md#decryptField) | **POST** /webrobot/api/cloud-credentials/id/{credentialId}/decrypt-field |  |
| [**delete()**](DefaultApi.md#delete) | **DELETE** /api/strapi-tables/{table}/{id} |  |
| [**deleteAgent()**](DefaultApi.md#deleteAgent) | **DELETE** /webrobot/api/agents/{agentId} |  |
| [**deleteApiKey()**](DefaultApi.md#deleteApiKey) | **DELETE** /webrobot/api/auth/api-keys/{key_id} |  |
| [**deleteBillingPlan()**](DefaultApi.md#deleteBillingPlan) | **DELETE** /webrobot/api/billing/plans/{id} |  |
| [**deleteCategory()**](DefaultApi.md#deleteCategory) | **DELETE** /webrobot/api/categories/id/{categoryId} |  |
| [**deleteCloudCredential()**](DefaultApi.md#deleteCloudCredential) | **DELETE** /webrobot/api/cloud-credentials/id/{credentialId} |  |
| [**deleteCronJob()**](DefaultApi.md#deleteCronJob) | **DELETE** /webrobot/cloud/scheduler/cronjobs/{name} |  |
| [**deleteDataset()**](DefaultApi.md#deleteDataset) | **DELETE** /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId} |  |
| [**deleteDataset1()**](DefaultApi.md#deleteDataset1) | **DELETE** /webrobot/api/datasets/{datasetId} |  |
| [**deleteDatasetVersion()**](DefaultApi.md#deleteDatasetVersion) | **DELETE** /webrobot/api/datasets-legacy/version/id/{versionsetId} |  |
| [**deleteInstallation()**](DefaultApi.md#deleteInstallation) | **DELETE** /webrobot/api/admin/plugin-installations/{id} |  |
| [**deleteProfile()**](DefaultApi.md#deleteProfile) | **DELETE** /webrobot/api/agentic/profiles/{id} |  |
| [**deleteProject()**](DefaultApi.md#deleteProject) | **DELETE** /webrobot/api/projects/id/{projectId} |  |
| [**deletePythonExtension()**](DefaultApi.md#deletePythonExtension) | **DELETE** /webrobot/api/python-extensions/python-extensions/{extensionId} |  |
| [**deleteTask()**](DefaultApi.md#deleteTask) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} |  |
| [**deleteUserInvite()**](DefaultApi.md#deleteUserInvite) | **DELETE** /webrobot/api/auth/user-invites/{id} |  |
| [**deleteVersion()**](DefaultApi.md#deleteVersion) | **DELETE** /webrobot/api/admin/etl-library-versions/id/{id} |  |
| [**deprecateBundle()**](DefaultApi.md#deprecateBundle) | **POST** /webrobot/api/admin/bundles/{id}/deprecate |  |
| [**disablePlugin()**](DefaultApi.md#disablePlugin) | **POST** /webrobot/api/admin/plugins/{pluginId}/disable |  |
| [**disablePlugin1()**](DefaultApi.md#disablePlugin1) | **POST** /webrobot/api/admin/plugin-installations/{id}/disable |  |
| [**disablePluginForOrganization()**](DefaultApi.md#disablePluginForOrganization) | **POST** /webrobot/api/admin/plugin-installations/{pluginInstallationId}/organizations/{organizationId}/disable |  |
| [**downloadBundle()**](DefaultApi.md#downloadBundle) | **GET** /webrobot/api/admin/bundles/{id}/download |  |
| [**downloadCliPlugin()**](DefaultApi.md#downloadCliPlugin) | **GET** /webrobot/api/admin/bundles/cli-plugins/{pluginId} |  |
| [**downloadModel()**](DefaultApi.md#downloadModel) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/download |  |
| [**downloadUiZip()**](DefaultApi.md#downloadUiZip) | **GET** /webrobot/api/admin/plugin-installations/{pluginId}/ui/download |  |
| [**enableByPluginIdForOrganization()**](DefaultApi.md#enableByPluginIdForOrganization) | **POST** /webrobot/api/admin/plugin-installations/by-plugin-id/{pluginId}/organizations/{organizationId}/enable |  |
| [**enablePlugin()**](DefaultApi.md#enablePlugin) | **POST** /webrobot/api/admin/plugins/{pluginId}/enable |  |
| [**enablePlugin1()**](DefaultApi.md#enablePlugin1) | **POST** /webrobot/api/admin/plugin-installations/{id}/enable |  |
| [**enablePluginForOrganization()**](DefaultApi.md#enablePluginForOrganization) | **POST** /webrobot/api/admin/plugin-installations/{pluginInstallationId}/organizations/{organizationId}/enable |  |
| [**estimateCost()**](DefaultApi.md#estimateCost) | **POST** /webrobot/api/ai-providers/providers/{provider}/cost-estimate |  |
| [**executeDemo()**](DefaultApi.md#executeDemo) | **POST** /webrobot/api/demo/execute/{pipeline-name} |  |
| [**executeJob()**](DefaultApi.md#executeJob) | **POST** /webrobot/api/ean-image-sourcing/{country}/execute |  |
| [**executeJob1()**](DefaultApi.md#executeJob1) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/execute |  |
| [**executeQuery()**](DefaultApi.md#executeQuery) | **POST** /webrobot/api/datasets/query |  |
| [**extractDirect()**](DefaultApi.md#extractDirect) | **POST** /webrobot/api/extract/direct |  |
| [**findAll()**](DefaultApi.md#findAll) | **GET** /api/strapi-tables/{table} |  |
| [**generatePipeline()**](DefaultApi.md#generatePipeline) | **POST** /webrobot/api/demo/generate-pipeline |  |
| [**generatePysparkCode()**](DefaultApi.md#generatePysparkCode) | **POST** /webrobot/api/python-extensions/python-extensions/{extensionId}/generate-pyspark |  |
| [**getAgent()**](DefaultApi.md#getAgent) | **GET** /webrobot/api/agents/{categoryId}/{agentId} |  |
| [**getAgentExtensions()**](DefaultApi.md#getAgentExtensions) | **GET** /webrobot/api/python-extensions/agents/{agentId}/extensions |  |
| [**getAgentFromName()**](DefaultApi.md#getAgentFromName) | **GET** /webrobot/api/agents/{categoryId}/name/{agentName} |  |
| [**getAgentPythonExtensions()**](DefaultApi.md#getAgentPythonExtensions) | **GET** /webrobot/api/python-extensions/agents/{agentId}/python-extensions |  |
| [**getAllAgents()**](DefaultApi.md#getAllAgents) | **GET** /webrobot/api/agents/{categoryId} |  |
| [**getAllCategories()**](DefaultApi.md#getAllCategories) | **GET** /webrobot/api/categories |  |
| [**getAllCloudCredentials()**](DefaultApi.md#getAllCloudCredentials) | **GET** /webrobot/api/cloud-credentials |  |
| [**getAllDatasetVersions()**](DefaultApi.md#getAllDatasetVersions) | **GET** /webrobot/api/datasets-legacy/{projectId}/{botId}/versions |  |
| [**getAllDatasets()**](DefaultApi.md#getAllDatasets) | **GET** /webrobot/api/datasets-legacy/datasets |  |
| [**getAllDatasets1()**](DefaultApi.md#getAllDatasets1) | **GET** /webrobot/api/datasets |  |
| [**getAllInstallations()**](DefaultApi.md#getAllInstallations) | **GET** /webrobot/api/admin/plugin-installations |  |
| [**getAllProjects()**](DefaultApi.md#getAllProjects) | **GET** /webrobot/api/projects |  |
| [**getAllTasks()**](DefaultApi.md#getAllTasks) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks |  |
| [**getAllVersions()**](DefaultApi.md#getAllVersions) | **GET** /webrobot/api/admin/etl-library-versions |  |
| [**getAllVersionsets()**](DefaultApi.md#getAllVersionsets) | **GET** /webrobot/api/datasets-legacy/{datasetId}/versions |  |
| [**getBillingPlans()**](DefaultApi.md#getBillingPlans) | **GET** /webrobot/api/billing/plans |  |
| [**getBootstrapStatus()**](DefaultApi.md#getBootstrapStatus) | **GET** /webrobot/api/ean-image-sourcing/bootstrap/status |  |
| [**getBundleScan()**](DefaultApi.md#getBundleScan) | **GET** /webrobot/api/admin/bundles/{id}/scan |  |
| [**getById()**](DefaultApi.md#getById) | **GET** /api/strapi-tables/{table}/{id} |  |
| [**getCapabilities()**](DefaultApi.md#getCapabilities) | **GET** /webrobot/cloud/spark/capabilities |  |
| [**getCatalogStages()**](DefaultApi.md#getCatalogStages) | **GET** /webrobot/api/demo/catalog/stages |  |
| [**getCategory()**](DefaultApi.md#getCategory) | **GET** /webrobot/api/categories/id/{categoryId} |  |
| [**getCategoryFromName()**](DefaultApi.md#getCategoryFromName) | **GET** /webrobot/api/categories/{categoryName} |  |
| [**getCloudCredentialById()**](DefaultApi.md#getCloudCredentialById) | **GET** /webrobot/api/cloud-credentials/id/{credentialId} |  |
| [**getCloudCredentialsByProvider()**](DefaultApi.md#getCloudCredentialsByProvider) | **GET** /webrobot/api/cloud-credentials/provider/{provider} |  |
| [**getCronJob()**](DefaultApi.md#getCronJob) | **GET** /webrobot/cloud/scheduler/cronjobs/{name} |  |
| [**getCurrentUser()**](DefaultApi.md#getCurrentUser) | **GET** /webrobot/api/auth/me |  |
| [**getDataset()**](DefaultApi.md#getDataset) | **GET** /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId} |  |
| [**getDataset1()**](DefaultApi.md#getDataset1) | **GET** /webrobot/api/datasets/{datasetId} |  |
| [**getDatasetFields()**](DefaultApi.md#getDatasetFields) | **GET** /webrobot/api/datasets/{datasetId}/fields |  |
| [**getDatasetInfoByTask()**](DefaultApi.md#getDatasetInfoByTask) | **GET** /webrobot/api/datasets/query/task/{taskId}/info |  |
| [**getDatasetInputFile()**](DefaultApi.md#getDatasetInputFile) | **GET** /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId}/input/url |  |
| [**getDatasetInputFilePagination()**](DefaultApi.md#getDatasetInputFilePagination) | **GET** /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId}/input/{offset}/{limit} |  |
| [**getDatasetInputFileSize()**](DefaultApi.md#getDatasetInputFileSize) | **GET** /webrobot/api/datasets-legacy/{datasetId}/input/size |  |
| [**getDatasetStatus()**](DefaultApi.md#getDatasetStatus) | **GET** /webrobot/api/datasets-legacy/datasets/{datasetId}/status |  |
| [**getDatasetVersionInputFile()**](DefaultApi.md#getDatasetVersionInputFile) | **GET** /webrobot/api/datasets-legacy/{categoryId}/{jobId}/{datasetId}/versions/{versionsetId}/input/url |  |
| [**getDatasetVersionInputFilePagination()**](DefaultApi.md#getDatasetVersionInputFilePagination) | **GET** /webrobot/api/datasets-legacy/{datasetId}/versions/{versionsetId}/input/{offset}/{limit} |  |
| [**getEffectiveEntitlements()**](DefaultApi.md#getEffectiveEntitlements) | **GET** /webrobot/api/etl/entitlements |  |
| [**getExecutionLogs()**](DefaultApi.md#getExecutionLogs) | **GET** /webrobot/api/demo/executions/{executionId}/logs |  |
| [**getExecutionLogs1()**](DefaultApi.md#getExecutionLogs1) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/executions/{executionId}/logs |  |
| [**getExecutionOutput()**](DefaultApi.md#getExecutionOutput) | **GET** /webrobot/api/demo/executions/{executionId}/output |  |
| [**getExecutionStatus()**](DefaultApi.md#getExecutionStatus) | **GET** /webrobot/api/demo/executions/{executionId}/status |  |
| [**getExecutionStatus1()**](DefaultApi.md#getExecutionStatus1) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/executions/{executionId}/status |  |
| [**getHealth()**](DefaultApi.md#getHealth) | **GET** /health |  |
| [**getHtml()**](DefaultApi.md#getHtml) | **GET** /webrobot/api/html/{url}/{protocol} |  |
| [**getImagesSimplified()**](DefaultApi.md#getImagesSimplified) | **POST** /webrobot/api/ean-image-sourcing/{country}/images |  |
| [**getInfo()**](DefaultApi.md#getInfo) | **GET** /webrobot/cloud/spark/info |  |
| [**getInfo1()**](DefaultApi.md#getInfo1) | **GET** /webrobot/cloud/training/info |  |
| [**getInstallationById()**](DefaultApi.md#getInstallationById) | **GET** /webrobot/api/admin/plugin-installations/{id} |  |
| [**getJob()**](DefaultApi.md#getJob) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId} |  |
| [**getJobLogs()**](DefaultApi.md#getJobLogs) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/logs |  |
| [**getJobMetrics()**](DefaultApi.md#getJobMetrics) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/metrics |  |
| [**getOrganization()**](DefaultApi.md#getOrganization) | **GET** /webrobot/api/auth/organizations/{id} |  |
| [**getOrganizationPlugins()**](DefaultApi.md#getOrganizationPlugins) | **GET** /webrobot/api/admin/plugin-installations/../organizations/{organizationId}/plugin-installations |  |
| [**getOrganizationUsers()**](DefaultApi.md#getOrganizationUsers) | **GET** /webrobot/api/auth/organizations/{id}/users |  |
| [**getPartnersByType()**](DefaultApi.md#getPartnersByType) | **GET** /webrobot/api/auth/partners/{type} |  |
| [**getPluginInfo()**](DefaultApi.md#getPluginInfo) | **GET** /webrobot/api/demo/info |  |
| [**getPluginInfo1()**](DefaultApi.md#getPluginInfo1) | **GET** /webrobot/api/ean-image-sourcing/info |  |
| [**getPluginInfo2()**](DefaultApi.md#getPluginInfo2) | **GET** /webrobot/api/python-extensions/info |  |
| [**getPluginOrganizations()**](DefaultApi.md#getPluginOrganizations) | **GET** /webrobot/api/admin/plugin-installations/{pluginInstallationId}/organizations |  |
| [**getPluginUsage()**](DefaultApi.md#getPluginUsage) | **GET** /webrobot/api/admin/plugins/{pluginId}/usage |  |
| [**getProfile()**](DefaultApi.md#getProfile) | **GET** /webrobot/api/agentic/profiles/{id} |  |
| [**getProject()**](DefaultApi.md#getProject) | **GET** /webrobot/api/projects/id/{projectId} |  |
| [**getProjectFromName()**](DefaultApi.md#getProjectFromName) | **GET** /webrobot/api/projects/{projectName} |  |
| [**getProjectJobs()**](DefaultApi.md#getProjectJobs) | **GET** /webrobot/api/projects/id/{projectId}/jobs |  |
| [**getProjectMetrics()**](DefaultApi.md#getProjectMetrics) | **GET** /webrobot/api/projects/id/{projectId}/metrics |  |
| [**getProjectSchedule()**](DefaultApi.md#getProjectSchedule) | **GET** /webrobot/api/projects/id/{projectId}/schedule |  |
| [**getStage()**](DefaultApi.md#getStage) | **GET** /webrobot/api/manifest/stages/{name} |  |
| [**getStatus()**](DefaultApi.md#getStatus) | **GET** /webrobot/api/ean-image-sourcing/{country}/status |  |
| [**getSupportedExtensionTypes()**](DefaultApi.md#getSupportedExtensionTypes) | **GET** /webrobot/api/python-extensions/supported-types |  |
| [**getSupportedModels()**](DefaultApi.md#getSupportedModels) | **GET** /webrobot/api/ai-providers/providers/{provider}/models |  |
| [**getSupportedProviders()**](DefaultApi.md#getSupportedProviders) | **GET** /webrobot/api/ai-providers/providers |  |
| [**getSystemLogs()**](DefaultApi.md#getSystemLogs) | **GET** /webrobot/api/projects/admin/system-logs |  |
| [**getTableColumns()**](DefaultApi.md#getTableColumns) | **GET** /webrobot/api/datasets/query/columns |  |
| [**getTask()**](DefaultApi.md#getTask) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} |  |
| [**getTaskByOutputDataset()**](DefaultApi.md#getTaskByOutputDataset) | **GET** /webrobot/api/datasets/query/by-dataset/{datasetId}/task |  |
| [**getTaskMetrics()**](DefaultApi.md#getTaskMetrics) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/metrics |  |
| [**getTaskStatus()**](DefaultApi.md#getTaskStatus) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/status |  |
| [**getTrainingLogs()**](DefaultApi.md#getTrainingLogs) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/logs |  |
| [**getTrainingStatus()**](DefaultApi.md#getTrainingStatus) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/status |  |
| [**getUiDefinitions()**](DefaultApi.md#getUiDefinitions) | **GET** /webrobot/api/admin/plugin-installations/ui-definitions |  |
| [**getUploadFileUrl()**](DefaultApi.md#getUploadFileUrl) | **GET** /webrobot/api/datasets-legacy/{categoryId}/{jobId}/upload/{attachmentName} |  |
| [**getUrlDownload()**](DefaultApi.md#getUrlDownload) | **GET** /webrobot/api/package/download |  |
| [**getUrlUpload()**](DefaultApi.md#getUrlUpload) | **GET** /webrobot/api/package/upload |  |
| [**getUserInvites()**](DefaultApi.md#getUserInvites) | **GET** /webrobot/api/auth/user-invites |  |
| [**getVersionByBuildTypeAndBuildNumber()**](DefaultApi.md#getVersionByBuildTypeAndBuildNumber) | **GET** /webrobot/api/admin/etl-library-versions/build-type/{buildType}/build-number/{buildNumber} |  |
| [**getVersionById()**](DefaultApi.md#getVersionById) | **GET** /webrobot/api/admin/etl-library-versions/id/{id} |  |
| [**getVersionset()**](DefaultApi.md#getVersionset) | **GET** /webrobot/api/datasets-legacy/version/id/{versionsetId} |  |
| [**getVersionsetFromVersion()**](DefaultApi.md#getVersionsetFromVersion) | **POST** /webrobot/api/datasets-legacy/{datasetId}/versions/version/{version} |  |
| [**getVersionsetFromVersionBase()**](DefaultApi.md#getVersionsetFromVersionBase) | **GET** /webrobot/api/datasets-legacy/{datasetId}/versions/version/{version}/base |  |
| [**healthCheck()**](DefaultApi.md#healthCheck) | **GET** /webrobot/cloud/spark/health |  |
| [**healthCheck1()**](DefaultApi.md#healthCheck1) | **GET** /webrobot/cloud/training/health |  |
| [**indexDataset()**](DefaultApi.md#indexDataset) | **POST** /webrobot/api/datasets/{datasetId}/index |  |
| [**infer()**](DefaultApi.md#infer) | **POST** /webrobot/api/llm/infer |  |
| [**insert()**](DefaultApi.md#insert) | **POST** /api/strapi-tables/{table} |  |
| [**installBundle()**](DefaultApi.md#installBundle) | **POST** /webrobot/api/admin/bundles/install |  |
| [**jobCompletionWebhook()**](DefaultApi.md#jobCompletionWebhook) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/completion |  |
| [**listAdapters()**](DefaultApi.md#listAdapters) | **GET** /webrobot/api/admin/cloud-adapters |  |
| [**listApiKeys()**](DefaultApi.md#listApiKeys) | **GET** /webrobot/api/auth/api-keys |  |
| [**listAvailable()**](DefaultApi.md#listAvailable) | **GET** /webrobot/api/admin/cloud-adapters/available |  |
| [**listBundles()**](DefaultApi.md#listBundles) | **GET** /webrobot/api/admin/bundles |  |
| [**listCharges()**](DefaultApi.md#listCharges) | **GET** /webrobot/api/admin/marketplace-billing/charges |  |
| [**listCliPlugins()**](DefaultApi.md#listCliPlugins) | **GET** /webrobot/api/admin/bundles/cli-plugins-list |  |
| [**listCronJobs()**](DefaultApi.md#listCronJobs) | **GET** /webrobot/cloud/scheduler/cronjobs |  |
| [**listDemos()**](DefaultApi.md#listDemos) | **GET** /webrobot/api/demo/list |  |
| [**listExecutions()**](DefaultApi.md#listExecutions) | **GET** /webrobot/api/agentic/executions |  |
| [**listMyAdapters()**](DefaultApi.md#listMyAdapters) | **GET** /webrobot/api/admin/cloud-adapters/mine |  |
| [**listPayouts()**](DefaultApi.md#listPayouts) | **GET** /webrobot/api/admin/marketplace-billing/payouts |  |
| [**listPlugins()**](DefaultApi.md#listPlugins) | **GET** /webrobot/api/admin/plugins |  |
| [**listProfiles()**](DefaultApi.md#listProfiles) | **GET** /webrobot/api/agentic/profiles |  |
| [**listProviders()**](DefaultApi.md#listProviders) | **GET** /webrobot/api/llm/providers |  |
| [**listRevenueShare()**](DefaultApi.md#listRevenueShare) | **GET** /webrobot/api/admin/agency-billing/revenue-share |  |
| [**listStages()**](DefaultApi.md#listStages) | **GET** /webrobot/api/catalog/stages |  |
| [**listStages1()**](DefaultApi.md#listStages1) | **GET** /webrobot/api/manifest/stages |  |
| [**listTables()**](DefaultApi.md#listTables) | **GET** /webrobot/api/datasets/query/tables |  |
| [**markFailed()**](DefaultApi.md#markFailed) | **POST** /webrobot/api/admin/marketplace-billing/charges/by-invoice/{invoiceId}/mark-failed |  |
| [**markPaid()**](DefaultApi.md#markPaid) | **POST** /webrobot/api/admin/marketplace-billing/charges/by-invoice/{invoiceId}/mark-paid |  |
| [**markZombieTasks()**](DefaultApi.md#markZombieTasks) | **POST** /webrobot/api/projects/admin/tasks/mark-zombies |  |
| [**probeAdapter()**](DefaultApi.md#probeAdapter) | **POST** /webrobot/api/admin/cloud-adapters/{providerKey}/probe |  |
| [**processYamlExtensions()**](DefaultApi.md#processYamlExtensions) | **POST** /webrobot/api/python-extensions/process-yaml |  |
| [**publishModel()**](DefaultApi.md#publishModel) | **POST** /webrobot/api/ai-providers/providers/huggingface/models/publish |  |
| [**queryDatasetByTask()**](DefaultApi.md#queryDatasetByTask) | **POST** /webrobot/api/datasets/query/task/{taskId} |  |
| [**queryImages()**](DefaultApi.md#queryImages) | **POST** /webrobot/api/ean-image-sourcing/{country}/query |  |
| [**refreshOrganizationsBillingStatus()**](DefaultApi.md#refreshOrganizationsBillingStatus) | **POST** /webrobot/api/auth/organizations/billing/refresh |  |
| [**refund()**](DefaultApi.md#refund) | **POST** /webrobot/api/admin/marketplace-billing/charges/{id}/refund |  |
| [**registerPlugin()**](DefaultApi.md#registerPlugin) | **POST** /webrobot/api/admin/plugin-installations |  |
| [**registerPythonExtension()**](DefaultApi.md#registerPythonExtension) | **POST** /webrobot/api/python-extensions/python-extensions/register |  |
| [**rejectBundle()**](DefaultApi.md#rejectBundle) | **POST** /webrobot/api/admin/bundles/{id}/reject |  |
| [**reloadPipelines()**](DefaultApi.md#reloadPipelines) | **POST** /webrobot/api/demo/reload-pipelines |  |
| [**reloadPlugins()**](DefaultApi.md#reloadPlugins) | **POST** /webrobot/api/admin/plugin-installations/reload |  |
| [**removeJobFromProject()**](DefaultApi.md#removeJobFromProject) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId} |  |
| [**reportHealth()**](DefaultApi.md#reportHealth) | **POST** /webrobot/api/admin/cloud-adapters/{providerKey}/health |  |
| [**rescheduleEvents()**](DefaultApi.md#rescheduleEvents) | **POST** /webrobot/api/streaming/reschedule-events |  |
| [**rollup()**](DefaultApi.md#rollup) | **POST** /webrobot/api/admin/stage-usage/rollup |  |
| [**runCharges()**](DefaultApi.md#runCharges) | **POST** /webrobot/api/admin/marketplace-billing/run-charges |  |
| [**runHealthCheck()**](DefaultApi.md#runHealthCheck) | **POST** /webrobot/api/admin/cloud-adapters/run-health-check |  |
| [**runOrchestrationCharges()**](DefaultApi.md#runOrchestrationCharges) | **POST** /webrobot/api/admin/marketplace-billing/run-orchestration-charges |  |
| [**runPayouts()**](DefaultApi.md#runPayouts) | **POST** /webrobot/api/admin/marketplace-billing/run-payouts |  |
| [**runProviderEndpointCharges()**](DefaultApi.md#runProviderEndpointCharges) | **POST** /webrobot/api/admin/marketplace-billing/run-provider-endpoint-charges |  |
| [**runRevenueShare()**](DefaultApi.md#runRevenueShare) | **POST** /webrobot/api/admin/agency-billing/run-revenue-share |  |
| [**saveGeneratedPipeline()**](DefaultApi.md#saveGeneratedPipeline) | **POST** /webrobot/api/demo/save-generated-pipeline |  |
| [**scheduleJob()**](DefaultApi.md#scheduleJob) | **POST** /webrobot/api/ean-image-sourcing/{country}/schedule |  |
| [**serveDemoApp()**](DefaultApi.md#serveDemoApp) | **GET** /webrobot/api/demo/app |  |
| [**serveStaticFile()**](DefaultApi.md#serveStaticFile) | **GET** /webrobot/api/demo/app/{filename} |  |
| [**setProjectSchedule()**](DefaultApi.md#setProjectSchedule) | **PUT** /webrobot/api/projects/id/{projectId}/schedule |  |
| [**start()**](DefaultApi.md#start) | **POST** /webrobot/api/agentic/start |  |
| [**startExportAll()**](DefaultApi.md#startExportAll) | **GET** /webrobot/api/package/export/all |  |
| [**startExportOrganization()**](DefaultApi.md#startExportOrganization) | **GET** /webrobot/api/package/export/organization/{organizationId} |  |
| [**startExportOrganizationWithOptions()**](DefaultApi.md#startExportOrganizationWithOptions) | **POST** /webrobot/api/package/export/organization/{organizationId} |  |
| [**startExportProject()**](DefaultApi.md#startExportProject) | **GET** /webrobot/api/package/export/id/{projectId} |  |
| [**startImportAll()**](DefaultApi.md#startImportAll) | **GET** /webrobot/api/package/import/all |  |
| [**startImportAllWithOptions()**](DefaultApi.md#startImportAllWithOptions) | **POST** /webrobot/api/package/import/all |  |
| [**startImportOrganization()**](DefaultApi.md#startImportOrganization) | **GET** /webrobot/api/package/import/organization/{organizationId} |  |
| [**startImportOrganizationWithOptions()**](DefaultApi.md#startImportOrganizationWithOptions) | **POST** /webrobot/api/package/import/organization/{organizationId} |  |
| [**startImportProject()**](DefaultApi.md#startImportProject) | **GET** /webrobot/api/package/import/id/{projectId} |  |
| [**startImportProjectWithOptions()**](DefaultApi.md#startImportProjectWithOptions) | **POST** /webrobot/api/package/import/id/{projectId} |  |
| [**startTask()**](DefaultApi.md#startTask) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/start |  |
| [**startTraining()**](DefaultApi.md#startTraining) | **POST** /webrobot/api/ai-providers/providers/{provider}/training |  |
| [**status()**](DefaultApi.md#status) | **GET** /webrobot/api/agentic/{eid} |  |
| [**stopJob()**](DefaultApi.md#stopJob) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/stop |  |
| [**stopTask()**](DefaultApi.md#stopTask) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/stop |  |
| [**suggestStages()**](DefaultApi.md#suggestStages) | **POST** /webrobot/api/demo/wizard/suggest |  |
| [**test()**](DefaultApi.md#test) | **GET** /webrobot/api/categories/test |  |
| [**test1()**](DefaultApi.md#test1) | **GET** /webrobot/api/projects/test |  |
| [**testCloudCredential()**](DefaultApi.md#testCloudCredential) | **POST** /webrobot/api/cloud-credentials/test |  |
| [**update()**](DefaultApi.md#update) | **PUT** /api/strapi-tables/{table}/{id} |  |
| [**updateAdapter()**](DefaultApi.md#updateAdapter) | **PUT** /webrobot/api/admin/cloud-adapters/{providerKey} |  |
| [**updateAgent()**](DefaultApi.md#updateAgent) | **PUT** /webrobot/api/agents/{categoryId}/{agentId} |  |
| [**updateAgentPythonExtensions()**](DefaultApi.md#updateAgentPythonExtensions) | **POST** /webrobot/api/python-extensions/agents/{agentId}/python-extensions |  |
| [**updateBillingPlan()**](DefaultApi.md#updateBillingPlan) | **PUT** /webrobot/api/billing/plans/{id} |  |
| [**updateCategory()**](DefaultApi.md#updateCategory) | **PUT** /webrobot/api/categories/id/{categoryId} |  |
| [**updateCloudCredential()**](DefaultApi.md#updateCloudCredential) | **PUT** /webrobot/api/cloud-credentials/id/{credentialId} |  |
| [**updateDataset()**](DefaultApi.md#updateDataset) | **PUT** /webrobot/api/datasets/{datasetId} |  |
| [**updateInstallation()**](DefaultApi.md#updateInstallation) | **PUT** /webrobot/api/admin/plugin-installations/{id} |  |
| [**updateJob()**](DefaultApi.md#updateJob) | **PUT** /webrobot/api/projects/id/{projectId}/jobs/{jobId} |  |
| [**updateOrganization()**](DefaultApi.md#updateOrganization) | **PUT** /webrobot/api/auth/organizations/{id} |  |
| [**updateProfile()**](DefaultApi.md#updateProfile) | **PUT** /webrobot/api/agentic/profiles/{id} |  |
| [**updateProject()**](DefaultApi.md#updateProject) | **PUT** /webrobot/api/projects/id/{projectId} |  |
| [**updatePythonExtension()**](DefaultApi.md#updatePythonExtension) | **PUT** /webrobot/api/python-extensions/python-extensions/{extensionId} |  |
| [**updateTask()**](DefaultApi.md#updateTask) | **PUT** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} |  |
| [**updateVersion()**](DefaultApi.md#updateVersion) | **PUT** /webrobot/api/admin/etl-library-versions/id/{id} |  |
| [**uploadCsv()**](DefaultApi.md#uploadCsv) | **POST** /webrobot/api/ean-image-sourcing/{country}/upload |  |
| [**uploadDataset()**](DefaultApi.md#uploadDataset) | **POST** /webrobot/api/demo/upload-dataset/{pipeline-name} |  |
| [**uploadDataset1()**](DefaultApi.md#uploadDataset1) | **POST** /webrobot/api/ai-providers/providers/{provider}/datasets |  |
| [**uploadDataset2()**](DefaultApi.md#uploadDataset2) | **POST** /webrobot/api/datasets-legacy/{projectId}/{botId} |  |
| [**uploadDatasetFile()**](DefaultApi.md#uploadDatasetFile) | **POST** /webrobot/api/datasets/upload |  |
| [**uploadFile()**](DefaultApi.md#uploadFile) | **POST** /webrobot/api/package/upload |  |
| [**uploadPlugin()**](DefaultApi.md#uploadPlugin) | **POST** /webrobot/api/admin/plugins/upload |  |
| [**validate()**](DefaultApi.md#validate) | **POST** /webrobot/api/manifest/validate |  |
| [**validatePythonExtension()**](DefaultApi.md#validatePythonExtension) | **POST** /webrobot/api/python-extensions/validate |  |
| [**wizardInferActions()**](DefaultApi.md#wizardInferActions) | **POST** /webrobot/api/demo/wizard/infer-actions |  |
| [**wizardInferFields()**](DefaultApi.md#wizardInferFields) | **POST** /webrobot/api/demo/wizard/infer-fields |  |
| [**wizardInferSegment()**](DefaultApi.md#wizardInferSegment) | **POST** /webrobot/api/demo/wizard/infer-segment |  |
| [**wizardInferSelector()**](DefaultApi.md#wizardInferSelector) | **POST** /webrobot/api/demo/wizard/infer-selector |  |
| [**wizardProxy()**](DefaultApi.md#wizardProxy) | **GET** /webrobot/api/demo/wizard/proxy |  |
| [**wizardSuggestFieldNames()**](DefaultApi.md#wizardSuggestFieldNames) | **POST** /webrobot/api/demo/wizard/suggest-field-names |  |
| [**wizardValidate()**](DefaultApi.md#wizardValidate) | **POST** /webrobot/api/demo/wizard/validate |  |


## `addJobToProject()`

```php
addJobToProject($project_id, $job_dto)
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
$job_dto = new \OpenAPI\Client\Model\JobDto(); // \OpenAPI\Client\Model\JobDto

try {
    $apiInstance->addJobToProject($project_id, $job_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->addJobToProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
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

## `apply()`

```php
apply($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->apply($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->apply: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `applyMigrations()`

```php
applyMigrations($id)
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
$id = 56; // int

try {
    $apiInstance->applyMigrations($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->applyMigrations: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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

## `approveBundle()`

```php
approveBundle($id)
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
$id = 56; // int

try {
    $apiInstance->approveBundle($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->approveBundle: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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

## `assignUserToOrganization()`

```php
assignUserToOrganization($id, $request_body)
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
$id = 'id_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->assignUserToOrganization($id, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->assignUserToOrganization: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `bootstrapForOrganization()`

```php
bootstrapForOrganization($organization_id, $request_body)
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
$organization_id = 'organization_id_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->bootstrapForOrganization($organization_id, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->bootstrapForOrganization: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
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

## `cancel()`

```php
cancel($eid)
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
$eid = 'eid_example'; // string

try {
    $apiInstance->cancel($eid);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->cancel: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **eid** | **string**|  | |

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

## `cancelExecution()`

```php
cancelExecution($execution_id)
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
$execution_id = 'execution_id_example'; // string

try {
    $apiInstance->cancelExecution($execution_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->cancelExecution: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **execution_id** | **string**|  | |

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

## `cancelExecution1()`

```php
cancelExecution1($project_id, $job_id, $execution_id)
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
$execution_id = 'execution_id_example'; // string

try {
    $apiInstance->cancelExecution1($project_id, $job_id, $execution_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->cancelExecution1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **execution_id** | **string**|  | |

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

## `cancelTraining()`

```php
cancelTraining($provider, $job_id)
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

try {
    $apiInstance->cancelTraining($provider, $job_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->cancelTraining: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
| **job_id** | **string**|  | |

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

## `cmfClose()`

```php
cmfClose($session_id)
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
$session_id = 'session_id_example'; // string

try {
    $apiInstance->cmfClose($session_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->cmfClose: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **session_id** | **string**|  | |

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

## `cmfOpen()`

```php
cmfOpen($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->cmfOpen($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->cmfOpen: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `cmfStep()`

```php
cmfStep($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->cmfStep($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->cmfStep: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `completion()`

```php
completion($eid, $completion_request)
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
$eid = 'eid_example'; // string
$completion_request = new \OpenAPI\Client\Model\CompletionRequest(); // \OpenAPI\Client\Model\CompletionRequest

try {
    $apiInstance->completion($eid, $completion_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->completion: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **eid** | **string**|  | |
| **completion_request** | [**\OpenAPI\Client\Model\CompletionRequest**](../Model/CompletionRequest.md)|  | [optional] |

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

## `copyAgent()`

```php
copyAgent($agent_id, $copy_to_organizations_dto)
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
$copy_to_organizations_dto = new \OpenAPI\Client\Model\CopyToOrganizationsDto(); // \OpenAPI\Client\Model\CopyToOrganizationsDto

try {
    $apiInstance->copyAgent($agent_id, $copy_to_organizations_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->copyAgent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **agent_id** | **string**|  | |
| **copy_to_organizations_dto** | [**\OpenAPI\Client\Model\CopyToOrganizationsDto**](../Model/CopyToOrganizationsDto.md)|  | [optional] |

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

## `createAgent()`

```php
createAgent($agent_dto)
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
$agent_dto = new \OpenAPI\Client\Model\AgentDto(); // \OpenAPI\Client\Model\AgentDto

try {
    $apiInstance->createAgent($agent_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createAgent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `createApiKey()`

```php
createApiKey($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->createApiKey($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createApiKey: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `createBillingPlan()`

```php
createBillingPlan($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->createBillingPlan($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createBillingPlan: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `createCategory()`

```php
createCategory($job_category_dto)
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
$job_category_dto = new \OpenAPI\Client\Model\JobCategoryDto(); // \OpenAPI\Client\Model\JobCategoryDto

try {
    $apiInstance->createCategory($job_category_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createCategory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `createCloudCredential()`

```php
createCloudCredential($cloud_credential)
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
$cloud_credential = new \OpenAPI\Client\Model\CloudCredential(); // \OpenAPI\Client\Model\CloudCredential

try {
    $apiInstance->createCloudCredential($cloud_credential);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createCloudCredential: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cloud_credential** | [**\OpenAPI\Client\Model\CloudCredential**](../Model/CloudCredential.md)|  | [optional] |

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

## `createCronJob()`

```php
createCronJob($cron_job_request)
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
$cron_job_request = new \OpenAPI\Client\Model\CronJobRequest(); // \OpenAPI\Client\Model\CronJobRequest

try {
    $apiInstance->createCronJob($cron_job_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createCronJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cron_job_request** | [**\OpenAPI\Client\Model\CronJobRequest**](../Model/CronJobRequest.md)|  | [optional] |

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

## `createCustomPlan()`

```php
createCustomPlan($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->createCustomPlan($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createCustomPlan: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `createDataset()`

```php
createDataset($dataset_dto)
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
$dataset_dto = new \OpenAPI\Client\Model\DatasetDto(); // \OpenAPI\Client\Model\DatasetDto

try {
    $apiInstance->createDataset($dataset_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_dto** | [**\OpenAPI\Client\Model\DatasetDto**](../Model/DatasetDto.md)|  | [optional] |

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

## `createOrUpdateVersion()`

```php
createOrUpdateVersion($etl_library_version_api_dto)
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
$etl_library_version_api_dto = new \OpenAPI\Client\Model\EtlLibraryVersionApiDto(); // \OpenAPI\Client\Model\EtlLibraryVersionApiDto

try {
    $apiInstance->createOrUpdateVersion($etl_library_version_api_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createOrUpdateVersion: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **etl_library_version_api_dto** | [**\OpenAPI\Client\Model\EtlLibraryVersionApiDto**](../Model/EtlLibraryVersionApiDto.md)|  | [optional] |

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

## `createOrganization()`

```php
createOrganization($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->createOrganization($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createOrganization: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `createProfile()`

```php
createProfile($agentic_profile)
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
$agentic_profile = new \OpenAPI\Client\Model\AgenticProfile(); // \OpenAPI\Client\Model\AgenticProfile

try {
    $apiInstance->createProfile($agentic_profile);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createProfile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **agentic_profile** | [**\OpenAPI\Client\Model\AgenticProfile**](../Model/AgenticProfile.md)|  | [optional] |

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
createProject($job_project_dto)
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
$job_project_dto = new \OpenAPI\Client\Model\JobProjectDto(); // \OpenAPI\Client\Model\JobProjectDto

try {
    $apiInstance->createProject($job_project_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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
createTask($project_id, $job_id, $task_dto)
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
$task_dto = new \OpenAPI\Client\Model\TaskDto(); // \OpenAPI\Client\Model\TaskDto

try {
    $apiInstance->createTask($project_id, $job_id, $task_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->createTask: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
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

## `decryptField()`

```php
decryptField($credential_id, $request_body)
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
$credential_id = 'credential_id_example'; // string
$request_body = array('key' => 'request_body_example'); // array<string,string>

try {
    $apiInstance->decryptField($credential_id, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->decryptField: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **credential_id** | **string**|  | |
| **request_body** | [**array<string,string>**](../Model/string.md)|  | [optional] |

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
deleteAgent($agent_id)
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

try {
    $apiInstance->deleteAgent($agent_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteAgent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **agent_id** | **string**|  | |

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

## `deleteApiKey()`

```php
deleteApiKey($key_id)
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
$key_id = 'key_id_example'; // string

try {
    $apiInstance->deleteApiKey($key_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteApiKey: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **key_id** | **string**|  | |

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

## `deleteBillingPlan()`

```php
deleteBillingPlan($id)
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
$id = 56; // int

try {
    $apiInstance->deleteBillingPlan($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteBillingPlan: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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
deleteCategory($category_id)
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

try {
    $apiInstance->deleteCategory($category_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteCategory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |

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

## `deleteCloudCredential()`

```php
deleteCloudCredential($credential_id)
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
$credential_id = 'credential_id_example'; // string

try {
    $apiInstance->deleteCloudCredential($credential_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteCloudCredential: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **credential_id** | **string**|  | |

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

## `deleteCronJob()`

```php
deleteCronJob($name, $namespace)
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
$name = 'name_example'; // string
$namespace = 'namespace_example'; // string

try {
    $apiInstance->deleteCronJob($name, $namespace);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteCronJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**|  | |
| **namespace** | **string**|  | [optional] |

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
deleteDataset($dataset_id)
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

try {
    $apiInstance->deleteDataset($dataset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |

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

## `deleteDataset1()`

```php
deleteDataset1($dataset_id)
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

try {
    $apiInstance->deleteDataset1($dataset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteDataset1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |

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
deleteDatasetVersion($versionset_id)
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

try {
    $apiInstance->deleteDatasetVersion($versionset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteDatasetVersion: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **versionset_id** | **string**|  | |

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

## `deleteInstallation()`

```php
deleteInstallation($id)
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
$id = 56; // int

try {
    $apiInstance->deleteInstallation($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteInstallation: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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

## `deleteProfile()`

```php
deleteProfile($id)
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
$id = 56; // int

try {
    $apiInstance->deleteProfile($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteProfile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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
deleteProject($project_id)
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

try {
    $apiInstance->deleteProject($project_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |

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

## `deletePythonExtension()`

```php
deletePythonExtension($extension_id)
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
$extension_id = 'extension_id_example'; // string

try {
    $apiInstance->deletePythonExtension($extension_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deletePythonExtension: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **extension_id** | **string**|  | |

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
deleteTask($project_id, $job_id, $task_id)
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

try {
    $apiInstance->deleteTask($project_id, $job_id, $task_id);
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

## `deleteUserInvite()`

```php
deleteUserInvite($id)
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
$id = 'id_example'; // string

try {
    $apiInstance->deleteUserInvite($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteUserInvite: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `deleteVersion()`

```php
deleteVersion($id)
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
$id = 56; // int

try {
    $apiInstance->deleteVersion($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deleteVersion: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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

## `deprecateBundle()`

```php
deprecateBundle($id)
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
$id = 56; // int

try {
    $apiInstance->deprecateBundle($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->deprecateBundle: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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

## `disablePlugin()`

```php
disablePlugin($plugin_id, $build_type)
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
$plugin_id = 'plugin_id_example'; // string
$build_type = 'development'; // string

try {
    $apiInstance->disablePlugin($plugin_id, $build_type);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->disablePlugin: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_id** | **string**|  | |
| **build_type** | **string**|  | [optional] [default to &#39;development&#39;] |

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

## `disablePlugin1()`

```php
disablePlugin1($id)
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
$id = 56; // int

try {
    $apiInstance->disablePlugin1($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->disablePlugin1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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

## `disablePluginForOrganization()`

```php
disablePluginForOrganization($plugin_installation_id, $organization_id)
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
$plugin_installation_id = 56; // int
$organization_id = 'organization_id_example'; // string

try {
    $apiInstance->disablePluginForOrganization($plugin_installation_id, $organization_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->disablePluginForOrganization: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_installation_id** | **int**|  | |
| **organization_id** | **string**|  | |

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

## `downloadBundle()`

```php
downloadBundle($id)
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
$id = 56; // int

try {
    $apiInstance->downloadBundle($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->downloadBundle: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/zip`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `downloadCliPlugin()`

```php
downloadCliPlugin($plugin_id, $version)
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
$plugin_id = 'plugin_id_example'; // string
$version = 'version_example'; // string

try {
    $apiInstance->downloadCliPlugin($plugin_id, $version);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->downloadCliPlugin: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_id** | **string**|  | |
| **version** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/java-archive`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `downloadModel()`

```php
downloadModel($provider, $job_id, $output_path)
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
$output_path = 'output_path_example'; // string

try {
    $apiInstance->downloadModel($provider, $job_id, $output_path);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->downloadModel: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
| **job_id** | **string**|  | |
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

## `downloadUiZip()`

```php
downloadUiZip($plugin_id, $build_type)
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
$plugin_id = 'plugin_id_example'; // string
$build_type = 'build_type_example'; // string

try {
    $apiInstance->downloadUiZip($plugin_id, $build_type);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->downloadUiZip: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_id** | **string**|  | |
| **build_type** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/zip`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `enableByPluginIdForOrganization()`

```php
enableByPluginIdForOrganization($plugin_id, $organization_id)
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
$plugin_id = 'plugin_id_example'; // string
$organization_id = 'organization_id_example'; // string

try {
    $apiInstance->enableByPluginIdForOrganization($plugin_id, $organization_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->enableByPluginIdForOrganization: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_id** | **string**|  | |
| **organization_id** | **string**|  | |

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

## `enablePlugin()`

```php
enablePlugin($plugin_id, $build_type)
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
$plugin_id = 'plugin_id_example'; // string
$build_type = 'development'; // string

try {
    $apiInstance->enablePlugin($plugin_id, $build_type);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->enablePlugin: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_id** | **string**|  | |
| **build_type** | **string**|  | [optional] [default to &#39;development&#39;] |

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

## `enablePlugin1()`

```php
enablePlugin1($id)
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
$id = 56; // int

try {
    $apiInstance->enablePlugin1($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->enablePlugin1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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

## `enablePluginForOrganization()`

```php
enablePluginForOrganization($plugin_installation_id, $organization_id)
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
$plugin_installation_id = 56; // int
$organization_id = 'organization_id_example'; // string

try {
    $apiInstance->enablePluginForOrganization($plugin_installation_id, $organization_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->enablePluginForOrganization: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_installation_id** | **int**|  | |
| **organization_id** | **string**|  | |

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
estimateCost($provider, $training_request_bean)
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
$training_request_bean = new \OpenAPI\Client\Model\TrainingRequestBean(); // \OpenAPI\Client\Model\TrainingRequestBean

try {
    $apiInstance->estimateCost($provider, $training_request_bean);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->estimateCost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
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

## `executeDemo()`

```php
executeDemo($pipeline_name, $request_body)
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
$pipeline_name = 'pipeline_name_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->executeDemo($pipeline_name, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->executeDemo: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pipeline_name** | **string**|  | |
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

## `executeJob()`

```php
executeJob($country, $request_body)
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
$country = 'country_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->executeJob($country, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->executeJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **country** | **string**|  | |
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

## `executeJob1()`

```php
executeJob1($project_id, $job_id, $request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->executeJob1($project_id, $job_id, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->executeJob1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
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

## `executeQuery()`

```php
executeQuery($presto_query_request)
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
$presto_query_request = new \OpenAPI\Client\Model\PrestoQueryRequest(); // \OpenAPI\Client\Model\PrestoQueryRequest

try {
    $apiInstance->executeQuery($presto_query_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->executeQuery: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **presto_query_request** | [**\OpenAPI\Client\Model\PrestoQueryRequest**](../Model/PrestoQueryRequest.md)|  | [optional] |

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

## `extractDirect()`

```php
extractDirect($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->extractDirect($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->extractDirect: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `generatePipeline()`

```php
generatePipeline($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->generatePipeline($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->generatePipeline: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `generatePysparkCode()`

```php
generatePysparkCode($extension_id)
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
$extension_id = 'extension_id_example'; // string

try {
    $apiInstance->generatePysparkCode($extension_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->generatePysparkCode: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **extension_id** | **string**|  | |

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
getAgent($category_id, $agent_id)
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

try {
    $apiInstance->getAgent($category_id, $agent_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAgent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |
| **agent_id** | **string**|  | |

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

## `getAgentExtensions()`

```php
getAgentExtensions($agent_id)
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

try {
    $apiInstance->getAgentExtensions($agent_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAgentExtensions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **agent_id** | **string**|  | |

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
getAgentFromName($category_id, $agent_name)
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

try {
    $apiInstance->getAgentFromName($category_id, $agent_name);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAgentFromName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |
| **agent_name** | **string**|  | |

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

## `getAgentPythonExtensions()`

```php
getAgentPythonExtensions($agent_id)
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

try {
    $apiInstance->getAgentPythonExtensions($agent_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAgentPythonExtensions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **agent_id** | **string**|  | |

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
getAllAgents($category_id)
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

try {
    $apiInstance->getAllAgents($category_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllAgents: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |

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
getAllCategories()
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
    $apiInstance->getAllCategories();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllCategories: ', $e->getMessage(), PHP_EOL;
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

## `getAllCloudCredentials()`

```php
getAllCloudCredentials($provider, $page, $page_size)
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
$page = 0; // int
$page_size = 50; // int

try {
    $apiInstance->getAllCloudCredentials($provider, $page, $page_size);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllCloudCredentials: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | [optional] |
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

## `getAllDatasetVersions()`

```php
getAllDatasetVersions()
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
    $apiInstance->getAllDatasetVersions();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllDatasetVersions: ', $e->getMessage(), PHP_EOL;
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

## `getAllDatasets()`

```php
getAllDatasets($status)
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
$status = 'status_example'; // string

try {
    $apiInstance->getAllDatasets($status);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllDatasets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `getAllDatasets1()`

```php
getAllDatasets1($type, $indexed, $format)
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
$type = 'type_example'; // string
$indexed = 'indexed_example'; // string
$format = 'format_example'; // string

try {
    $apiInstance->getAllDatasets1($type, $indexed, $format);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllDatasets1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **type** | **string**|  | [optional] |
| **indexed** | **string**|  | [optional] |
| **format** | **string**|  | [optional] |

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

## `getAllInstallations()`

```php
getAllInstallations($organization_id, $enabled_only)
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
$organization_id = 'organization_id_example'; // string
$enabled_only = True; // bool

try {
    $apiInstance->getAllInstallations($organization_id, $enabled_only);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllInstallations: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | [optional] |
| **enabled_only** | **bool**|  | [optional] |

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
getAllProjects()
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
    $apiInstance->getAllProjects();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllProjects: ', $e->getMessage(), PHP_EOL;
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

## `getAllTasks()`

```php
getAllTasks($project_id, $job_id)
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

try {
    $apiInstance->getAllTasks($project_id, $job_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllTasks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |

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

## `getAllVersions()`

```php
getAllVersions($build_type, $active_only)
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
$build_type = 'build_type_example'; // string
$active_only = True; // bool

try {
    $apiInstance->getAllVersions($build_type, $active_only);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllVersions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **build_type** | **string**|  | [optional] |
| **active_only** | **bool**|  | [optional] |

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
getAllVersionsets($dataset_id)
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

try {
    $apiInstance->getAllVersionsets($dataset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getAllVersionsets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |

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

## `getBillingPlans()`

```php
getBillingPlans($organization_id, $standard)
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
$organization_id = 56; // int
$standard = True; // bool

try {
    $apiInstance->getBillingPlans($organization_id, $standard);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getBillingPlans: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **int**|  | [optional] |
| **standard** | **bool**|  | [optional] |

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

## `getBootstrapStatus()`

```php
getBootstrapStatus()
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
    $apiInstance->getBootstrapStatus();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getBootstrapStatus: ', $e->getMessage(), PHP_EOL;
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

## `getBundleScan()`

```php
getBundleScan($id)
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
$id = 56; // int

try {
    $apiInstance->getBundleScan($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getBundleScan: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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

## `getCapabilities()`

```php
getCapabilities()
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
    $apiInstance->getCapabilities();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getCapabilities: ', $e->getMessage(), PHP_EOL;
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

## `getCatalogStages()`

```php
getCatalogStages($search)
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
$search = 'search_example'; // string

try {
    $apiInstance->getCatalogStages($search);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getCatalogStages: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **search** | **string**|  | [optional] |

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
getCategory($category_id)
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

try {
    $apiInstance->getCategory($category_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getCategory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |

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
getCategoryFromName($category_name)
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

try {
    $apiInstance->getCategoryFromName($category_name);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getCategoryFromName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_name** | **string**|  | |

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

## `getCloudCredentialById()`

```php
getCloudCredentialById($credential_id)
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
$credential_id = 'credential_id_example'; // string

try {
    $apiInstance->getCloudCredentialById($credential_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getCloudCredentialById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **credential_id** | **string**|  | |

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

## `getCloudCredentialsByProvider()`

```php
getCloudCredentialsByProvider($provider)
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

try {
    $apiInstance->getCloudCredentialsByProvider($provider);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getCloudCredentialsByProvider: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |

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

## `getCronJob()`

```php
getCronJob($name, $namespace)
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
$name = 'name_example'; // string
$namespace = 'namespace_example'; // string

try {
    $apiInstance->getCronJob($name, $namespace);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getCronJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**|  | |
| **namespace** | **string**|  | [optional] |

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

## `getCurrentUser()`

```php
getCurrentUser()
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
    $apiInstance->getCurrentUser();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getCurrentUser: ', $e->getMessage(), PHP_EOL;
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

## `getDataset()`

```php
getDataset($dataset_id)
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

try {
    $apiInstance->getDataset($dataset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |

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

## `getDataset1()`

```php
getDataset1($dataset_id)
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

try {
    $apiInstance->getDataset1($dataset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDataset1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |

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

## `getDatasetFields()`

```php
getDatasetFields($dataset_id)
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

try {
    $apiInstance->getDatasetFields($dataset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDatasetFields: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |

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

## `getDatasetInfoByTask()`

```php
getDatasetInfoByTask($task_id)
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
$task_id = 'task_id_example'; // string

try {
    $apiInstance->getDatasetInfoByTask($task_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDatasetInfoByTask: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **task_id** | **string**|  | |

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
getDatasetInputFile($dataset_id)
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

try {
    $apiInstance->getDatasetInputFile($dataset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDatasetInputFile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |

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
getDatasetInputFilePagination($offset, $dataset_id, $limit)
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

try {
    $apiInstance->getDatasetInputFilePagination($offset, $dataset_id, $limit);
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
getDatasetInputFileSize($dataset_id)
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

try {
    $apiInstance->getDatasetInputFileSize($dataset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDatasetInputFileSize: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |

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
getDatasetStatus($dataset_id)
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

try {
    $apiInstance->getDatasetStatus($dataset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getDatasetStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |

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
getDatasetVersionInputFile($category_id, $job_id, $versionset_id, $dataset_id)
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

try {
    $apiInstance->getDatasetVersionInputFile($category_id, $job_id, $versionset_id, $dataset_id);
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
getDatasetVersionInputFilePagination($project_id, $bot_id, $offset, $limit, $versionset_id, $dataset_id)
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

try {
    $apiInstance->getDatasetVersionInputFilePagination($project_id, $bot_id, $offset, $limit, $versionset_id, $dataset_id);
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

## `getEffectiveEntitlements()`

```php
getEffectiveEntitlements($organization_id)
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
$organization_id = 56; // int

try {
    $apiInstance->getEffectiveEntitlements($organization_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getEffectiveEntitlements: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **int**|  | [optional] |

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

## `getExecutionLogs()`

```php
getExecutionLogs($execution_id, $tail, $pod_type, $executor_index)
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
$execution_id = 'execution_id_example'; // string
$tail = 56; // int
$pod_type = 'pod_type_example'; // string
$executor_index = 56; // int

try {
    $apiInstance->getExecutionLogs($execution_id, $tail, $pod_type, $executor_index);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getExecutionLogs: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **execution_id** | **string**|  | |
| **tail** | **int**|  | [optional] |
| **pod_type** | **string**|  | [optional] |
| **executor_index** | **int**|  | [optional] |

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

## `getExecutionLogs1()`

```php
getExecutionLogs1($project_id, $job_id, $execution_id, $pod_type, $executor_index, $pod_name, $tail)
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
$execution_id = 'execution_id_example'; // string
$pod_type = 'pod_type_example'; // string
$executor_index = 56; // int
$pod_name = 'pod_name_example'; // string
$tail = 56; // int

try {
    $apiInstance->getExecutionLogs1($project_id, $job_id, $execution_id, $pod_type, $executor_index, $pod_name, $tail);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getExecutionLogs1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **execution_id** | **string**|  | |
| **pod_type** | **string**|  | [optional] |
| **executor_index** | **int**|  | [optional] |
| **pod_name** | **string**|  | [optional] |
| **tail** | **int**|  | [optional] |

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

## `getExecutionOutput()`

```php
getExecutionOutput($execution_id, $limit, $dataset_id)
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
$execution_id = 'execution_id_example'; // string
$limit = 56; // int
$dataset_id = 56; // int

try {
    $apiInstance->getExecutionOutput($execution_id, $limit, $dataset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getExecutionOutput: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **execution_id** | **string**|  | |
| **limit** | **int**|  | [optional] |
| **dataset_id** | **int**|  | [optional] |

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

## `getExecutionStatus()`

```php
getExecutionStatus($execution_id)
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
$execution_id = 'execution_id_example'; // string

try {
    $apiInstance->getExecutionStatus($execution_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getExecutionStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **execution_id** | **string**|  | |

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

## `getExecutionStatus1()`

```php
getExecutionStatus1($project_id, $job_id, $execution_id)
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
$execution_id = 'execution_id_example'; // string

try {
    $apiInstance->getExecutionStatus1($project_id, $job_id, $execution_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getExecutionStatus1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **execution_id** | **string**|  | |

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

## `getImagesSimplified()`

```php
getImagesSimplified($country, $organization_code, $request_body)
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
$country = 'country_example'; // string
$organization_code = 'organization_code_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->getImagesSimplified($country, $organization_code, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getImagesSimplified: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **country** | **string**|  | |
| **organization_code** | **string**|  | [optional] |
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

## `getInfo()`

```php
getInfo()
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
    $apiInstance->getInfo();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getInfo: ', $e->getMessage(), PHP_EOL;
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

## `getInfo1()`

```php
getInfo1()
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
    $apiInstance->getInfo1();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getInfo1: ', $e->getMessage(), PHP_EOL;
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

## `getInstallationById()`

```php
getInstallationById($id)
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
$id = 56; // int

try {
    $apiInstance->getInstallationById($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getInstallationById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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

## `getJob()`

```php
getJob($project_id, $job_id)
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

try {
    $apiInstance->getJob($project_id, $job_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |

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

## `getJobLogs()`

```php
getJobLogs($project_id, $job_id, $task_id, $pod_type, $executor_index, $pod_name, $tail)
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
$task_id = 56; // int
$pod_type = 'pod_type_example'; // string
$executor_index = 56; // int
$pod_name = 'pod_name_example'; // string
$tail = 56; // int

try {
    $apiInstance->getJobLogs($project_id, $job_id, $task_id, $pod_type, $executor_index, $pod_name, $tail);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getJobLogs: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **task_id** | **int**|  | [optional] |
| **pod_type** | **string**|  | [optional] |
| **executor_index** | **int**|  | [optional] |
| **pod_name** | **string**|  | [optional] |
| **tail** | **int**|  | [optional] |

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

## `getJobMetrics()`

```php
getJobMetrics($project_id, $job_id, $start_time, $end_time)
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
$start_time = 'start_time_example'; // string
$end_time = 'end_time_example'; // string

try {
    $apiInstance->getJobMetrics($project_id, $job_id, $start_time, $end_time);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getJobMetrics: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **start_time** | **string**|  | [optional] |
| **end_time** | **string**|  | [optional] |

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

## `getOrganization()`

```php
getOrganization($id)
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
$id = 'id_example'; // string

try {
    $apiInstance->getOrganization($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getOrganization: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `getOrganizationPlugins()`

```php
getOrganizationPlugins($organization_id)
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
$organization_id = 'organization_id_example'; // string

try {
    $apiInstance->getOrganizationPlugins($organization_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getOrganizationPlugins: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |

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

## `getOrganizationUsers()`

```php
getOrganizationUsers($id)
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
$id = 'id_example'; // string

try {
    $apiInstance->getOrganizationUsers($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getOrganizationUsers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `getPartnersByType()`

```php
getPartnersByType($type)
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
$type = 'type_example'; // string

try {
    $apiInstance->getPartnersByType($type);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getPartnersByType: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **type** | **string**|  | |

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

## `getPluginInfo()`

```php
getPluginInfo()
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
    $apiInstance->getPluginInfo();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getPluginInfo: ', $e->getMessage(), PHP_EOL;
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

## `getPluginInfo1()`

```php
getPluginInfo1()
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
    $apiInstance->getPluginInfo1();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getPluginInfo1: ', $e->getMessage(), PHP_EOL;
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

## `getPluginInfo2()`

```php
getPluginInfo2()
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
    $apiInstance->getPluginInfo2();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getPluginInfo2: ', $e->getMessage(), PHP_EOL;
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

## `getPluginOrganizations()`

```php
getPluginOrganizations($plugin_installation_id)
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
$plugin_installation_id = 56; // int

try {
    $apiInstance->getPluginOrganizations($plugin_installation_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getPluginOrganizations: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_installation_id** | **int**|  | |

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

## `getPluginUsage()`

```php
getPluginUsage($plugin_id, $from, $to, $organization_id, $group_by)
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
$plugin_id = 'plugin_id_example'; // string
$from = 'from_example'; // string
$to = 'to_example'; // string
$organization_id = 'organization_id_example'; // string
$group_by = 'stage'; // string

try {
    $apiInstance->getPluginUsage($plugin_id, $from, $to, $organization_id, $group_by);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getPluginUsage: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_id** | **string**|  | |
| **from** | **string**|  | [optional] |
| **to** | **string**|  | [optional] |
| **organization_id** | **string**|  | [optional] |
| **group_by** | **string**|  | [optional] [default to &#39;stage&#39;] |

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

## `getProfile()`

```php
getProfile($id)
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
$id = 56; // int

try {
    $apiInstance->getProfile($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getProfile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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

## `getProject()`

```php
getProject($project_id)
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

try {
    $apiInstance->getProject($project_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |

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
getProjectFromName($project_name)
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

try {
    $apiInstance->getProjectFromName($project_name);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getProjectFromName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_name** | **string**|  | |

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
getProjectJobs($project_id)
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

try {
    $apiInstance->getProjectJobs($project_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getProjectJobs: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |

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

## `getProjectMetrics()`

```php
getProjectMetrics($project_id, $start_time, $end_time)
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
$start_time = 'start_time_example'; // string
$end_time = 'end_time_example'; // string

try {
    $apiInstance->getProjectMetrics($project_id, $start_time, $end_time);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getProjectMetrics: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **start_time** | **string**|  | [optional] |
| **end_time** | **string**|  | [optional] |

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
getProjectSchedule($project_id)
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

try {
    $apiInstance->getProjectSchedule($project_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getProjectSchedule: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |

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

## `getStage()`

```php
getStage($name)
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
$name = 'name_example'; // string

try {
    $apiInstance->getStage($name);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getStage: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**|  | |

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

## `getStatus()`

```php
getStatus($country)
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
$country = 'country_example'; // string

try {
    $apiInstance->getStatus($country);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **country** | **string**|  | |

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

## `getSupportedExtensionTypes()`

```php
getSupportedExtensionTypes()
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
    $apiInstance->getSupportedExtensionTypes();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getSupportedExtensionTypes: ', $e->getMessage(), PHP_EOL;
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

## `getSupportedModels()`

```php
getSupportedModels($provider)
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

try {
    $apiInstance->getSupportedModels($provider);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getSupportedModels: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |

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
getSupportedProviders()
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
    $apiInstance->getSupportedProviders();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getSupportedProviders: ', $e->getMessage(), PHP_EOL;
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

## `getSystemLogs()`

```php
getSystemLogs($service, $level, $tail, $start_time, $end_time)
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
$service = 'service_example'; // string
$level = 'level_example'; // string
$tail = 56; // int
$start_time = 56; // int
$end_time = 56; // int

try {
    $apiInstance->getSystemLogs($service, $level, $tail, $start_time, $end_time);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getSystemLogs: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **service** | **string**|  | [optional] |
| **level** | **string**|  | [optional] |
| **tail** | **int**|  | [optional] |
| **start_time** | **int**|  | [optional] |
| **end_time** | **int**|  | [optional] |

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

## `getTableColumns()`

```php
getTableColumns($catalog, $schema, $table)
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
$catalog = 'minio'; // string
$schema = 'default'; // string
$table = 'table_example'; // string

try {
    $apiInstance->getTableColumns($catalog, $schema, $table);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getTableColumns: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **catalog** | **string**|  | [optional] [default to &#39;minio&#39;] |
| **schema** | **string**|  | [optional] [default to &#39;default&#39;] |
| **table** | **string**|  | [optional] |

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
getTask($project_id, $job_id, $task_id)
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

try {
    $apiInstance->getTask($project_id, $job_id, $task_id);
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

## `getTaskByOutputDataset()`

```php
getTaskByOutputDataset($dataset_id)
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

try {
    $apiInstance->getTaskByOutputDataset($dataset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getTaskByOutputDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |

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

## `getTaskMetrics()`

```php
getTaskMetrics($project_id, $job_id, $task_id)
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

try {
    $apiInstance->getTaskMetrics($project_id, $job_id, $task_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getTaskMetrics: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **task_id** | **string**|  | |

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
getTaskStatus($project_id, $job_id, $task_id)
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

try {
    $apiInstance->getTaskStatus($project_id, $job_id, $task_id);
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
getTrainingLogs($provider, $job_id)
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

try {
    $apiInstance->getTrainingLogs($provider, $job_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getTrainingLogs: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
| **job_id** | **string**|  | |

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
getTrainingStatus($provider, $job_id)
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

try {
    $apiInstance->getTrainingStatus($provider, $job_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getTrainingStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
| **job_id** | **string**|  | |

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

## `getUiDefinitions()`

```php
getUiDefinitions($organization_id, $build_type)
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
$organization_id = 'organization_id_example'; // string
$build_type = 'build_type_example'; // string

try {
    $apiInstance->getUiDefinitions($organization_id, $build_type);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getUiDefinitions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | [optional] |
| **build_type** | **string**|  | [optional] |

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
getUploadFileUrl($project_id, $bot_id, $attachment_name)
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

try {
    $apiInstance->getUploadFileUrl($project_id, $bot_id, $attachment_name);
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
getUrlDownload()
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
    $apiInstance->getUrlDownload();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getUrlDownload: ', $e->getMessage(), PHP_EOL;
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

## `getUrlUpload()`

```php
getUrlUpload()
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
    $apiInstance->getUrlUpload();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getUrlUpload: ', $e->getMessage(), PHP_EOL;
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

## `getUserInvites()`

```php
getUserInvites()
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
    $apiInstance->getUserInvites();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getUserInvites: ', $e->getMessage(), PHP_EOL;
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

## `getVersionByBuildTypeAndBuildNumber()`

```php
getVersionByBuildTypeAndBuildNumber($build_type, $build_number)
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
$build_type = 'build_type_example'; // string
$build_number = 56; // int

try {
    $apiInstance->getVersionByBuildTypeAndBuildNumber($build_type, $build_number);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getVersionByBuildTypeAndBuildNumber: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **build_type** | **string**|  | |
| **build_number** | **int**|  | |

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

## `getVersionById()`

```php
getVersionById($id)
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
$id = 56; // int

try {
    $apiInstance->getVersionById($id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getVersionById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |

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
getVersionset($versionset_id)
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

try {
    $apiInstance->getVersionset($versionset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getVersionset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **versionset_id** | **string**|  | |

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
getVersionsetFromVersion($dataset_id, $version, $time_period)
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
$time_period = new \OpenAPI\Client\Model\TimePeriod(); // \OpenAPI\Client\Model\TimePeriod

try {
    $apiInstance->getVersionsetFromVersion($dataset_id, $version, $time_period);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getVersionsetFromVersion: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |
| **version** | **string**|  | |
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
getVersionsetFromVersionBase($dataset_id, $version)
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

try {
    $apiInstance->getVersionsetFromVersionBase($dataset_id, $version);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getVersionsetFromVersionBase: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |
| **version** | **string**|  | |

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

## `healthCheck()`

```php
healthCheck()
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
    $apiInstance->healthCheck();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->healthCheck: ', $e->getMessage(), PHP_EOL;
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

## `healthCheck1()`

```php
healthCheck1()
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
    $apiInstance->healthCheck1();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->healthCheck1: ', $e->getMessage(), PHP_EOL;
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

## `indexDataset()`

```php
indexDataset($dataset_id)
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

try {
    $apiInstance->indexDataset($dataset_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->indexDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |

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

## `infer()`

```php
infer($infer_request)
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
$infer_request = new \OpenAPI\Client\Model\InferRequest(); // \OpenAPI\Client\Model\InferRequest

try {
    $apiInstance->infer($infer_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->infer: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **infer_request** | [**\OpenAPI\Client\Model\InferRequest**](../Model/InferRequest.md)|  | [optional] |

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

## `installBundle()`

```php
installBundle($build_type, $bundle, $build_type2, $force)
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
$build_type = 'build_type_example'; // string
$bundle = new \OpenAPI\Client\Model\FormDataContentDisposition(); // \OpenAPI\Client\Model\FormDataContentDisposition
$build_type2 = 'build_type_example'; // string
$force = True; // bool

try {
    $apiInstance->installBundle($build_type, $bundle, $build_type2, $force);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->installBundle: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **build_type** | **string**|  | [optional] |
| **bundle** | [**\OpenAPI\Client\Model\FormDataContentDisposition**](../Model/FormDataContentDisposition.md)|  | [optional] |
| **build_type2** | **string**|  | [optional] |
| **force** | **bool**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `jobCompletionWebhook()`

```php
jobCompletionWebhook($project_id, $job_id, $job_completion_webhook_request)
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
$job_completion_webhook_request = new \OpenAPI\Client\Model\JobCompletionWebhookRequest(); // \OpenAPI\Client\Model\JobCompletionWebhookRequest

try {
    $apiInstance->jobCompletionWebhook($project_id, $job_id, $job_completion_webhook_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->jobCompletionWebhook: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
| **job_completion_webhook_request** | [**\OpenAPI\Client\Model\JobCompletionWebhookRequest**](../Model/JobCompletionWebhookRequest.md)|  | [optional] |

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

## `listAdapters()`

```php
listAdapters()
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
    $apiInstance->listAdapters();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listAdapters: ', $e->getMessage(), PHP_EOL;
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

## `listApiKeys()`

```php
listApiKeys($organization, $organization_code)
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
$organization = 'organization_example'; // string
$organization_code = 'organization_code_example'; // string

try {
    $apiInstance->listApiKeys($organization, $organization_code);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listApiKeys: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization** | **string**|  | [optional] |
| **organization_code** | **string**|  | [optional] |

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

## `listAvailable()`

```php
listAvailable()
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
    $apiInstance->listAvailable();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listAvailable: ', $e->getMessage(), PHP_EOL;
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

## `listBundles()`

```php
listBundles($status)
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
$status = 'status_example'; // string

try {
    $apiInstance->listBundles($status);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listBundles: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `listCharges()`

```php
listCharges($period)
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
$period = 'period_example'; // string

try {
    $apiInstance->listCharges($period);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listCharges: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **period** | **string**|  | [optional] |

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

## `listCliPlugins()`

```php
listCliPlugins()
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
    $apiInstance->listCliPlugins();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listCliPlugins: ', $e->getMessage(), PHP_EOL;
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

## `listCronJobs()`

```php
listCronJobs($namespace)
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
$namespace = 'namespace_example'; // string

try {
    $apiInstance->listCronJobs($namespace);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listCronJobs: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **namespace** | **string**|  | [optional] |

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

## `listDemos()`

```php
listDemos()
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
    $apiInstance->listDemos();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listDemos: ', $e->getMessage(), PHP_EOL;
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

## `listExecutions()`

```php
listExecutions($limit, $organization_id)
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
$limit = 50; // int
$organization_id = 'organization_id_example'; // string

try {
    $apiInstance->listExecutions($limit, $organization_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listExecutions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **int**|  | [optional] [default to 50] |
| **organization_id** | **string**|  | [optional] |

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

## `listMyAdapters()`

```php
listMyAdapters()
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
    $apiInstance->listMyAdapters();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listMyAdapters: ', $e->getMessage(), PHP_EOL;
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

## `listPayouts()`

```php
listPayouts($period)
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
$period = 'period_example'; // string

try {
    $apiInstance->listPayouts($period);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listPayouts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **period** | **string**|  | [optional] |

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

## `listPlugins()`

```php
listPlugins($build_type)
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
$build_type = 'development'; // string

try {
    $apiInstance->listPlugins($build_type);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listPlugins: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **build_type** | **string**|  | [optional] [default to &#39;development&#39;] |

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

## `listProfiles()`

```php
listProfiles($enabled_only, $organization_id)
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
$enabled_only = false; // bool
$organization_id = 'organization_id_example'; // string

try {
    $apiInstance->listProfiles($enabled_only, $organization_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listProfiles: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **enabled_only** | **bool**|  | [optional] [default to false] |
| **organization_id** | **string**|  | [optional] |

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

## `listProviders()`

```php
listProviders()
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
    $apiInstance->listProviders();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listProviders: ', $e->getMessage(), PHP_EOL;
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

## `listRevenueShare()`

```php
listRevenueShare($period)
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
$period = 'period_example'; // string

try {
    $apiInstance->listRevenueShare($period);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listRevenueShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **period** | **string**|  | [optional] |

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

## `listStages()`

```php
listStages($plugin_id, $stage_name, $plugin_type, $scope)
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
$plugin_id = 'plugin_id_example'; // string
$stage_name = 'stage_name_example'; // string
$plugin_type = 'plugin_type_example'; // string
$scope = 'org'; // string

try {
    $apiInstance->listStages($plugin_id, $stage_name, $plugin_type, $scope);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listStages: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_id** | **string**|  | [optional] |
| **stage_name** | **string**|  | [optional] |
| **plugin_type** | **string**|  | [optional] |
| **scope** | **string**|  | [optional] [default to &#39;org&#39;] |

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

## `listStages1()`

```php
listStages1($category, $type, $search)
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
$category = 'category_example'; // string
$type = 'type_example'; // string
$search = 'search_example'; // string

try {
    $apiInstance->listStages1($category, $type, $search);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listStages1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category** | **string**|  | [optional] |
| **type** | **string**|  | [optional] |
| **search** | **string**|  | [optional] |

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

## `listTables()`

```php
listTables($catalog, $schema)
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
$catalog = 'minio'; // string
$schema = 'default'; // string

try {
    $apiInstance->listTables($catalog, $schema);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->listTables: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **catalog** | **string**|  | [optional] [default to &#39;minio&#39;] |
| **schema** | **string**|  | [optional] [default to &#39;default&#39;] |

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

## `markFailed()`

```php
markFailed($invoice_id, $reason)
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
$invoice_id = 'invoice_id_example'; // string
$reason = 'reason_example'; // string

try {
    $apiInstance->markFailed($invoice_id, $reason);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->markFailed: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **invoice_id** | **string**|  | |
| **reason** | **string**|  | [optional] |

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

## `markPaid()`

```php
markPaid($invoice_id)
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
$invoice_id = 'invoice_id_example'; // string

try {
    $apiInstance->markPaid($invoice_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->markPaid: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **invoice_id** | **string**|  | |

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

## `markZombieTasks()`

```php
markZombieTasks($timeout_hours)
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
$timeout_hours = 56; // int

try {
    $apiInstance->markZombieTasks($timeout_hours);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->markZombieTasks: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **timeout_hours** | **int**|  | [optional] |

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

## `probeAdapter()`

```php
probeAdapter($provider_key)
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
$provider_key = 'provider_key_example'; // string

try {
    $apiInstance->probeAdapter($provider_key);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->probeAdapter: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider_key** | **string**|  | |

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

## `processYamlExtensions()`

```php
processYamlExtensions($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->processYamlExtensions($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->processYamlExtensions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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
publishModel($model_publish_request)
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
$model_publish_request = new \OpenAPI\Client\Model\ModelPublishRequest(); // \OpenAPI\Client\Model\ModelPublishRequest

try {
    $apiInstance->publishModel($model_publish_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->publishModel: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `queryDatasetByTask()`

```php
queryDatasetByTask($task_id, $presto_query_request)
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
$task_id = 'task_id_example'; // string
$presto_query_request = new \OpenAPI\Client\Model\PrestoQueryRequest(); // \OpenAPI\Client\Model\PrestoQueryRequest

try {
    $apiInstance->queryDatasetByTask($task_id, $presto_query_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->queryDatasetByTask: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **task_id** | **string**|  | |
| **presto_query_request** | [**\OpenAPI\Client\Model\PrestoQueryRequest**](../Model/PrestoQueryRequest.md)|  | [optional] |

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

## `queryImages()`

```php
queryImages($country, $organization_code, $request_body)
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
$country = 'country_example'; // string
$organization_code = 'organization_code_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->queryImages($country, $organization_code, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->queryImages: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **country** | **string**|  | |
| **organization_code** | **string**|  | [optional] |
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

## `refreshOrganizationsBillingStatus()`

```php
refreshOrganizationsBillingStatus()
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
    $apiInstance->refreshOrganizationsBillingStatus();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->refreshOrganizationsBillingStatus: ', $e->getMessage(), PHP_EOL;
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

## `refund()`

```php
refund($id, $amount_cents, $reason)
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
$id = 56; // int
$amount_cents = 56; // int
$reason = 'reason_example'; // string

try {
    $apiInstance->refund($id, $amount_cents, $reason);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->refund: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |
| **amount_cents** | **int**|  | [optional] |
| **reason** | **string**|  | [optional] |

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

## `registerPlugin()`

```php
registerPlugin($plugin_installation)
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
$plugin_installation = new \OpenAPI\Client\Model\PluginInstallation(); // \OpenAPI\Client\Model\PluginInstallation

try {
    $apiInstance->registerPlugin($plugin_installation);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->registerPlugin: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **plugin_installation** | [**\OpenAPI\Client\Model\PluginInstallation**](../Model/PluginInstallation.md)|  | [optional] |

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

## `registerPythonExtension()`

```php
registerPythonExtension($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->registerPythonExtension($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->registerPythonExtension: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `rejectBundle()`

```php
rejectBundle($id, $request_body)
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
$id = 56; // int
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->rejectBundle($id, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->rejectBundle: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |
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

## `reloadPipelines()`

```php
reloadPipelines()
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
    $apiInstance->reloadPipelines();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->reloadPipelines: ', $e->getMessage(), PHP_EOL;
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

## `reloadPlugins()`

```php
reloadPlugins()
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
    $apiInstance->reloadPlugins();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->reloadPlugins: ', $e->getMessage(), PHP_EOL;
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

## `removeJobFromProject()`

```php
removeJobFromProject($project_id, $job_id)
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

try {
    $apiInstance->removeJobFromProject($project_id, $job_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->removeJobFromProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |

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

## `reportHealth()`

```php
reportHealth($provider_key, $request_body)
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
$provider_key = 'provider_key_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->reportHealth($provider_key, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->reportHealth: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider_key** | **string**|  | |
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

## `rescheduleEvents()`

```php
rescheduleEvents($reschedule_events_request)
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
$reschedule_events_request = new \OpenAPI\Client\Model\RescheduleEventsRequest(); // \OpenAPI\Client\Model\RescheduleEventsRequest

try {
    $apiInstance->rescheduleEvents($reschedule_events_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->rescheduleEvents: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **reschedule_events_request** | [**\OpenAPI\Client\Model\RescheduleEventsRequest**](../Model/RescheduleEventsRequest.md)|  | [optional] |

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

## `rollup()`

```php
rollup($day)
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
$day = 'day_example'; // string

try {
    $apiInstance->rollup($day);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->rollup: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **day** | **string**|  | [optional] |

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

## `runCharges()`

```php
runCharges($period, $dry_run)
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
$period = 'period_example'; // string
$dry_run = false; // bool

try {
    $apiInstance->runCharges($period, $dry_run);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->runCharges: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **period** | **string**|  | [optional] |
| **dry_run** | **bool**|  | [optional] [default to false] |

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

## `runHealthCheck()`

```php
runHealthCheck()
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
    $apiInstance->runHealthCheck();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->runHealthCheck: ', $e->getMessage(), PHP_EOL;
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

## `runOrchestrationCharges()`

```php
runOrchestrationCharges($period, $dry_run)
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
$period = 'period_example'; // string
$dry_run = false; // bool

try {
    $apiInstance->runOrchestrationCharges($period, $dry_run);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->runOrchestrationCharges: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **period** | **string**|  | [optional] |
| **dry_run** | **bool**|  | [optional] [default to false] |

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

## `runPayouts()`

```php
runPayouts($period, $dry_run)
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
$period = 'period_example'; // string
$dry_run = false; // bool

try {
    $apiInstance->runPayouts($period, $dry_run);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->runPayouts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **period** | **string**|  | [optional] |
| **dry_run** | **bool**|  | [optional] [default to false] |

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

## `runProviderEndpointCharges()`

```php
runProviderEndpointCharges($period, $dry_run)
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
$period = 'period_example'; // string
$dry_run = false; // bool

try {
    $apiInstance->runProviderEndpointCharges($period, $dry_run);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->runProviderEndpointCharges: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **period** | **string**|  | [optional] |
| **dry_run** | **bool**|  | [optional] [default to false] |

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

## `runRevenueShare()`

```php
runRevenueShare($period, $dry_run)
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
$period = 'period_example'; // string
$dry_run = false; // bool

try {
    $apiInstance->runRevenueShare($period, $dry_run);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->runRevenueShare: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **period** | **string**|  | [optional] |
| **dry_run** | **bool**|  | [optional] [default to false] |

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

## `saveGeneratedPipeline()`

```php
saveGeneratedPipeline($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->saveGeneratedPipeline($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->saveGeneratedPipeline: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `scheduleJob()`

```php
scheduleJob($country, $request_body)
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
$country = 'country_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->scheduleJob($country, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->scheduleJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **country** | **string**|  | |
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

## `serveDemoApp()`

```php
serveDemoApp()
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
    $apiInstance->serveDemoApp();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->serveDemoApp: ', $e->getMessage(), PHP_EOL;
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

## `serveStaticFile()`

```php
serveStaticFile($filename)
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
$filename = 'filename_example'; // string

try {
    $apiInstance->serveStaticFile($filename);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->serveStaticFile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **filename** | **string**|  | |

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
setProjectSchedule($project_id, $project_schedule_request)
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
$project_schedule_request = new \OpenAPI\Client\Model\ProjectScheduleRequest(); // \OpenAPI\Client\Model\ProjectScheduleRequest

try {
    $apiInstance->setProjectSchedule($project_id, $project_schedule_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->setProjectSchedule: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
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

## `start()`

```php
start($start_request)
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
$start_request = new \OpenAPI\Client\Model\StartRequest(); // \OpenAPI\Client\Model\StartRequest

try {
    $apiInstance->start($start_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->start: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **start_request** | [**\OpenAPI\Client\Model\StartRequest**](../Model/StartRequest.md)|  | [optional] |

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
startExportAll()
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
    $apiInstance->startExportAll();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startExportAll: ', $e->getMessage(), PHP_EOL;
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

## `startExportOrganization()`

```php
startExportOrganization($organization_id)
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
$organization_id = 'organization_id_example'; // string

try {
    $apiInstance->startExportOrganization($organization_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startExportOrganization: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |

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

## `startExportOrganizationWithOptions()`

```php
startExportOrganizationWithOptions($organization_id, $export_options_dto)
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
$organization_id = 'organization_id_example'; // string
$export_options_dto = new \OpenAPI\Client\Model\ExportOptionsDto(); // \OpenAPI\Client\Model\ExportOptionsDto

try {
    $apiInstance->startExportOrganizationWithOptions($organization_id, $export_options_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startExportOrganizationWithOptions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **export_options_dto** | [**\OpenAPI\Client\Model\ExportOptionsDto**](../Model/ExportOptionsDto.md)|  | [optional] |

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

## `startExportProject()`

```php
startExportProject($project_id)
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

try {
    $apiInstance->startExportProject($project_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startExportProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |

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
startImportAll()
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
    $apiInstance->startImportAll();
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startImportAll: ', $e->getMessage(), PHP_EOL;
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

## `startImportAllWithOptions()`

```php
startImportAllWithOptions($import_options_dto)
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
$import_options_dto = new \OpenAPI\Client\Model\ImportOptionsDto(); // \OpenAPI\Client\Model\ImportOptionsDto

try {
    $apiInstance->startImportAllWithOptions($import_options_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startImportAllWithOptions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **import_options_dto** | [**\OpenAPI\Client\Model\ImportOptionsDto**](../Model/ImportOptionsDto.md)|  | [optional] |

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

## `startImportOrganization()`

```php
startImportOrganization($organization_id)
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
$organization_id = 'organization_id_example'; // string

try {
    $apiInstance->startImportOrganization($organization_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startImportOrganization: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |

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

## `startImportOrganizationWithOptions()`

```php
startImportOrganizationWithOptions($organization_id, $filename, $import_options_dto)
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
$organization_id = 'organization_id_example'; // string
$filename = 'filename_example'; // string
$import_options_dto = new \OpenAPI\Client\Model\ImportOptionsDto(); // \OpenAPI\Client\Model\ImportOptionsDto

try {
    $apiInstance->startImportOrganizationWithOptions($organization_id, $filename, $import_options_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startImportOrganizationWithOptions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **organization_id** | **string**|  | |
| **filename** | **string**|  | [optional] |
| **import_options_dto** | [**\OpenAPI\Client\Model\ImportOptionsDto**](../Model/ImportOptionsDto.md)|  | [optional] |

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

## `startImportProject()`

```php
startImportProject($project_id)
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

try {
    $apiInstance->startImportProject($project_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startImportProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |

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

## `startImportProjectWithOptions()`

```php
startImportProjectWithOptions($project_id, $filename, $import_options_dto)
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
$filename = 'filename_example'; // string
$import_options_dto = new \OpenAPI\Client\Model\ImportOptionsDto(); // \OpenAPI\Client\Model\ImportOptionsDto

try {
    $apiInstance->startImportProjectWithOptions($project_id, $filename, $import_options_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startImportProjectWithOptions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **filename** | **string**|  | [optional] |
| **import_options_dto** | [**\OpenAPI\Client\Model\ImportOptionsDto**](../Model/ImportOptionsDto.md)|  | [optional] |

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

## `startTask()`

```php
startTask($project_id, $job_id, $task_id)
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

try {
    $apiInstance->startTask($project_id, $job_id, $task_id);
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
startTraining($provider, $training_request_bean)
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
$training_request_bean = new \OpenAPI\Client\Model\TrainingRequestBean(); // \OpenAPI\Client\Model\TrainingRequestBean

try {
    $apiInstance->startTraining($provider, $training_request_bean);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->startTraining: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
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

## `status()`

```php
status($eid)
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
$eid = 'eid_example'; // string

try {
    $apiInstance->status($eid);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->status: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **eid** | **string**|  | |

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

## `stopJob()`

```php
stopJob($project_id, $job_id)
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

try {
    $apiInstance->stopJob($project_id, $job_id);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->stopJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |

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

## `stopTask()`

```php
stopTask($project_id, $job_id, $task_id)
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

try {
    $apiInstance->stopTask($project_id, $job_id, $task_id);
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

## `suggestStages()`

```php
suggestStages($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->suggestStages($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->suggestStages: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `testCloudCredential()`

```php
testCloudCredential($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->testCloudCredential($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->testCloudCredential: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `updateAdapter()`

```php
updateAdapter($provider_key, $request_body)
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
$provider_key = 'provider_key_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->updateAdapter($provider_key, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateAdapter: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider_key** | **string**|  | |
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
updateAgent($category_id, $agent_id, $agent_dto)
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
$agent_dto = new \OpenAPI\Client\Model\AgentDto(); // \OpenAPI\Client\Model\AgentDto

try {
    $apiInstance->updateAgent($category_id, $agent_id, $agent_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateAgent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |
| **agent_id** | **string**|  | |
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

## `updateAgentPythonExtensions()`

```php
updateAgentPythonExtensions($agent_id, $request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->updateAgentPythonExtensions($agent_id, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateAgentPythonExtensions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **agent_id** | **string**|  | |
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

## `updateBillingPlan()`

```php
updateBillingPlan($id, $request_body)
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
$id = 56; // int
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->updateBillingPlan($id, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateBillingPlan: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |
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

## `updateCategory()`

```php
updateCategory($category_id, $job_category_dto)
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
$job_category_dto = new \OpenAPI\Client\Model\JobCategoryDto(); // \OpenAPI\Client\Model\JobCategoryDto

try {
    $apiInstance->updateCategory($category_id, $job_category_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateCategory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**|  | |
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

## `updateCloudCredential()`

```php
updateCloudCredential($credential_id, $cloud_credential)
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
$credential_id = 'credential_id_example'; // string
$cloud_credential = new \OpenAPI\Client\Model\CloudCredential(); // \OpenAPI\Client\Model\CloudCredential

try {
    $apiInstance->updateCloudCredential($credential_id, $cloud_credential);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateCloudCredential: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **credential_id** | **string**|  | |
| **cloud_credential** | [**\OpenAPI\Client\Model\CloudCredential**](../Model/CloudCredential.md)|  | [optional] |

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

## `updateDataset()`

```php
updateDataset($dataset_id, $dataset_dto)
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
$dataset_dto = new \OpenAPI\Client\Model\DatasetDto(); // \OpenAPI\Client\Model\DatasetDto

try {
    $apiInstance->updateDataset($dataset_id, $dataset_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**|  | |
| **dataset_dto** | [**\OpenAPI\Client\Model\DatasetDto**](../Model/DatasetDto.md)|  | [optional] |

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

## `updateInstallation()`

```php
updateInstallation($id, $plugin_installation)
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
$id = 56; // int
$plugin_installation = new \OpenAPI\Client\Model\PluginInstallation(); // \OpenAPI\Client\Model\PluginInstallation

try {
    $apiInstance->updateInstallation($id, $plugin_installation);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateInstallation: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |
| **plugin_installation** | [**\OpenAPI\Client\Model\PluginInstallation**](../Model/PluginInstallation.md)|  | [optional] |

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

## `updateJob()`

```php
updateJob($project_id, $job_id, $job_dto)
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
$job_dto = new \OpenAPI\Client\Model\JobDto(); // \OpenAPI\Client\Model\JobDto

try {
    $apiInstance->updateJob($project_id, $job_id, $job_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
| **job_id** | **string**|  | |
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

## `updateOrganization()`

```php
updateOrganization($id, $request_body)
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
$id = 'id_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->updateOrganization($id, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateOrganization: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `updateProfile()`

```php
updateProfile($id, $agentic_profile)
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
$id = 56; // int
$agentic_profile = new \OpenAPI\Client\Model\AgenticProfile(); // \OpenAPI\Client\Model\AgenticProfile

try {
    $apiInstance->updateProfile($id, $agentic_profile);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateProfile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |
| **agentic_profile** | [**\OpenAPI\Client\Model\AgenticProfile**](../Model/AgenticProfile.md)|  | [optional] |

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
updateProject($project_id, $job_project_dto)
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
$job_project_dto = new \OpenAPI\Client\Model\JobProjectDto(); // \OpenAPI\Client\Model\JobProjectDto

try {
    $apiInstance->updateProject($project_id, $job_project_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateProject: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **project_id** | **string**|  | |
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

## `updatePythonExtension()`

```php
updatePythonExtension($extension_id, $request_body)
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
$extension_id = 'extension_id_example'; // string
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->updatePythonExtension($extension_id, $request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updatePythonExtension: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **extension_id** | **string**|  | |
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

## `updateTask()`

```php
updateTask($project_id, $job_id, $task_id, $task_dto)
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
$task_dto = new \OpenAPI\Client\Model\TaskDto(); // \OpenAPI\Client\Model\TaskDto

try {
    $apiInstance->updateTask($project_id, $job_id, $task_id, $task_dto);
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

## `updateVersion()`

```php
updateVersion($id, $etl_library_version_api_dto)
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
$id = 56; // int
$etl_library_version_api_dto = new \OpenAPI\Client\Model\EtlLibraryVersionApiDto(); // \OpenAPI\Client\Model\EtlLibraryVersionApiDto

try {
    $apiInstance->updateVersion($id, $etl_library_version_api_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->updateVersion: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **int**|  | |
| **etl_library_version_api_dto** | [**\OpenAPI\Client\Model\EtlLibraryVersionApiDto**](../Model/EtlLibraryVersionApiDto.md)|  | [optional] |

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

## `uploadCsv()`

```php
uploadCsv($country, $organization_code, $content_disposition, $entity, $headers, $media_type, $message_body_workers, $parent, $providers, $body_parts, $fields, $parameterized_headers)
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
$country = 'country_example'; // string
$organization_code = 'organization_code_example'; // string
$content_disposition = new \OpenAPI\Client\Model\ContentDisposition(); // \OpenAPI\Client\Model\ContentDisposition
$entity = array('key' => new \stdClass); // object
$headers = NULL; // array<string,string[]>
$media_type = new \OpenAPI\Client\Model\BodyPartMediaType(); // \OpenAPI\Client\Model\BodyPartMediaType
$message_body_workers = array('key' => new \stdClass); // object
$parent = new \OpenAPI\Client\Model\MultiPart(); // \OpenAPI\Client\Model\MultiPart
$providers = array('key' => new \stdClass); // object
$body_parts = array(new \OpenAPI\Client\Model\\OpenAPI\Client\Model\BodyPart()); // \OpenAPI\Client\Model\BodyPart[]
$fields = NULL; // array<string,\OpenAPI\Client\Model\FormDataBodyPart[]>
$parameterized_headers = NULL; // array<string,\OpenAPI\Client\Model\ParameterizedHeader[]>

try {
    $apiInstance->uploadCsv($country, $organization_code, $content_disposition, $entity, $headers, $media_type, $message_body_workers, $parent, $providers, $body_parts, $fields, $parameterized_headers);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->uploadCsv: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **country** | **string**|  | |
| **organization_code** | **string**|  | [optional] |
| **content_disposition** | [**\OpenAPI\Client\Model\ContentDisposition**](../Model/ContentDisposition.md)|  | [optional] |
| **entity** | [**object**](../Model/object.md)|  | [optional] |
| **headers** | [**array<string,string[]>**](../Model/array.md)|  | [optional] |
| **media_type** | [**\OpenAPI\Client\Model\BodyPartMediaType**](../Model/BodyPartMediaType.md)|  | [optional] |
| **message_body_workers** | [**object**](../Model/object.md)|  | [optional] |
| **parent** | [**\OpenAPI\Client\Model\MultiPart**](../Model/MultiPart.md)|  | [optional] |
| **providers** | [**object**](../Model/object.md)|  | [optional] |
| **body_parts** | [**\OpenAPI\Client\Model\BodyPart[]**](../Model/\OpenAPI\Client\Model\BodyPart.md)|  | [optional] |
| **fields** | [**array<string,\OpenAPI\Client\Model\FormDataBodyPart[]>**](../Model/array.md)|  | [optional] |
| **parameterized_headers** | [**array<string,\OpenAPI\Client\Model\ParameterizedHeader[]>**](../Model/array.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `uploadDataset()`

```php
uploadDataset($pipeline_name, $content_disposition, $entity, $headers, $media_type, $message_body_workers, $parent, $providers, $body_parts, $fields, $parameterized_headers)
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
$pipeline_name = 'pipeline_name_example'; // string
$content_disposition = new \OpenAPI\Client\Model\ContentDisposition(); // \OpenAPI\Client\Model\ContentDisposition
$entity = array('key' => new \stdClass); // object
$headers = NULL; // array<string,string[]>
$media_type = new \OpenAPI\Client\Model\BodyPartMediaType(); // \OpenAPI\Client\Model\BodyPartMediaType
$message_body_workers = array('key' => new \stdClass); // object
$parent = new \OpenAPI\Client\Model\MultiPart(); // \OpenAPI\Client\Model\MultiPart
$providers = array('key' => new \stdClass); // object
$body_parts = array(new \OpenAPI\Client\Model\\OpenAPI\Client\Model\BodyPart()); // \OpenAPI\Client\Model\BodyPart[]
$fields = NULL; // array<string,\OpenAPI\Client\Model\FormDataBodyPart[]>
$parameterized_headers = NULL; // array<string,\OpenAPI\Client\Model\ParameterizedHeader[]>

try {
    $apiInstance->uploadDataset($pipeline_name, $content_disposition, $entity, $headers, $media_type, $message_body_workers, $parent, $providers, $body_parts, $fields, $parameterized_headers);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->uploadDataset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pipeline_name** | **string**|  | |
| **content_disposition** | [**\OpenAPI\Client\Model\ContentDisposition**](../Model/ContentDisposition.md)|  | [optional] |
| **entity** | [**object**](../Model/object.md)|  | [optional] |
| **headers** | [**array<string,string[]>**](../Model/array.md)|  | [optional] |
| **media_type** | [**\OpenAPI\Client\Model\BodyPartMediaType**](../Model/BodyPartMediaType.md)|  | [optional] |
| **message_body_workers** | [**object**](../Model/object.md)|  | [optional] |
| **parent** | [**\OpenAPI\Client\Model\MultiPart**](../Model/MultiPart.md)|  | [optional] |
| **providers** | [**object**](../Model/object.md)|  | [optional] |
| **body_parts** | [**\OpenAPI\Client\Model\BodyPart[]**](../Model/\OpenAPI\Client\Model\BodyPart.md)|  | [optional] |
| **fields** | [**array<string,\OpenAPI\Client\Model\FormDataBodyPart[]>**](../Model/array.md)|  | [optional] |
| **parameterized_headers** | [**array<string,\OpenAPI\Client\Model\ParameterizedHeader[]>**](../Model/array.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `uploadDataset1()`

```php
uploadDataset1($provider, $dataset_upload_request)
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
$dataset_upload_request = new \OpenAPI\Client\Model\DatasetUploadRequest(); // \OpenAPI\Client\Model\DatasetUploadRequest

try {
    $apiInstance->uploadDataset1($provider, $dataset_upload_request);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->uploadDataset1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **provider** | **string**|  | |
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

## `uploadDataset2()`

```php
uploadDataset2($dataset_upload_api_dto)
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
$dataset_upload_api_dto = new \OpenAPI\Client\Model\DatasetUploadApiDto(); // \OpenAPI\Client\Model\DatasetUploadApiDto

try {
    $apiInstance->uploadDataset2($dataset_upload_api_dto);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->uploadDataset2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `uploadDatasetFile()`

```php
uploadDatasetFile($content_disposition, $entity, $headers, $media_type, $message_body_workers, $parent, $providers, $body_parts, $fields, $parameterized_headers)
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
$content_disposition = new \OpenAPI\Client\Model\ContentDisposition(); // \OpenAPI\Client\Model\ContentDisposition
$entity = array('key' => new \stdClass); // object
$headers = NULL; // array<string,string[]>
$media_type = new \OpenAPI\Client\Model\BodyPartMediaType(); // \OpenAPI\Client\Model\BodyPartMediaType
$message_body_workers = array('key' => new \stdClass); // object
$parent = new \OpenAPI\Client\Model\MultiPart(); // \OpenAPI\Client\Model\MultiPart
$providers = array('key' => new \stdClass); // object
$body_parts = array(new \OpenAPI\Client\Model\\OpenAPI\Client\Model\BodyPart()); // \OpenAPI\Client\Model\BodyPart[]
$fields = NULL; // array<string,\OpenAPI\Client\Model\FormDataBodyPart[]>
$parameterized_headers = NULL; // array<string,\OpenAPI\Client\Model\ParameterizedHeader[]>

try {
    $apiInstance->uploadDatasetFile($content_disposition, $entity, $headers, $media_type, $message_body_workers, $parent, $providers, $body_parts, $fields, $parameterized_headers);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->uploadDatasetFile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **content_disposition** | [**\OpenAPI\Client\Model\ContentDisposition**](../Model/ContentDisposition.md)|  | [optional] |
| **entity** | [**object**](../Model/object.md)|  | [optional] |
| **headers** | [**array<string,string[]>**](../Model/array.md)|  | [optional] |
| **media_type** | [**\OpenAPI\Client\Model\BodyPartMediaType**](../Model/BodyPartMediaType.md)|  | [optional] |
| **message_body_workers** | [**object**](../Model/object.md)|  | [optional] |
| **parent** | [**\OpenAPI\Client\Model\MultiPart**](../Model/MultiPart.md)|  | [optional] |
| **providers** | [**object**](../Model/object.md)|  | [optional] |
| **body_parts** | [**\OpenAPI\Client\Model\BodyPart[]**](../Model/\OpenAPI\Client\Model\BodyPart.md)|  | [optional] |
| **fields** | [**array<string,\OpenAPI\Client\Model\FormDataBodyPart[]>**](../Model/array.md)|  | [optional] |
| **parameterized_headers** | [**array<string,\OpenAPI\Client\Model\ParameterizedHeader[]>**](../Model/array.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `uploadFile()`

```php
uploadFile($file)
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
$file = new \OpenAPI\Client\Model\FormDataContentDisposition(); // \OpenAPI\Client\Model\FormDataContentDisposition

try {
    $apiInstance->uploadFile($file);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->uploadFile: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **file** | [**\OpenAPI\Client\Model\FormDataContentDisposition**](../Model/FormDataContentDisposition.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `uploadPlugin()`

```php
uploadPlugin($file, $plugin_id, $plugin_type, $build_type, $build_number, $organization_ids)
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
$file = new \OpenAPI\Client\Model\FormDataContentDisposition(); // \OpenAPI\Client\Model\FormDataContentDisposition
$plugin_id = 'plugin_id_example'; // string
$plugin_type = 'api'; // string
$build_type = 'development'; // string
$build_number = 56; // int
$organization_ids = 'organization_ids_example'; // string

try {
    $apiInstance->uploadPlugin($file, $plugin_id, $plugin_type, $build_type, $build_number, $organization_ids);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->uploadPlugin: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **file** | [**\OpenAPI\Client\Model\FormDataContentDisposition**](../Model/FormDataContentDisposition.md)|  | [optional] |
| **plugin_id** | **string**|  | [optional] |
| **plugin_type** | **string**|  | [optional] [default to &#39;api&#39;] |
| **build_type** | **string**|  | [optional] [default to &#39;development&#39;] |
| **build_number** | **int**|  | [optional] |
| **organization_ids** | **string**|  | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `validate()`

```php
validate($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->validate($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->validate: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `validatePythonExtension()`

```php
validatePythonExtension($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->validatePythonExtension($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->validatePythonExtension: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `wizardInferActions()`

```php
wizardInferActions($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->wizardInferActions($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->wizardInferActions: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `wizardInferFields()`

```php
wizardInferFields($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->wizardInferFields($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->wizardInferFields: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `wizardInferSegment()`

```php
wizardInferSegment($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->wizardInferSegment($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->wizardInferSegment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `wizardInferSelector()`

```php
wizardInferSelector($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->wizardInferSelector($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->wizardInferSelector: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `wizardProxy()`

```php
wizardProxy($url, $strategy)
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
$url = 'url_example'; // string
$strategy = 'strategy_example'; // string

try {
    $apiInstance->wizardProxy($url, $strategy);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->wizardProxy: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **url** | **string**|  | [optional] |
| **strategy** | **string**|  | [optional] |

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

## `wizardSuggestFieldNames()`

```php
wizardSuggestFieldNames($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->wizardSuggestFieldNames($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->wizardSuggestFieldNames: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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

## `wizardValidate()`

```php
wizardValidate($request_body)
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
$request_body = array('key' => new \stdClass); // array<string,object>

try {
    $apiInstance->wizardValidate($request_body);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->wizardValidate: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
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
