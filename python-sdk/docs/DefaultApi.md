# webrobot.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_job_to_project**](DefaultApi.md#add_job_to_project) | **POST** /webrobot/api/projects/id/{projectId}/jobs | 
[**apply**](DefaultApi.md#apply) | **POST** /webrobot/api/manifest/apply | 
[**apply_migrations**](DefaultApi.md#apply_migrations) | **POST** /webrobot/api/admin/bundles/{id}/apply-migrations | 
[**approve_bundle**](DefaultApi.md#approve_bundle) | **POST** /webrobot/api/admin/bundles/{id}/approve | 
[**assign_user_to_organization**](DefaultApi.md#assign_user_to_organization) | **POST** /webrobot/api/auth/organizations/{id}/assign-user | 
[**bootstrap_for_organization**](DefaultApi.md#bootstrap_for_organization) | **POST** /webrobot/api/ean-image-sourcing/bootstrap/organization/{organizationId} | 
[**cancel**](DefaultApi.md#cancel) | **DELETE** /webrobot/api/agentic/{eid} | 
[**cancel_execution**](DefaultApi.md#cancel_execution) | **DELETE** /webrobot/api/demo/executions/{executionId} | 
[**cancel_execution1**](DefaultApi.md#cancel_execution1) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/executions/{executionId} | 
[**cancel_training**](DefaultApi.md#cancel_training) | **DELETE** /webrobot/api/ai-providers/providers/{provider}/training/{jobId} | 
[**cmf_close**](DefaultApi.md#cmf_close) | **DELETE** /webrobot/api/demo/wizard/cmf/{sessionId} | 
[**cmf_open**](DefaultApi.md#cmf_open) | **POST** /webrobot/api/demo/wizard/cmf/open | 
[**cmf_step**](DefaultApi.md#cmf_step) | **POST** /webrobot/api/demo/wizard/cmf/step | 
[**completion**](DefaultApi.md#completion) | **POST** /webrobot/api/agentic/{eid}/completion | 
[**copy_agent**](DefaultApi.md#copy_agent) | **POST** /webrobot/api/agents/{agentId}/copy | 
[**create_agent**](DefaultApi.md#create_agent) | **POST** /webrobot/api/agents | 
[**create_api_key**](DefaultApi.md#create_api_key) | **POST** /webrobot/api/auth/api-keys | 
[**create_billing_plan**](DefaultApi.md#create_billing_plan) | **POST** /webrobot/api/billing/plans | 
[**create_category**](DefaultApi.md#create_category) | **POST** /webrobot/api/categories | 
[**create_cloud_credential**](DefaultApi.md#create_cloud_credential) | **POST** /webrobot/api/cloud-credentials | 
[**create_cron_job**](DefaultApi.md#create_cron_job) | **POST** /webrobot/cloud/scheduler/cronjobs | 
[**create_custom_plan**](DefaultApi.md#create_custom_plan) | **POST** /webrobot/api/billing/custom-plan | 
[**create_dataset**](DefaultApi.md#create_dataset) | **POST** /webrobot/api/datasets | 
[**create_or_update_version**](DefaultApi.md#create_or_update_version) | **POST** /webrobot/api/admin/etl-library-versions | 
[**create_organization**](DefaultApi.md#create_organization) | **POST** /webrobot/api/auth/organizations | 
[**create_profile**](DefaultApi.md#create_profile) | **POST** /webrobot/api/agentic/profiles | 
[**create_project**](DefaultApi.md#create_project) | **POST** /webrobot/api/projects | 
[**create_task**](DefaultApi.md#create_task) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks | 
[**decrypt_field**](DefaultApi.md#decrypt_field) | **POST** /webrobot/api/cloud-credentials/id/{credentialId}/decrypt-field | 
[**delete**](DefaultApi.md#delete) | **DELETE** /api/strapi-tables/{table}/{id} | 
[**delete_agent**](DefaultApi.md#delete_agent) | **DELETE** /webrobot/api/agents/{agentId} | 
[**delete_api_key**](DefaultApi.md#delete_api_key) | **DELETE** /webrobot/api/auth/api-keys/{key_id} | 
[**delete_billing_plan**](DefaultApi.md#delete_billing_plan) | **DELETE** /webrobot/api/billing/plans/{id} | 
[**delete_category**](DefaultApi.md#delete_category) | **DELETE** /webrobot/api/categories/id/{categoryId} | 
[**delete_cloud_credential**](DefaultApi.md#delete_cloud_credential) | **DELETE** /webrobot/api/cloud-credentials/id/{credentialId} | 
[**delete_cron_job**](DefaultApi.md#delete_cron_job) | **DELETE** /webrobot/cloud/scheduler/cronjobs/{name} | 
[**delete_dataset**](DefaultApi.md#delete_dataset) | **DELETE** /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId} | 
[**delete_dataset1**](DefaultApi.md#delete_dataset1) | **DELETE** /webrobot/api/datasets/{datasetId} | 
[**delete_dataset_version**](DefaultApi.md#delete_dataset_version) | **DELETE** /webrobot/api/datasets-legacy/version/id/{versionsetId} | 
[**delete_installation**](DefaultApi.md#delete_installation) | **DELETE** /webrobot/api/admin/plugin-installations/{id} | 
[**delete_profile**](DefaultApi.md#delete_profile) | **DELETE** /webrobot/api/agentic/profiles/{id} | 
[**delete_project**](DefaultApi.md#delete_project) | **DELETE** /webrobot/api/projects/id/{projectId} | 
[**delete_python_extension**](DefaultApi.md#delete_python_extension) | **DELETE** /webrobot/api/python-extensions/python-extensions/{extensionId} | 
[**delete_task**](DefaultApi.md#delete_task) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
[**delete_user_invite**](DefaultApi.md#delete_user_invite) | **DELETE** /webrobot/api/auth/user-invites/{id} | 
[**delete_version**](DefaultApi.md#delete_version) | **DELETE** /webrobot/api/admin/etl-library-versions/id/{id} | 
[**deprecate_bundle**](DefaultApi.md#deprecate_bundle) | **POST** /webrobot/api/admin/bundles/{id}/deprecate | 
[**disable_plugin**](DefaultApi.md#disable_plugin) | **POST** /webrobot/api/admin/plugins/{pluginId}/disable | 
[**disable_plugin1**](DefaultApi.md#disable_plugin1) | **POST** /webrobot/api/admin/plugin-installations/{id}/disable | 
[**disable_plugin_for_organization**](DefaultApi.md#disable_plugin_for_organization) | **POST** /webrobot/api/admin/plugin-installations/{pluginInstallationId}/organizations/{organizationId}/disable | 
[**download_bundle**](DefaultApi.md#download_bundle) | **GET** /webrobot/api/admin/bundles/{id}/download | 
[**download_cli_plugin**](DefaultApi.md#download_cli_plugin) | **GET** /webrobot/api/admin/bundles/cli-plugins/{pluginId} | 
[**download_model**](DefaultApi.md#download_model) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/download | 
[**download_ui_zip**](DefaultApi.md#download_ui_zip) | **GET** /webrobot/api/admin/plugin-installations/{pluginId}/ui/download | 
[**enable_by_plugin_id_for_organization**](DefaultApi.md#enable_by_plugin_id_for_organization) | **POST** /webrobot/api/admin/plugin-installations/by-plugin-id/{pluginId}/organizations/{organizationId}/enable | 
[**enable_plugin**](DefaultApi.md#enable_plugin) | **POST** /webrobot/api/admin/plugins/{pluginId}/enable | 
[**enable_plugin1**](DefaultApi.md#enable_plugin1) | **POST** /webrobot/api/admin/plugin-installations/{id}/enable | 
[**enable_plugin_for_organization**](DefaultApi.md#enable_plugin_for_organization) | **POST** /webrobot/api/admin/plugin-installations/{pluginInstallationId}/organizations/{organizationId}/enable | 
[**estimate_cost**](DefaultApi.md#estimate_cost) | **POST** /webrobot/api/ai-providers/providers/{provider}/cost-estimate | 
[**execute_demo**](DefaultApi.md#execute_demo) | **POST** /webrobot/api/demo/execute/{pipeline-name} | 
[**execute_job**](DefaultApi.md#execute_job) | **POST** /webrobot/api/ean-image-sourcing/{country}/execute | 
[**execute_job1**](DefaultApi.md#execute_job1) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/execute | 
[**execute_query**](DefaultApi.md#execute_query) | **POST** /webrobot/api/datasets/query | 
[**extract_direct**](DefaultApi.md#extract_direct) | **POST** /webrobot/api/extract/direct | 
[**find_all**](DefaultApi.md#find_all) | **GET** /api/strapi-tables/{table} | 
[**generate_pipeline**](DefaultApi.md#generate_pipeline) | **POST** /webrobot/api/demo/generate-pipeline | 
[**generate_pyspark_code**](DefaultApi.md#generate_pyspark_code) | **POST** /webrobot/api/python-extensions/python-extensions/{extensionId}/generate-pyspark | 
[**get_agent**](DefaultApi.md#get_agent) | **GET** /webrobot/api/agents/{categoryId}/{agentId} | 
[**get_agent_extensions**](DefaultApi.md#get_agent_extensions) | **GET** /webrobot/api/python-extensions/agents/{agentId}/extensions | 
[**get_agent_from_name**](DefaultApi.md#get_agent_from_name) | **GET** /webrobot/api/agents/{categoryId}/name/{agentName} | 
[**get_agent_python_extensions**](DefaultApi.md#get_agent_python_extensions) | **GET** /webrobot/api/python-extensions/agents/{agentId}/python-extensions | 
[**get_all_agents**](DefaultApi.md#get_all_agents) | **GET** /webrobot/api/agents/{categoryId} | 
[**get_all_categories**](DefaultApi.md#get_all_categories) | **GET** /webrobot/api/categories | 
[**get_all_cloud_credentials**](DefaultApi.md#get_all_cloud_credentials) | **GET** /webrobot/api/cloud-credentials | 
[**get_all_dataset_versions**](DefaultApi.md#get_all_dataset_versions) | **GET** /webrobot/api/datasets-legacy/{projectId}/{botId}/versions | 
[**get_all_datasets**](DefaultApi.md#get_all_datasets) | **GET** /webrobot/api/datasets-legacy/datasets | 
[**get_all_datasets1**](DefaultApi.md#get_all_datasets1) | **GET** /webrobot/api/datasets | 
[**get_all_installations**](DefaultApi.md#get_all_installations) | **GET** /webrobot/api/admin/plugin-installations | 
[**get_all_projects**](DefaultApi.md#get_all_projects) | **GET** /webrobot/api/projects | 
[**get_all_tasks**](DefaultApi.md#get_all_tasks) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks | 
[**get_all_versions**](DefaultApi.md#get_all_versions) | **GET** /webrobot/api/admin/etl-library-versions | 
[**get_all_versionsets**](DefaultApi.md#get_all_versionsets) | **GET** /webrobot/api/datasets-legacy/{datasetId}/versions | 
[**get_billing_plans**](DefaultApi.md#get_billing_plans) | **GET** /webrobot/api/billing/plans | 
[**get_bootstrap_status**](DefaultApi.md#get_bootstrap_status) | **GET** /webrobot/api/ean-image-sourcing/bootstrap/status | 
[**get_bundle_scan**](DefaultApi.md#get_bundle_scan) | **GET** /webrobot/api/admin/bundles/{id}/scan | 
[**get_by_id**](DefaultApi.md#get_by_id) | **GET** /api/strapi-tables/{table}/{id} | 
[**get_capabilities**](DefaultApi.md#get_capabilities) | **GET** /webrobot/cloud/spark/capabilities | 
[**get_catalog_stages**](DefaultApi.md#get_catalog_stages) | **GET** /webrobot/api/demo/catalog/stages | 
[**get_category**](DefaultApi.md#get_category) | **GET** /webrobot/api/categories/id/{categoryId} | 
[**get_category_from_name**](DefaultApi.md#get_category_from_name) | **GET** /webrobot/api/categories/{categoryName} | 
[**get_cloud_credential_by_id**](DefaultApi.md#get_cloud_credential_by_id) | **GET** /webrobot/api/cloud-credentials/id/{credentialId} | 
[**get_cloud_credentials_by_provider**](DefaultApi.md#get_cloud_credentials_by_provider) | **GET** /webrobot/api/cloud-credentials/provider/{provider} | 
[**get_cron_job**](DefaultApi.md#get_cron_job) | **GET** /webrobot/cloud/scheduler/cronjobs/{name} | 
[**get_current_user**](DefaultApi.md#get_current_user) | **GET** /webrobot/api/auth/me | 
[**get_dataset**](DefaultApi.md#get_dataset) | **GET** /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId} | 
[**get_dataset1**](DefaultApi.md#get_dataset1) | **GET** /webrobot/api/datasets/{datasetId} | 
[**get_dataset_fields**](DefaultApi.md#get_dataset_fields) | **GET** /webrobot/api/datasets/{datasetId}/fields | 
[**get_dataset_info_by_task**](DefaultApi.md#get_dataset_info_by_task) | **GET** /webrobot/api/datasets/query/task/{taskId}/info | 
[**get_dataset_input_file**](DefaultApi.md#get_dataset_input_file) | **GET** /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId}/input/url | 
[**get_dataset_input_file_pagination**](DefaultApi.md#get_dataset_input_file_pagination) | **GET** /webrobot/api/datasets-legacy/{projectId}/{botId}/{datasetId}/input/{offset}/{limit} | 
[**get_dataset_input_file_size**](DefaultApi.md#get_dataset_input_file_size) | **GET** /webrobot/api/datasets-legacy/{datasetId}/input/size | 
[**get_dataset_status**](DefaultApi.md#get_dataset_status) | **GET** /webrobot/api/datasets-legacy/datasets/{datasetId}/status | 
[**get_dataset_version_input_file**](DefaultApi.md#get_dataset_version_input_file) | **GET** /webrobot/api/datasets-legacy/{categoryId}/{jobId}/{datasetId}/versions/{versionsetId}/input/url | 
[**get_dataset_version_input_file_pagination**](DefaultApi.md#get_dataset_version_input_file_pagination) | **GET** /webrobot/api/datasets-legacy/{datasetId}/versions/{versionsetId}/input/{offset}/{limit} | 
[**get_effective_entitlements**](DefaultApi.md#get_effective_entitlements) | **GET** /webrobot/api/etl/entitlements | 
[**get_execution_logs**](DefaultApi.md#get_execution_logs) | **GET** /webrobot/api/demo/executions/{executionId}/logs | 
[**get_execution_logs1**](DefaultApi.md#get_execution_logs1) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/executions/{executionId}/logs | 
[**get_execution_output**](DefaultApi.md#get_execution_output) | **GET** /webrobot/api/demo/executions/{executionId}/output | 
[**get_execution_status**](DefaultApi.md#get_execution_status) | **GET** /webrobot/api/demo/executions/{executionId}/status | 
[**get_execution_status1**](DefaultApi.md#get_execution_status1) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/executions/{executionId}/status | 
[**get_health**](DefaultApi.md#get_health) | **GET** /health | 
[**get_html**](DefaultApi.md#get_html) | **GET** /webrobot/api/html/{url}/{protocol} | 
[**get_images_simplified**](DefaultApi.md#get_images_simplified) | **POST** /webrobot/api/ean-image-sourcing/{country}/images | 
[**get_info**](DefaultApi.md#get_info) | **GET** /webrobot/cloud/spark/info | 
[**get_info1**](DefaultApi.md#get_info1) | **GET** /webrobot/cloud/training/info | 
[**get_installation_by_id**](DefaultApi.md#get_installation_by_id) | **GET** /webrobot/api/admin/plugin-installations/{id} | 
[**get_job**](DefaultApi.md#get_job) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId} | 
[**get_job_logs**](DefaultApi.md#get_job_logs) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/logs | 
[**get_job_metrics**](DefaultApi.md#get_job_metrics) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/metrics | 
[**get_organization**](DefaultApi.md#get_organization) | **GET** /webrobot/api/auth/organizations/{id} | 
[**get_organization_plugins**](DefaultApi.md#get_organization_plugins) | **GET** /webrobot/api/admin/plugin-installations/../organizations/{organizationId}/plugin-installations | 
[**get_organization_users**](DefaultApi.md#get_organization_users) | **GET** /webrobot/api/auth/organizations/{id}/users | 
[**get_partners_by_type**](DefaultApi.md#get_partners_by_type) | **GET** /webrobot/api/auth/partners/{type} | 
[**get_plugin_info**](DefaultApi.md#get_plugin_info) | **GET** /webrobot/api/demo/info | 
[**get_plugin_info1**](DefaultApi.md#get_plugin_info1) | **GET** /webrobot/api/ean-image-sourcing/info | 
[**get_plugin_info2**](DefaultApi.md#get_plugin_info2) | **GET** /webrobot/api/python-extensions/info | 
[**get_plugin_organizations**](DefaultApi.md#get_plugin_organizations) | **GET** /webrobot/api/admin/plugin-installations/{pluginInstallationId}/organizations | 
[**get_plugin_usage**](DefaultApi.md#get_plugin_usage) | **GET** /webrobot/api/admin/plugins/{pluginId}/usage | 
[**get_profile**](DefaultApi.md#get_profile) | **GET** /webrobot/api/agentic/profiles/{id} | 
[**get_project**](DefaultApi.md#get_project) | **GET** /webrobot/api/projects/id/{projectId} | 
[**get_project_from_name**](DefaultApi.md#get_project_from_name) | **GET** /webrobot/api/projects/{projectName} | 
[**get_project_jobs**](DefaultApi.md#get_project_jobs) | **GET** /webrobot/api/projects/id/{projectId}/jobs | 
[**get_project_metrics**](DefaultApi.md#get_project_metrics) | **GET** /webrobot/api/projects/id/{projectId}/metrics | 
[**get_project_schedule**](DefaultApi.md#get_project_schedule) | **GET** /webrobot/api/projects/id/{projectId}/schedule | 
[**get_stage**](DefaultApi.md#get_stage) | **GET** /webrobot/api/manifest/stages/{name} | 
[**get_status**](DefaultApi.md#get_status) | **GET** /webrobot/api/ean-image-sourcing/{country}/status | 
[**get_supported_extension_types**](DefaultApi.md#get_supported_extension_types) | **GET** /webrobot/api/python-extensions/supported-types | 
[**get_supported_models**](DefaultApi.md#get_supported_models) | **GET** /webrobot/api/ai-providers/providers/{provider}/models | 
[**get_supported_providers**](DefaultApi.md#get_supported_providers) | **GET** /webrobot/api/ai-providers/providers | 
[**get_system_logs**](DefaultApi.md#get_system_logs) | **GET** /webrobot/api/projects/admin/system-logs | 
[**get_table_columns**](DefaultApi.md#get_table_columns) | **GET** /webrobot/api/datasets/query/columns | 
[**get_task**](DefaultApi.md#get_task) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
[**get_task_by_output_dataset**](DefaultApi.md#get_task_by_output_dataset) | **GET** /webrobot/api/datasets/query/by-dataset/{datasetId}/task | 
[**get_task_metrics**](DefaultApi.md#get_task_metrics) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/metrics | 
[**get_task_status**](DefaultApi.md#get_task_status) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/status | 
[**get_training_logs**](DefaultApi.md#get_training_logs) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/logs | 
[**get_training_status**](DefaultApi.md#get_training_status) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/status | 
[**get_ui_definitions**](DefaultApi.md#get_ui_definitions) | **GET** /webrobot/api/admin/plugin-installations/ui-definitions | 
[**get_upload_file_url**](DefaultApi.md#get_upload_file_url) | **GET** /webrobot/api/datasets-legacy/{categoryId}/{jobId}/upload/{attachmentName} | 
[**get_url_download**](DefaultApi.md#get_url_download) | **GET** /webrobot/api/package/download | 
[**get_url_upload**](DefaultApi.md#get_url_upload) | **GET** /webrobot/api/package/upload | 
[**get_user_invites**](DefaultApi.md#get_user_invites) | **GET** /webrobot/api/auth/user-invites | 
[**get_version_by_build_type_and_build_number**](DefaultApi.md#get_version_by_build_type_and_build_number) | **GET** /webrobot/api/admin/etl-library-versions/build-type/{buildType}/build-number/{buildNumber} | 
[**get_version_by_id**](DefaultApi.md#get_version_by_id) | **GET** /webrobot/api/admin/etl-library-versions/id/{id} | 
[**get_versionset**](DefaultApi.md#get_versionset) | **GET** /webrobot/api/datasets-legacy/version/id/{versionsetId} | 
[**get_versionset_from_version**](DefaultApi.md#get_versionset_from_version) | **POST** /webrobot/api/datasets-legacy/{datasetId}/versions/version/{version} | 
[**get_versionset_from_version_base**](DefaultApi.md#get_versionset_from_version_base) | **GET** /webrobot/api/datasets-legacy/{datasetId}/versions/version/{version}/base | 
[**health_check**](DefaultApi.md#health_check) | **GET** /webrobot/cloud/spark/health | 
[**health_check1**](DefaultApi.md#health_check1) | **GET** /webrobot/cloud/training/health | 
[**index_dataset**](DefaultApi.md#index_dataset) | **POST** /webrobot/api/datasets/{datasetId}/index | 
[**infer**](DefaultApi.md#infer) | **POST** /webrobot/api/llm/infer | 
[**insert**](DefaultApi.md#insert) | **POST** /api/strapi-tables/{table} | 
[**install_bundle**](DefaultApi.md#install_bundle) | **POST** /webrobot/api/admin/bundles/install | 
[**job_completion_webhook**](DefaultApi.md#job_completion_webhook) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/completion | 
[**list_adapters**](DefaultApi.md#list_adapters) | **GET** /webrobot/api/admin/cloud-adapters | 
[**list_api_keys**](DefaultApi.md#list_api_keys) | **GET** /webrobot/api/auth/api-keys | 
[**list_available**](DefaultApi.md#list_available) | **GET** /webrobot/api/admin/cloud-adapters/available | 
[**list_bundles**](DefaultApi.md#list_bundles) | **GET** /webrobot/api/admin/bundles | 
[**list_charges**](DefaultApi.md#list_charges) | **GET** /webrobot/api/admin/marketplace-billing/charges | 
[**list_cli_plugins**](DefaultApi.md#list_cli_plugins) | **GET** /webrobot/api/admin/bundles/cli-plugins-list | 
[**list_cron_jobs**](DefaultApi.md#list_cron_jobs) | **GET** /webrobot/cloud/scheduler/cronjobs | 
[**list_demos**](DefaultApi.md#list_demos) | **GET** /webrobot/api/demo/list | 
[**list_executions**](DefaultApi.md#list_executions) | **GET** /webrobot/api/agentic/executions | 
[**list_my_adapters**](DefaultApi.md#list_my_adapters) | **GET** /webrobot/api/admin/cloud-adapters/mine | 
[**list_payouts**](DefaultApi.md#list_payouts) | **GET** /webrobot/api/admin/marketplace-billing/payouts | 
[**list_plugins**](DefaultApi.md#list_plugins) | **GET** /webrobot/api/admin/plugins | 
[**list_profiles**](DefaultApi.md#list_profiles) | **GET** /webrobot/api/agentic/profiles | 
[**list_providers**](DefaultApi.md#list_providers) | **GET** /webrobot/api/llm/providers | 
[**list_revenue_share**](DefaultApi.md#list_revenue_share) | **GET** /webrobot/api/admin/agency-billing/revenue-share | 
[**list_stages**](DefaultApi.md#list_stages) | **GET** /webrobot/api/catalog/stages | 
[**list_stages1**](DefaultApi.md#list_stages1) | **GET** /webrobot/api/manifest/stages | 
[**list_tables**](DefaultApi.md#list_tables) | **GET** /webrobot/api/datasets/query/tables | 
[**mark_failed**](DefaultApi.md#mark_failed) | **POST** /webrobot/api/admin/marketplace-billing/charges/by-invoice/{invoiceId}/mark-failed | 
[**mark_paid**](DefaultApi.md#mark_paid) | **POST** /webrobot/api/admin/marketplace-billing/charges/by-invoice/{invoiceId}/mark-paid | 
[**mark_zombie_tasks**](DefaultApi.md#mark_zombie_tasks) | **POST** /webrobot/api/projects/admin/tasks/mark-zombies | 
[**probe_adapter**](DefaultApi.md#probe_adapter) | **POST** /webrobot/api/admin/cloud-adapters/{providerKey}/probe | 
[**process_yaml_extensions**](DefaultApi.md#process_yaml_extensions) | **POST** /webrobot/api/python-extensions/process-yaml | 
[**publish_model**](DefaultApi.md#publish_model) | **POST** /webrobot/api/ai-providers/providers/huggingface/models/publish | 
[**query_dataset_by_task**](DefaultApi.md#query_dataset_by_task) | **POST** /webrobot/api/datasets/query/task/{taskId} | 
[**query_images**](DefaultApi.md#query_images) | **POST** /webrobot/api/ean-image-sourcing/{country}/query | 
[**refresh_organizations_billing_status**](DefaultApi.md#refresh_organizations_billing_status) | **POST** /webrobot/api/auth/organizations/billing/refresh | 
[**refund**](DefaultApi.md#refund) | **POST** /webrobot/api/admin/marketplace-billing/charges/{id}/refund | 
[**register_plugin**](DefaultApi.md#register_plugin) | **POST** /webrobot/api/admin/plugin-installations | 
[**register_python_extension**](DefaultApi.md#register_python_extension) | **POST** /webrobot/api/python-extensions/python-extensions/register | 
[**reject_bundle**](DefaultApi.md#reject_bundle) | **POST** /webrobot/api/admin/bundles/{id}/reject | 
[**reload_pipelines**](DefaultApi.md#reload_pipelines) | **POST** /webrobot/api/demo/reload-pipelines | 
[**reload_plugins**](DefaultApi.md#reload_plugins) | **POST** /webrobot/api/admin/plugin-installations/reload | 
[**remove_job_from_project**](DefaultApi.md#remove_job_from_project) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId} | 
[**report_health**](DefaultApi.md#report_health) | **POST** /webrobot/api/admin/cloud-adapters/{providerKey}/health | 
[**reschedule_events**](DefaultApi.md#reschedule_events) | **POST** /webrobot/api/streaming/reschedule-events | 
[**rollup**](DefaultApi.md#rollup) | **POST** /webrobot/api/admin/stage-usage/rollup | 
[**run_charges**](DefaultApi.md#run_charges) | **POST** /webrobot/api/admin/marketplace-billing/run-charges | 
[**run_health_check**](DefaultApi.md#run_health_check) | **POST** /webrobot/api/admin/cloud-adapters/run-health-check | 
[**run_orchestration_charges**](DefaultApi.md#run_orchestration_charges) | **POST** /webrobot/api/admin/marketplace-billing/run-orchestration-charges | 
[**run_payouts**](DefaultApi.md#run_payouts) | **POST** /webrobot/api/admin/marketplace-billing/run-payouts | 
[**run_provider_endpoint_charges**](DefaultApi.md#run_provider_endpoint_charges) | **POST** /webrobot/api/admin/marketplace-billing/run-provider-endpoint-charges | 
[**run_revenue_share**](DefaultApi.md#run_revenue_share) | **POST** /webrobot/api/admin/agency-billing/run-revenue-share | 
[**save_generated_pipeline**](DefaultApi.md#save_generated_pipeline) | **POST** /webrobot/api/demo/save-generated-pipeline | 
[**schedule_job**](DefaultApi.md#schedule_job) | **POST** /webrobot/api/ean-image-sourcing/{country}/schedule | 
[**serve_demo_app**](DefaultApi.md#serve_demo_app) | **GET** /webrobot/api/demo/app | 
[**serve_static_file**](DefaultApi.md#serve_static_file) | **GET** /webrobot/api/demo/app/{filename} | 
[**set_project_schedule**](DefaultApi.md#set_project_schedule) | **PUT** /webrobot/api/projects/id/{projectId}/schedule | 
[**start**](DefaultApi.md#start) | **POST** /webrobot/api/agentic/start | 
[**start_export_all**](DefaultApi.md#start_export_all) | **GET** /webrobot/api/package/export/all | 
[**start_export_organization**](DefaultApi.md#start_export_organization) | **GET** /webrobot/api/package/export/organization/{organizationId} | 
[**start_export_organization_with_options**](DefaultApi.md#start_export_organization_with_options) | **POST** /webrobot/api/package/export/organization/{organizationId} | 
[**start_export_project**](DefaultApi.md#start_export_project) | **GET** /webrobot/api/package/export/id/{projectId} | 
[**start_import_all**](DefaultApi.md#start_import_all) | **GET** /webrobot/api/package/import/all | 
[**start_import_all_with_options**](DefaultApi.md#start_import_all_with_options) | **POST** /webrobot/api/package/import/all | 
[**start_import_organization**](DefaultApi.md#start_import_organization) | **GET** /webrobot/api/package/import/organization/{organizationId} | 
[**start_import_organization_with_options**](DefaultApi.md#start_import_organization_with_options) | **POST** /webrobot/api/package/import/organization/{organizationId} | 
[**start_import_project**](DefaultApi.md#start_import_project) | **GET** /webrobot/api/package/import/id/{projectId} | 
[**start_import_project_with_options**](DefaultApi.md#start_import_project_with_options) | **POST** /webrobot/api/package/import/id/{projectId} | 
[**start_task**](DefaultApi.md#start_task) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/start | 
[**start_training**](DefaultApi.md#start_training) | **POST** /webrobot/api/ai-providers/providers/{provider}/training | 
[**status**](DefaultApi.md#status) | **GET** /webrobot/api/agentic/{eid} | 
[**stop_job**](DefaultApi.md#stop_job) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/stop | 
[**stop_task**](DefaultApi.md#stop_task) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/stop | 
[**suggest_stages**](DefaultApi.md#suggest_stages) | **POST** /webrobot/api/demo/wizard/suggest | 
[**test**](DefaultApi.md#test) | **GET** /webrobot/api/categories/test | 
[**test1**](DefaultApi.md#test1) | **GET** /webrobot/api/projects/test | 
[**test_cloud_credential**](DefaultApi.md#test_cloud_credential) | **POST** /webrobot/api/cloud-credentials/test | 
[**update**](DefaultApi.md#update) | **PUT** /api/strapi-tables/{table}/{id} | 
[**update_adapter**](DefaultApi.md#update_adapter) | **PUT** /webrobot/api/admin/cloud-adapters/{providerKey} | 
[**update_agent**](DefaultApi.md#update_agent) | **PUT** /webrobot/api/agents/{categoryId}/{agentId} | 
[**update_agent_python_extensions**](DefaultApi.md#update_agent_python_extensions) | **POST** /webrobot/api/python-extensions/agents/{agentId}/python-extensions | 
[**update_billing_plan**](DefaultApi.md#update_billing_plan) | **PUT** /webrobot/api/billing/plans/{id} | 
[**update_category**](DefaultApi.md#update_category) | **PUT** /webrobot/api/categories/id/{categoryId} | 
[**update_cloud_credential**](DefaultApi.md#update_cloud_credential) | **PUT** /webrobot/api/cloud-credentials/id/{credentialId} | 
[**update_dataset**](DefaultApi.md#update_dataset) | **PUT** /webrobot/api/datasets/{datasetId} | 
[**update_installation**](DefaultApi.md#update_installation) | **PUT** /webrobot/api/admin/plugin-installations/{id} | 
[**update_job**](DefaultApi.md#update_job) | **PUT** /webrobot/api/projects/id/{projectId}/jobs/{jobId} | 
[**update_organization**](DefaultApi.md#update_organization) | **PUT** /webrobot/api/auth/organizations/{id} | 
[**update_profile**](DefaultApi.md#update_profile) | **PUT** /webrobot/api/agentic/profiles/{id} | 
[**update_project**](DefaultApi.md#update_project) | **PUT** /webrobot/api/projects/id/{projectId} | 
[**update_python_extension**](DefaultApi.md#update_python_extension) | **PUT** /webrobot/api/python-extensions/python-extensions/{extensionId} | 
[**update_task**](DefaultApi.md#update_task) | **PUT** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
[**update_version**](DefaultApi.md#update_version) | **PUT** /webrobot/api/admin/etl-library-versions/id/{id} | 
[**upload_csv**](DefaultApi.md#upload_csv) | **POST** /webrobot/api/ean-image-sourcing/{country}/upload | 
[**upload_dataset**](DefaultApi.md#upload_dataset) | **POST** /webrobot/api/demo/upload-dataset/{pipeline-name} | 
[**upload_dataset1**](DefaultApi.md#upload_dataset1) | **POST** /webrobot/api/ai-providers/providers/{provider}/datasets | 
[**upload_dataset2**](DefaultApi.md#upload_dataset2) | **POST** /webrobot/api/datasets-legacy/{projectId}/{botId} | 
[**upload_dataset_file**](DefaultApi.md#upload_dataset_file) | **POST** /webrobot/api/datasets/upload | 
[**upload_file**](DefaultApi.md#upload_file) | **POST** /webrobot/api/package/upload | 
[**upload_plugin**](DefaultApi.md#upload_plugin) | **POST** /webrobot/api/admin/plugins/upload | 
[**validate**](DefaultApi.md#validate) | **POST** /webrobot/api/manifest/validate | 
[**validate_python_extension**](DefaultApi.md#validate_python_extension) | **POST** /webrobot/api/python-extensions/validate | 
[**wizard_infer_actions**](DefaultApi.md#wizard_infer_actions) | **POST** /webrobot/api/demo/wizard/infer-actions | 
[**wizard_infer_fields**](DefaultApi.md#wizard_infer_fields) | **POST** /webrobot/api/demo/wizard/infer-fields | 
[**wizard_infer_segment**](DefaultApi.md#wizard_infer_segment) | **POST** /webrobot/api/demo/wizard/infer-segment | 
[**wizard_infer_selector**](DefaultApi.md#wizard_infer_selector) | **POST** /webrobot/api/demo/wizard/infer-selector | 
[**wizard_proxy**](DefaultApi.md#wizard_proxy) | **GET** /webrobot/api/demo/wizard/proxy | 
[**wizard_suggest_field_names**](DefaultApi.md#wizard_suggest_field_names) | **POST** /webrobot/api/demo/wizard/suggest-field-names | 
[**wizard_validate**](DefaultApi.md#wizard_validate) | **POST** /webrobot/api/demo/wizard/validate | 


# **add_job_to_project**
> add_job_to_project(project_id, job_dto=job_dto)

### Example


```python
import webrobot
from webrobot.models.job_dto import JobDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_dto = webrobot.JobDto() # JobDto |  (optional)

    try:
        api_instance.add_job_to_project(project_id, job_dto=job_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->add_job_to_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_dto** | [**JobDto**](JobDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply**
> apply(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.apply(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->apply: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_migrations**
> apply_migrations(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.apply_migrations(id)
    except Exception as e:
        print("Exception when calling DefaultApi->apply_migrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_bundle**
> approve_bundle(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.approve_bundle(id)
    except Exception as e:
        print("Exception when calling DefaultApi->approve_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_user_to_organization**
> assign_user_to_organization(id, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 'id_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.assign_user_to_organization(id, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->assign_user_to_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bootstrap_for_organization**
> bootstrap_for_organization(organization_id, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    organization_id = 'organization_id_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.bootstrap_for_organization(organization_id, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->bootstrap_for_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel**
> cancel(eid)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    eid = 'eid_example' # str | 

    try:
        api_instance.cancel(eid)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_execution**
> cancel_execution(execution_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    execution_id = 'execution_id_example' # str | 

    try:
        api_instance.cancel_execution(execution_id)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_execution1**
> cancel_execution1(project_id, job_id, execution_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    execution_id = 'execution_id_example' # str | 

    try:
        api_instance.cancel_execution1(project_id, job_id, execution_id)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_execution1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **execution_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_training**
> cancel_training(provider, job_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider = 'provider_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        api_instance.cancel_training(provider, job_id)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_training: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cmf_close**
> cmf_close(session_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        api_instance.cmf_close(session_id)
    except Exception as e:
        print("Exception when calling DefaultApi->cmf_close: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cmf_open**
> cmf_open(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.cmf_open(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->cmf_open: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cmf_step**
> cmf_step(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.cmf_step(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->cmf_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **completion**
> completion(eid, completion_request=completion_request)

### Example


```python
import webrobot
from webrobot.models.completion_request import CompletionRequest
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    eid = 'eid_example' # str | 
    completion_request = webrobot.CompletionRequest() # CompletionRequest |  (optional)

    try:
        api_instance.completion(eid, completion_request=completion_request)
    except Exception as e:
        print("Exception when calling DefaultApi->completion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eid** | **str**|  | 
 **completion_request** | [**CompletionRequest**](CompletionRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_agent**
> copy_agent(agent_id, copy_to_organizations_dto=copy_to_organizations_dto)

### Example


```python
import webrobot
from webrobot.models.copy_to_organizations_dto import CopyToOrganizationsDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 
    copy_to_organizations_dto = webrobot.CopyToOrganizationsDto() # CopyToOrganizationsDto |  (optional)

    try:
        api_instance.copy_agent(agent_id, copy_to_organizations_dto=copy_to_organizations_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->copy_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **copy_to_organizations_dto** | [**CopyToOrganizationsDto**](CopyToOrganizationsDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent**
> create_agent(agent_dto=agent_dto)

### Example


```python
import webrobot
from webrobot.models.agent_dto import AgentDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    agent_dto = webrobot.AgentDto() # AgentDto |  (optional)

    try:
        api_instance.create_agent(agent_dto=agent_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->create_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_dto** | [**AgentDto**](AgentDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key**
> create_api_key(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.create_api_key(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_billing_plan**
> create_billing_plan(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.create_billing_plan(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->create_billing_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_category**
> create_category(job_category_dto=job_category_dto)

### Example


```python
import webrobot
from webrobot.models.job_category_dto import JobCategoryDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    job_category_dto = webrobot.JobCategoryDto() # JobCategoryDto |  (optional)

    try:
        api_instance.create_category(job_category_dto=job_category_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->create_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_category_dto** | [**JobCategoryDto**](JobCategoryDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_credential**
> create_cloud_credential(cloud_credential=cloud_credential)

### Example


```python
import webrobot
from webrobot.models.cloud_credential import CloudCredential
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    cloud_credential = webrobot.CloudCredential() # CloudCredential |  (optional)

    try:
        api_instance.create_cloud_credential(cloud_credential=cloud_credential)
    except Exception as e:
        print("Exception when calling DefaultApi->create_cloud_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_credential** | [**CloudCredential**](CloudCredential.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cron_job**
> create_cron_job(cron_job_request=cron_job_request)

### Example


```python
import webrobot
from webrobot.models.cron_job_request import CronJobRequest
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    cron_job_request = webrobot.CronJobRequest() # CronJobRequest |  (optional)

    try:
        api_instance.create_cron_job(cron_job_request=cron_job_request)
    except Exception as e:
        print("Exception when calling DefaultApi->create_cron_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cron_job_request** | [**CronJobRequest**](CronJobRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_plan**
> create_custom_plan(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.create_custom_plan(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->create_custom_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dataset**
> create_dataset(dataset_dto=dataset_dto)

### Example


```python
import webrobot
from webrobot.models.dataset_dto import DatasetDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_dto = webrobot.DatasetDto() # DatasetDto |  (optional)

    try:
        api_instance.create_dataset(dataset_dto=dataset_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->create_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_dto** | [**DatasetDto**](DatasetDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_version**
> create_or_update_version(etl_library_version_api_dto=etl_library_version_api_dto)

### Example


```python
import webrobot
from webrobot.models.etl_library_version_api_dto import EtlLibraryVersionApiDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    etl_library_version_api_dto = webrobot.EtlLibraryVersionApiDto() # EtlLibraryVersionApiDto |  (optional)

    try:
        api_instance.create_or_update_version(etl_library_version_api_dto=etl_library_version_api_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->create_or_update_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **etl_library_version_api_dto** | [**EtlLibraryVersionApiDto**](EtlLibraryVersionApiDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization**
> create_organization(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.create_organization(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_profile**
> create_profile(agentic_profile=agentic_profile)

### Example


```python
import webrobot
from webrobot.models.agentic_profile import AgenticProfile
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    agentic_profile = webrobot.AgenticProfile() # AgenticProfile |  (optional)

    try:
        api_instance.create_profile(agentic_profile=agentic_profile)
    except Exception as e:
        print("Exception when calling DefaultApi->create_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentic_profile** | [**AgenticProfile**](AgenticProfile.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> create_project(job_project_dto=job_project_dto)

### Example


```python
import webrobot
from webrobot.models.job_project_dto import JobProjectDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    job_project_dto = webrobot.JobProjectDto() # JobProjectDto |  (optional)

    try:
        api_instance.create_project(job_project_dto=job_project_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_project_dto** | [**JobProjectDto**](JobProjectDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task**
> create_task(project_id, job_id, task_dto=task_dto)

### Example


```python
import webrobot
from webrobot.models.task_dto import TaskDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    task_dto = webrobot.TaskDto() # TaskDto |  (optional)

    try:
        api_instance.create_task(project_id, job_id, task_dto=task_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->create_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_dto** | [**TaskDto**](TaskDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decrypt_field**
> decrypt_field(credential_id, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    credential_id = 'credential_id_example' # str | 
    request_body = {'key': 'request_body_example'} # Dict[str, str] |  (optional)

    try:
        api_instance.decrypt_field(credential_id, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->decrypt_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 
 **request_body** | [**Dict[str, str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(table, id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    table = 'table_example' # str | 
    id = 'id_example' # str | 

    try:
        api_instance.delete(table, id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent**
> delete_agent(agent_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        api_instance.delete_agent(agent_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> delete_api_key(key_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    key_id = 'key_id_example' # str | 

    try:
        api_instance.delete_api_key(key_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_plan**
> delete_billing_plan(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_billing_plan(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_billing_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**
> delete_category(category_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    category_id = 'category_id_example' # str | 

    try:
        api_instance.delete_category(category_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_credential**
> delete_cloud_credential(credential_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    credential_id = 'credential_id_example' # str | 

    try:
        api_instance.delete_cloud_credential(credential_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_cloud_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cron_job**
> delete_cron_job(name, namespace=namespace)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    name = 'name_example' # str | 
    namespace = 'namespace_example' # str |  (optional)

    try:
        api_instance.delete_cron_job(name, namespace=namespace)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_cron_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset**
> delete_dataset(dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.delete_dataset(dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset1**
> delete_dataset1(dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.delete_dataset1(dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_dataset1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset_version**
> delete_dataset_version(versionset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    versionset_id = 'versionset_id_example' # str | 

    try:
        api_instance.delete_dataset_version(versionset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_dataset_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_installation**
> delete_installation(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_installation(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_installation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_profile**
> delete_profile(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_profile(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_instance.delete_project(project_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_python_extension**
> delete_python_extension(extension_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    extension_id = 'extension_id_example' # str | 

    try:
        api_instance.delete_python_extension(extension_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_python_extension: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> delete_task(project_id, job_id, task_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    task_id = 'task_id_example' # str | 

    try:
        api_instance.delete_task(project_id, job_id, task_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_invite**
> delete_user_invite(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_user_invite(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_user_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version**
> delete_version(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_version(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deprecate_bundle**
> deprecate_bundle(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.deprecate_bundle(id)
    except Exception as e:
        print("Exception when calling DefaultApi->deprecate_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_plugin**
> disable_plugin(plugin_id, build_type=build_type)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    plugin_id = 'plugin_id_example' # str | 
    build_type = 'development' # str |  (optional) (default to 'development')

    try:
        api_instance.disable_plugin(plugin_id, build_type=build_type)
    except Exception as e:
        print("Exception when calling DefaultApi->disable_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 
 **build_type** | **str**|  | [optional] [default to &#39;development&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_plugin1**
> disable_plugin1(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.disable_plugin1(id)
    except Exception as e:
        print("Exception when calling DefaultApi->disable_plugin1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_plugin_for_organization**
> disable_plugin_for_organization(plugin_installation_id, organization_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    plugin_installation_id = 56 # int | 
    organization_id = 'organization_id_example' # str | 

    try:
        api_instance.disable_plugin_for_organization(plugin_installation_id, organization_id)
    except Exception as e:
        print("Exception when calling DefaultApi->disable_plugin_for_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_installation_id** | **int**|  | 
 **organization_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_bundle**
> download_bundle(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.download_bundle(id)
    except Exception as e:
        print("Exception when calling DefaultApi->download_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_cli_plugin**
> download_cli_plugin(plugin_id, version=version)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    plugin_id = 'plugin_id_example' # str | 
    version = 'version_example' # str |  (optional)

    try:
        api_instance.download_cli_plugin(plugin_id, version=version)
    except Exception as e:
        print("Exception when calling DefaultApi->download_cli_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 
 **version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/java-archive

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_model**
> download_model(provider, job_id, output_path=output_path)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider = 'provider_example' # str | 
    job_id = 'job_id_example' # str | 
    output_path = 'output_path_example' # str |  (optional)

    try:
        api_instance.download_model(provider, job_id, output_path=output_path)
    except Exception as e:
        print("Exception when calling DefaultApi->download_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **job_id** | **str**|  | 
 **output_path** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_ui_zip**
> download_ui_zip(plugin_id, build_type=build_type)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    plugin_id = 'plugin_id_example' # str | 
    build_type = 'build_type_example' # str |  (optional)

    try:
        api_instance.download_ui_zip(plugin_id, build_type=build_type)
    except Exception as e:
        print("Exception when calling DefaultApi->download_ui_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 
 **build_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_by_plugin_id_for_organization**
> enable_by_plugin_id_for_organization(plugin_id, organization_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    plugin_id = 'plugin_id_example' # str | 
    organization_id = 'organization_id_example' # str | 

    try:
        api_instance.enable_by_plugin_id_for_organization(plugin_id, organization_id)
    except Exception as e:
        print("Exception when calling DefaultApi->enable_by_plugin_id_for_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 
 **organization_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_plugin**
> enable_plugin(plugin_id, build_type=build_type)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    plugin_id = 'plugin_id_example' # str | 
    build_type = 'development' # str |  (optional) (default to 'development')

    try:
        api_instance.enable_plugin(plugin_id, build_type=build_type)
    except Exception as e:
        print("Exception when calling DefaultApi->enable_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 
 **build_type** | **str**|  | [optional] [default to &#39;development&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_plugin1**
> enable_plugin1(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.enable_plugin1(id)
    except Exception as e:
        print("Exception when calling DefaultApi->enable_plugin1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_plugin_for_organization**
> enable_plugin_for_organization(plugin_installation_id, organization_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    plugin_installation_id = 56 # int | 
    organization_id = 'organization_id_example' # str | 

    try:
        api_instance.enable_plugin_for_organization(plugin_installation_id, organization_id)
    except Exception as e:
        print("Exception when calling DefaultApi->enable_plugin_for_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_installation_id** | **int**|  | 
 **organization_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_cost**
> estimate_cost(provider, training_request_bean=training_request_bean)

### Example


```python
import webrobot
from webrobot.models.training_request_bean import TrainingRequestBean
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider = 'provider_example' # str | 
    training_request_bean = webrobot.TrainingRequestBean() # TrainingRequestBean |  (optional)

    try:
        api_instance.estimate_cost(provider, training_request_bean=training_request_bean)
    except Exception as e:
        print("Exception when calling DefaultApi->estimate_cost: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **training_request_bean** | [**TrainingRequestBean**](TrainingRequestBean.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_demo**
> execute_demo(pipeline_name, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    pipeline_name = 'pipeline_name_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.execute_demo(pipeline_name, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->execute_demo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_name** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_job**
> execute_job(country, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    country = 'country_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.execute_job(country, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->execute_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_job1**
> execute_job1(project_id, job_id, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.execute_job1(project_id, job_id, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->execute_job1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_query**
> execute_query(presto_query_request=presto_query_request)

### Example


```python
import webrobot
from webrobot.models.presto_query_request import PrestoQueryRequest
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    presto_query_request = webrobot.PrestoQueryRequest() # PrestoQueryRequest |  (optional)

    try:
        api_instance.execute_query(presto_query_request=presto_query_request)
    except Exception as e:
        print("Exception when calling DefaultApi->execute_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **presto_query_request** | [**PrestoQueryRequest**](PrestoQueryRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_direct**
> extract_direct(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.extract_direct(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->extract_direct: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all**
> find_all(table, page=page, page_size=page_size)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    table = 'table_example' # str | 
    page = 0 # int |  (optional) (default to 0)
    page_size = 50 # int |  (optional) (default to 50)

    try:
        api_instance.find_all(table, page=page, page_size=page_size)
    except Exception as e:
        print("Exception when calling DefaultApi->find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_pipeline**
> generate_pipeline(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.generate_pipeline(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->generate_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_pyspark_code**
> generate_pyspark_code(extension_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    extension_id = 'extension_id_example' # str | 

    try:
        api_instance.generate_pyspark_code(extension_id)
    except Exception as e:
        print("Exception when calling DefaultApi->generate_pyspark_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent**
> get_agent(category_id, agent_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    category_id = 'category_id_example' # str | 
    agent_id = 'agent_id_example' # str | 

    try:
        api_instance.get_agent(category_id, agent_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **agent_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_extensions**
> get_agent_extensions(agent_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        api_instance.get_agent_extensions(agent_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_agent_extensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_from_name**
> get_agent_from_name(category_id, agent_name)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    category_id = 'category_id_example' # str | 
    agent_name = 'agent_name_example' # str | 

    try:
        api_instance.get_agent_from_name(category_id, agent_name)
    except Exception as e:
        print("Exception when calling DefaultApi->get_agent_from_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **agent_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_python_extensions**
> get_agent_python_extensions(agent_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        api_instance.get_agent_python_extensions(agent_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_agent_python_extensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_agents**
> get_all_agents(category_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    category_id = 'category_id_example' # str | 

    try:
        api_instance.get_all_agents(category_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_categories**
> get_all_categories()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_all_categories()
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cloud_credentials**
> get_all_cloud_credentials(provider=provider, page=page, page_size=page_size)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider = 'provider_example' # str |  (optional)
    page = 0 # int |  (optional) (default to 0)
    page_size = 50 # int |  (optional) (default to 50)

    try:
        api_instance.get_all_cloud_credentials(provider=provider, page=page, page_size=page_size)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_cloud_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_dataset_versions**
> get_all_dataset_versions()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_all_dataset_versions()
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_dataset_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_datasets**
> get_all_datasets(status=status)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    status = 'status_example' # str |  (optional)

    try:
        api_instance.get_all_datasets(status=status)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_datasets1**
> get_all_datasets1(type=type, indexed=indexed, format=format)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    type = 'type_example' # str |  (optional)
    indexed = 'indexed_example' # str |  (optional)
    format = 'format_example' # str |  (optional)

    try:
        api_instance.get_all_datasets1(type=type, indexed=indexed, format=format)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_datasets1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **indexed** | **str**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_installations**
> get_all_installations(organization_id=organization_id, enabled_only=enabled_only)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    organization_id = 'organization_id_example' # str |  (optional)
    enabled_only = True # bool |  (optional)

    try:
        api_instance.get_all_installations(organization_id=organization_id, enabled_only=enabled_only)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_installations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | [optional] 
 **enabled_only** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects**
> get_all_projects()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_all_projects()
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_projects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tasks**
> get_all_tasks(project_id, job_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        api_instance.get_all_tasks(project_id, job_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_versions**
> get_all_versions(build_type=build_type, active_only=active_only)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    build_type = 'build_type_example' # str |  (optional)
    active_only = True # bool |  (optional)

    try:
        api_instance.get_all_versions(build_type=build_type, active_only=active_only)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_type** | **str**|  | [optional] 
 **active_only** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_versionsets**
> get_all_versionsets(dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.get_all_versionsets(dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_versionsets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_plans**
> get_billing_plans(organization_id=organization_id, standard=standard)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    organization_id = 56 # int |  (optional)
    standard = True # bool |  (optional)

    try:
        api_instance.get_billing_plans(organization_id=organization_id, standard=standard)
    except Exception as e:
        print("Exception when calling DefaultApi->get_billing_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 
 **standard** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bootstrap_status**
> get_bootstrap_status()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_bootstrap_status()
    except Exception as e:
        print("Exception when calling DefaultApi->get_bootstrap_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_scan**
> get_bundle_scan(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.get_bundle_scan(id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_bundle_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id**
> get_by_id(table, id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    table = 'table_example' # str | 
    id = 'id_example' # str | 

    try:
        api_instance.get_by_id(table, id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_capabilities**
> get_capabilities()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_capabilities()
    except Exception as e:
        print("Exception when calling DefaultApi->get_capabilities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_stages**
> get_catalog_stages(search=search)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    search = 'search_example' # str |  (optional)

    try:
        api_instance.get_catalog_stages(search=search)
    except Exception as e:
        print("Exception when calling DefaultApi->get_catalog_stages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> get_category(category_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    category_id = 'category_id_example' # str | 

    try:
        api_instance.get_category(category_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_from_name**
> get_category_from_name(category_name)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    category_name = 'category_name_example' # str | 

    try:
        api_instance.get_category_from_name(category_name)
    except Exception as e:
        print("Exception when calling DefaultApi->get_category_from_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_credential_by_id**
> get_cloud_credential_by_id(credential_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    credential_id = 'credential_id_example' # str | 

    try:
        api_instance.get_cloud_credential_by_id(credential_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_cloud_credential_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_credentials_by_provider**
> get_cloud_credentials_by_provider(provider)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider = 'provider_example' # str | 

    try:
        api_instance.get_cloud_credentials_by_provider(provider)
    except Exception as e:
        print("Exception when calling DefaultApi->get_cloud_credentials_by_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cron_job**
> get_cron_job(name, namespace=namespace)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    name = 'name_example' # str | 
    namespace = 'namespace_example' # str |  (optional)

    try:
        api_instance.get_cron_job(name, namespace=namespace)
    except Exception as e:
        print("Exception when calling DefaultApi->get_cron_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> get_current_user()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_current_user()
    except Exception as e:
        print("Exception when calling DefaultApi->get_current_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> get_dataset(dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.get_dataset(dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset1**
> get_dataset1(dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.get_dataset1(dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_fields**
> get_dataset_fields(dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.get_dataset_fields(dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_info_by_task**
> get_dataset_info_by_task(task_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        api_instance.get_dataset_info_by_task(task_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset_info_by_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_input_file**
> get_dataset_input_file(dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.get_dataset_input_file(dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset_input_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_input_file_pagination**
> get_dataset_input_file_pagination(offset, dataset_id, limit)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    offset = 56 # int | 
    dataset_id = 'dataset_id_example' # str | 
    limit = 56 # int | 

    try:
        api_instance.get_dataset_input_file_pagination(offset, dataset_id, limit)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset_input_file_pagination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | 
 **dataset_id** | **str**|  | 
 **limit** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_input_file_size**
> get_dataset_input_file_size(dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.get_dataset_input_file_size(dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset_input_file_size: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_status**
> get_dataset_status(dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.get_dataset_status(dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_version_input_file**
> get_dataset_version_input_file(category_id, job_id, versionset_id, dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    category_id = 'category_id_example' # str | 
    job_id = 'job_id_example' # str | 
    versionset_id = 'versionset_id_example' # str | 
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.get_dataset_version_input_file(category_id, job_id, versionset_id, dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset_version_input_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **job_id** | **str**|  | 
 **versionset_id** | **str**|  | 
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_version_input_file_pagination**
> get_dataset_version_input_file_pagination(project_id, bot_id, offset, limit, versionset_id, dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    bot_id = 'bot_id_example' # str | 
    offset = 56 # int | 
    limit = 56 # int | 
    versionset_id = 'versionset_id_example' # str | 
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.get_dataset_version_input_file_pagination(project_id, bot_id, offset, limit, versionset_id, dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset_version_input_file_pagination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **bot_id** | **str**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 
 **versionset_id** | **str**|  | 
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_entitlements**
> get_effective_entitlements(organization_id=organization_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    organization_id = 56 # int |  (optional)

    try:
        api_instance.get_effective_entitlements(organization_id=organization_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_effective_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_logs**
> get_execution_logs(execution_id, tail=tail, pod_type=pod_type, executor_index=executor_index)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    execution_id = 'execution_id_example' # str | 
    tail = 56 # int |  (optional)
    pod_type = 'pod_type_example' # str |  (optional)
    executor_index = 56 # int |  (optional)

    try:
        api_instance.get_execution_logs(execution_id, tail=tail, pod_type=pod_type, executor_index=executor_index)
    except Exception as e:
        print("Exception when calling DefaultApi->get_execution_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**|  | 
 **tail** | **int**|  | [optional] 
 **pod_type** | **str**|  | [optional] 
 **executor_index** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_logs1**
> get_execution_logs1(project_id, job_id, execution_id, pod_type=pod_type, executor_index=executor_index, pod_name=pod_name, tail=tail)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    execution_id = 'execution_id_example' # str | 
    pod_type = 'pod_type_example' # str |  (optional)
    executor_index = 56 # int |  (optional)
    pod_name = 'pod_name_example' # str |  (optional)
    tail = 56 # int |  (optional)

    try:
        api_instance.get_execution_logs1(project_id, job_id, execution_id, pod_type=pod_type, executor_index=executor_index, pod_name=pod_name, tail=tail)
    except Exception as e:
        print("Exception when calling DefaultApi->get_execution_logs1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **execution_id** | **str**|  | 
 **pod_type** | **str**|  | [optional] 
 **executor_index** | **int**|  | [optional] 
 **pod_name** | **str**|  | [optional] 
 **tail** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_output**
> get_execution_output(execution_id, limit=limit, dataset_id=dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    execution_id = 'execution_id_example' # str | 
    limit = 56 # int |  (optional)
    dataset_id = 56 # int |  (optional)

    try:
        api_instance.get_execution_output(execution_id, limit=limit, dataset_id=dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_execution_output: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **dataset_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_status**
> get_execution_status(execution_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    execution_id = 'execution_id_example' # str | 

    try:
        api_instance.get_execution_status(execution_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_execution_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_status1**
> get_execution_status1(project_id, job_id, execution_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    execution_id = 'execution_id_example' # str | 

    try:
        api_instance.get_execution_status1(project_id, job_id, execution_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_execution_status1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **execution_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health**
> get_health()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_health()
    except Exception as e:
        print("Exception when calling DefaultApi->get_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_html**
> get_html(protocol, url)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    protocol = 'protocol_example' # str | 
    url = 'url_example' # str | 

    try:
        api_instance.get_html(protocol, url)
    except Exception as e:
        print("Exception when calling DefaultApi->get_html: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol** | **str**|  | 
 **url** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images_simplified**
> get_images_simplified(country, organization_code=organization_code, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    country = 'country_example' # str | 
    organization_code = 'organization_code_example' # str |  (optional)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.get_images_simplified(country, organization_code=organization_code, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->get_images_simplified: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | 
 **organization_code** | **str**|  | [optional] 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_info**
> get_info()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_info()
    except Exception as e:
        print("Exception when calling DefaultApi->get_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_info1**
> get_info1()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_info1()
    except Exception as e:
        print("Exception when calling DefaultApi->get_info1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installation_by_id**
> get_installation_by_id(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.get_installation_by_id(id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_installation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> get_job(project_id, job_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        api_instance.get_job(project_id, job_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_logs**
> get_job_logs(project_id, job_id, task_id=task_id, pod_type=pod_type, executor_index=executor_index, pod_name=pod_name, tail=tail)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    task_id = 56 # int |  (optional)
    pod_type = 'pod_type_example' # str |  (optional)
    executor_index = 56 # int |  (optional)
    pod_name = 'pod_name_example' # str |  (optional)
    tail = 56 # int |  (optional)

    try:
        api_instance.get_job_logs(project_id, job_id, task_id=task_id, pod_type=pod_type, executor_index=executor_index, pod_name=pod_name, tail=tail)
    except Exception as e:
        print("Exception when calling DefaultApi->get_job_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **int**|  | [optional] 
 **pod_type** | **str**|  | [optional] 
 **executor_index** | **int**|  | [optional] 
 **pod_name** | **str**|  | [optional] 
 **tail** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_metrics**
> get_job_metrics(project_id, job_id, start_time=start_time, end_time=end_time)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    start_time = 'start_time_example' # str |  (optional)
    end_time = 'end_time_example' # str |  (optional)

    try:
        api_instance.get_job_metrics(project_id, job_id, start_time=start_time, end_time=end_time)
    except Exception as e:
        print("Exception when calling DefaultApi->get_job_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **start_time** | **str**|  | [optional] 
 **end_time** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> get_organization(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.get_organization(id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_plugins**
> get_organization_plugins(organization_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        api_instance.get_organization_plugins(organization_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_organization_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_users**
> get_organization_users(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.get_organization_users(id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_organization_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partners_by_type**
> get_partners_by_type(type)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    type = 'type_example' # str | 

    try:
        api_instance.get_partners_by_type(type)
    except Exception as e:
        print("Exception when calling DefaultApi->get_partners_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_info**
> get_plugin_info()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_plugin_info()
    except Exception as e:
        print("Exception when calling DefaultApi->get_plugin_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_info1**
> get_plugin_info1()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_plugin_info1()
    except Exception as e:
        print("Exception when calling DefaultApi->get_plugin_info1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_info2**
> get_plugin_info2()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_plugin_info2()
    except Exception as e:
        print("Exception when calling DefaultApi->get_plugin_info2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_organizations**
> get_plugin_organizations(plugin_installation_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    plugin_installation_id = 56 # int | 

    try:
        api_instance.get_plugin_organizations(plugin_installation_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_plugin_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_installation_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_usage**
> get_plugin_usage(plugin_id, var_from=var_from, to=to, organization_id=organization_id, group_by=group_by)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    plugin_id = 'plugin_id_example' # str | 
    var_from = 'var_from_example' # str |  (optional)
    to = 'to_example' # str |  (optional)
    organization_id = 'organization_id_example' # str |  (optional)
    group_by = 'stage' # str |  (optional) (default to 'stage')

    try:
        api_instance.get_plugin_usage(plugin_id, var_from=var_from, to=to, organization_id=organization_id, group_by=group_by)
    except Exception as e:
        print("Exception when calling DefaultApi->get_plugin_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 
 **var_from** | **str**|  | [optional] 
 **to** | **str**|  | [optional] 
 **organization_id** | **str**|  | [optional] 
 **group_by** | **str**|  | [optional] [default to &#39;stage&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> get_profile(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.get_profile(id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> get_project(project_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_instance.get_project(project_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_from_name**
> get_project_from_name(project_name)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_name = 'project_name_example' # str | 

    try:
        api_instance.get_project_from_name(project_name)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_from_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_jobs**
> get_project_jobs(project_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_instance.get_project_jobs(project_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_metrics**
> get_project_metrics(project_id, start_time=start_time, end_time=end_time)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    start_time = 'start_time_example' # str |  (optional)
    end_time = 'end_time_example' # str |  (optional)

    try:
        api_instance.get_project_metrics(project_id, start_time=start_time, end_time=end_time)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **start_time** | **str**|  | [optional] 
 **end_time** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_schedule**
> get_project_schedule(project_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_instance.get_project_schedule(project_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stage**
> get_stage(name)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    name = 'name_example' # str | 

    try:
        api_instance.get_stage(name)
    except Exception as e:
        print("Exception when calling DefaultApi->get_stage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> get_status(country)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    country = 'country_example' # str | 

    try:
        api_instance.get_status(country)
    except Exception as e:
        print("Exception when calling DefaultApi->get_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_extension_types**
> get_supported_extension_types()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_supported_extension_types()
    except Exception as e:
        print("Exception when calling DefaultApi->get_supported_extension_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_models**
> get_supported_models(provider)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider = 'provider_example' # str | 

    try:
        api_instance.get_supported_models(provider)
    except Exception as e:
        print("Exception when calling DefaultApi->get_supported_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_providers**
> get_supported_providers()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_supported_providers()
    except Exception as e:
        print("Exception when calling DefaultApi->get_supported_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_logs**
> get_system_logs(service=service, level=level, tail=tail, start_time=start_time, end_time=end_time)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    service = 'service_example' # str |  (optional)
    level = 'level_example' # str |  (optional)
    tail = 56 # int |  (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)

    try:
        api_instance.get_system_logs(service=service, level=level, tail=tail, start_time=start_time, end_time=end_time)
    except Exception as e:
        print("Exception when calling DefaultApi->get_system_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  | [optional] 
 **level** | **str**|  | [optional] 
 **tail** | **int**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_columns**
> get_table_columns(catalog=catalog, var_schema=var_schema, table=table)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    catalog = 'minio' # str |  (optional) (default to 'minio')
    var_schema = 'default' # str |  (optional) (default to 'default')
    table = 'table_example' # str |  (optional)

    try:
        api_instance.get_table_columns(catalog=catalog, var_schema=var_schema, table=table)
    except Exception as e:
        print("Exception when calling DefaultApi->get_table_columns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**|  | [optional] [default to &#39;minio&#39;]
 **var_schema** | **str**|  | [optional] [default to &#39;default&#39;]
 **table** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> get_task(project_id, job_id, task_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    task_id = 'task_id_example' # str | 

    try:
        api_instance.get_task(project_id, job_id, task_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_by_output_dataset**
> get_task_by_output_dataset(dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.get_task_by_output_dataset(dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_task_by_output_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_metrics**
> get_task_metrics(project_id, job_id, task_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    task_id = 'task_id_example' # str | 

    try:
        api_instance.get_task_metrics(project_id, job_id, task_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_task_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_status**
> get_task_status(project_id, job_id, task_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    task_id = 'task_id_example' # str | 

    try:
        api_instance.get_task_status(project_id, job_id, task_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_task_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_logs**
> get_training_logs(provider, job_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider = 'provider_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        api_instance.get_training_logs(provider, job_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_training_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_status**
> get_training_status(provider, job_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider = 'provider_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        api_instance.get_training_status(provider, job_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_training_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ui_definitions**
> get_ui_definitions(organization_id=organization_id, build_type=build_type)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    organization_id = 'organization_id_example' # str |  (optional)
    build_type = 'build_type_example' # str |  (optional)

    try:
        api_instance.get_ui_definitions(organization_id=organization_id, build_type=build_type)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ui_definitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | [optional] 
 **build_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_file_url**
> get_upload_file_url(project_id, bot_id, attachment_name)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    bot_id = 'bot_id_example' # str | 
    attachment_name = 'attachment_name_example' # str | 

    try:
        api_instance.get_upload_file_url(project_id, bot_id, attachment_name)
    except Exception as e:
        print("Exception when calling DefaultApi->get_upload_file_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **bot_id** | **str**|  | 
 **attachment_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_url_download**
> get_url_download()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_url_download()
    except Exception as e:
        print("Exception when calling DefaultApi->get_url_download: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_url_upload**
> get_url_upload()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_url_upload()
    except Exception as e:
        print("Exception when calling DefaultApi->get_url_upload: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_invites**
> get_user_invites()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.get_user_invites()
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_invites: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_by_build_type_and_build_number**
> get_version_by_build_type_and_build_number(build_type, build_number)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    build_type = 'build_type_example' # str | 
    build_number = 56 # int | 

    try:
        api_instance.get_version_by_build_type_and_build_number(build_type, build_number)
    except Exception as e:
        print("Exception when calling DefaultApi->get_version_by_build_type_and_build_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_type** | **str**|  | 
 **build_number** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_by_id**
> get_version_by_id(id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 

    try:
        api_instance.get_version_by_id(id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_version_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versionset**
> get_versionset(versionset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    versionset_id = 'versionset_id_example' # str | 

    try:
        api_instance.get_versionset(versionset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_versionset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versionset_from_version**
> get_versionset_from_version(dataset_id, version, time_period=time_period)

### Example


```python
import webrobot
from webrobot.models.time_period import TimePeriod
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    version = 'version_example' # str | 
    time_period = webrobot.TimePeriod() # TimePeriod |  (optional)

    try:
        api_instance.get_versionset_from_version(dataset_id, version, time_period=time_period)
    except Exception as e:
        print("Exception when calling DefaultApi->get_versionset_from_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **version** | **str**|  | 
 **time_period** | [**TimePeriod**](TimePeriod.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versionset_from_version_base**
> get_versionset_from_version_base(dataset_id, version)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    version = 'version_example' # str | 

    try:
        api_instance.get_versionset_from_version_base(dataset_id, version)
    except Exception as e:
        print("Exception when calling DefaultApi->get_versionset_from_version_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check**
> health_check()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.health_check()
    except Exception as e:
        print("Exception when calling DefaultApi->health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check1**
> health_check1()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.health_check1()
    except Exception as e:
        print("Exception when calling DefaultApi->health_check1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_dataset**
> index_dataset(dataset_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 

    try:
        api_instance.index_dataset(dataset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->index_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infer**
> infer(infer_request=infer_request)

### Example


```python
import webrobot
from webrobot.models.infer_request import InferRequest
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    infer_request = webrobot.InferRequest() # InferRequest |  (optional)

    try:
        api_instance.infer(infer_request=infer_request)
    except Exception as e:
        print("Exception when calling DefaultApi->infer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infer_request** | [**InferRequest**](InferRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert**
> insert(table, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    table = 'table_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.insert(table, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->insert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_bundle**
> install_bundle(build_type=build_type, bundle=bundle, build_type2=build_type2, force=force)

### Example


```python
import webrobot
from webrobot.models.form_data_content_disposition import FormDataContentDisposition
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    build_type = 'build_type_example' # str |  (optional)
    bundle = webrobot.FormDataContentDisposition() # FormDataContentDisposition |  (optional)
    build_type2 = 'build_type_example' # str |  (optional)
    force = True # bool |  (optional)

    try:
        api_instance.install_bundle(build_type=build_type, bundle=bundle, build_type2=build_type2, force=force)
    except Exception as e:
        print("Exception when calling DefaultApi->install_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_type** | **str**|  | [optional] 
 **bundle** | [**FormDataContentDisposition**](FormDataContentDisposition.md)|  | [optional] 
 **build_type2** | **str**|  | [optional] 
 **force** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_completion_webhook**
> job_completion_webhook(project_id, job_id, job_completion_webhook_request=job_completion_webhook_request)

### Example


```python
import webrobot
from webrobot.models.job_completion_webhook_request import JobCompletionWebhookRequest
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    job_completion_webhook_request = webrobot.JobCompletionWebhookRequest() # JobCompletionWebhookRequest |  (optional)

    try:
        api_instance.job_completion_webhook(project_id, job_id, job_completion_webhook_request=job_completion_webhook_request)
    except Exception as e:
        print("Exception when calling DefaultApi->job_completion_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **job_completion_webhook_request** | [**JobCompletionWebhookRequest**](JobCompletionWebhookRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_adapters**
> list_adapters()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.list_adapters()
    except Exception as e:
        print("Exception when calling DefaultApi->list_adapters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> list_api_keys(organization=organization, organization_code=organization_code)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    organization = 'organization_example' # str |  (optional)
    organization_code = 'organization_code_example' # str |  (optional)

    try:
        api_instance.list_api_keys(organization=organization, organization_code=organization_code)
    except Exception as e:
        print("Exception when calling DefaultApi->list_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | [optional] 
 **organization_code** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available**
> list_available()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.list_available()
    except Exception as e:
        print("Exception when calling DefaultApi->list_available: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bundles**
> list_bundles(status=status)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    status = 'status_example' # str |  (optional)

    try:
        api_instance.list_bundles(status=status)
    except Exception as e:
        print("Exception when calling DefaultApi->list_bundles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_charges**
> list_charges(period=period)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    period = 'period_example' # str |  (optional)

    try:
        api_instance.list_charges(period=period)
    except Exception as e:
        print("Exception when calling DefaultApi->list_charges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cli_plugins**
> list_cli_plugins()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.list_cli_plugins()
    except Exception as e:
        print("Exception when calling DefaultApi->list_cli_plugins: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cron_jobs**
> list_cron_jobs(namespace=namespace)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    namespace = 'namespace_example' # str |  (optional)

    try:
        api_instance.list_cron_jobs(namespace=namespace)
    except Exception as e:
        print("Exception when calling DefaultApi->list_cron_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_demos**
> list_demos()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.list_demos()
    except Exception as e:
        print("Exception when calling DefaultApi->list_demos: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_executions**
> list_executions(limit=limit, organization_id=organization_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    organization_id = 'organization_id_example' # str |  (optional)

    try:
        api_instance.list_executions(limit=limit, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling DefaultApi->list_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **organization_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_my_adapters**
> list_my_adapters()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.list_my_adapters()
    except Exception as e:
        print("Exception when calling DefaultApi->list_my_adapters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payouts**
> list_payouts(period=period)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    period = 'period_example' # str |  (optional)

    try:
        api_instance.list_payouts(period=period)
    except Exception as e:
        print("Exception when calling DefaultApi->list_payouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plugins**
> list_plugins(build_type=build_type)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    build_type = 'development' # str |  (optional) (default to 'development')

    try:
        api_instance.list_plugins(build_type=build_type)
    except Exception as e:
        print("Exception when calling DefaultApi->list_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_type** | **str**|  | [optional] [default to &#39;development&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_profiles**
> list_profiles(enabled_only=enabled_only, organization_id=organization_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    enabled_only = False # bool |  (optional) (default to False)
    organization_id = 'organization_id_example' # str |  (optional)

    try:
        api_instance.list_profiles(enabled_only=enabled_only, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling DefaultApi->list_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled_only** | **bool**|  | [optional] [default to False]
 **organization_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> list_providers()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.list_providers()
    except Exception as e:
        print("Exception when calling DefaultApi->list_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_revenue_share**
> list_revenue_share(period=period)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    period = 'period_example' # str |  (optional)

    try:
        api_instance.list_revenue_share(period=period)
    except Exception as e:
        print("Exception when calling DefaultApi->list_revenue_share: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stages**
> list_stages(plugin_id=plugin_id, stage_name=stage_name, plugin_type=plugin_type, scope=scope)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    plugin_id = 'plugin_id_example' # str |  (optional)
    stage_name = 'stage_name_example' # str |  (optional)
    plugin_type = 'plugin_type_example' # str |  (optional)
    scope = 'org' # str |  (optional) (default to 'org')

    try:
        api_instance.list_stages(plugin_id=plugin_id, stage_name=stage_name, plugin_type=plugin_type, scope=scope)
    except Exception as e:
        print("Exception when calling DefaultApi->list_stages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | [optional] 
 **stage_name** | **str**|  | [optional] 
 **plugin_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] [default to &#39;org&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stages1**
> list_stages1(category=category, type=type, search=search)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    category = 'category_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        api_instance.list_stages1(category=category, type=type, search=search)
    except Exception as e:
        print("Exception when calling DefaultApi->list_stages1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tables**
> list_tables(catalog=catalog, var_schema=var_schema)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    catalog = 'minio' # str |  (optional) (default to 'minio')
    var_schema = 'default' # str |  (optional) (default to 'default')

    try:
        api_instance.list_tables(catalog=catalog, var_schema=var_schema)
    except Exception as e:
        print("Exception when calling DefaultApi->list_tables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**|  | [optional] [default to &#39;minio&#39;]
 **var_schema** | **str**|  | [optional] [default to &#39;default&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_failed**
> mark_failed(invoice_id, reason=reason)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    invoice_id = 'invoice_id_example' # str | 
    reason = 'reason_example' # str |  (optional)

    try:
        api_instance.mark_failed(invoice_id, reason=reason)
    except Exception as e:
        print("Exception when calling DefaultApi->mark_failed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **reason** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_paid**
> mark_paid(invoice_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    invoice_id = 'invoice_id_example' # str | 

    try:
        api_instance.mark_paid(invoice_id)
    except Exception as e:
        print("Exception when calling DefaultApi->mark_paid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_zombie_tasks**
> mark_zombie_tasks(timeout_hours=timeout_hours)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    timeout_hours = 56 # int |  (optional)

    try:
        api_instance.mark_zombie_tasks(timeout_hours=timeout_hours)
    except Exception as e:
        print("Exception when calling DefaultApi->mark_zombie_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout_hours** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **probe_adapter**
> probe_adapter(provider_key)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider_key = 'provider_key_example' # str | 

    try:
        api_instance.probe_adapter(provider_key)
    except Exception as e:
        print("Exception when calling DefaultApi->probe_adapter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_yaml_extensions**
> process_yaml_extensions(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.process_yaml_extensions(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->process_yaml_extensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_model**
> publish_model(model_publish_request=model_publish_request)

### Example


```python
import webrobot
from webrobot.models.model_publish_request import ModelPublishRequest
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    model_publish_request = webrobot.ModelPublishRequest() # ModelPublishRequest |  (optional)

    try:
        api_instance.publish_model(model_publish_request=model_publish_request)
    except Exception as e:
        print("Exception when calling DefaultApi->publish_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_publish_request** | [**ModelPublishRequest**](ModelPublishRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_dataset_by_task**
> query_dataset_by_task(task_id, presto_query_request=presto_query_request)

### Example


```python
import webrobot
from webrobot.models.presto_query_request import PrestoQueryRequest
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    task_id = 'task_id_example' # str | 
    presto_query_request = webrobot.PrestoQueryRequest() # PrestoQueryRequest |  (optional)

    try:
        api_instance.query_dataset_by_task(task_id, presto_query_request=presto_query_request)
    except Exception as e:
        print("Exception when calling DefaultApi->query_dataset_by_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **presto_query_request** | [**PrestoQueryRequest**](PrestoQueryRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_images**
> query_images(country, organization_code=organization_code, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    country = 'country_example' # str | 
    organization_code = 'organization_code_example' # str |  (optional)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.query_images(country, organization_code=organization_code, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->query_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | 
 **organization_code** | **str**|  | [optional] 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_organizations_billing_status**
> refresh_organizations_billing_status()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.refresh_organizations_billing_status()
    except Exception as e:
        print("Exception when calling DefaultApi->refresh_organizations_billing_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund**
> refund(id, amount_cents=amount_cents, reason=reason)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 
    amount_cents = 56 # int |  (optional)
    reason = 'reason_example' # str |  (optional)

    try:
        api_instance.refund(id, amount_cents=amount_cents, reason=reason)
    except Exception as e:
        print("Exception when calling DefaultApi->refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **amount_cents** | **int**|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_plugin**
> register_plugin(plugin_installation=plugin_installation)

### Example


```python
import webrobot
from webrobot.models.plugin_installation import PluginInstallation
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    plugin_installation = webrobot.PluginInstallation() # PluginInstallation |  (optional)

    try:
        api_instance.register_plugin(plugin_installation=plugin_installation)
    except Exception as e:
        print("Exception when calling DefaultApi->register_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_installation** | [**PluginInstallation**](PluginInstallation.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_python_extension**
> register_python_extension(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.register_python_extension(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->register_python_extension: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_bundle**
> reject_bundle(id, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.reject_bundle(id, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->reject_bundle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_pipelines**
> reload_pipelines()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.reload_pipelines()
    except Exception as e:
        print("Exception when calling DefaultApi->reload_pipelines: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_plugins**
> reload_plugins()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.reload_plugins()
    except Exception as e:
        print("Exception when calling DefaultApi->reload_plugins: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_job_from_project**
> remove_job_from_project(project_id, job_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        api_instance.remove_job_from_project(project_id, job_id)
    except Exception as e:
        print("Exception when calling DefaultApi->remove_job_from_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_health**
> report_health(provider_key, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider_key = 'provider_key_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.report_health(provider_key, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->report_health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_key** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reschedule_events**
> reschedule_events(reschedule_events_request=reschedule_events_request)

### Example


```python
import webrobot
from webrobot.models.reschedule_events_request import RescheduleEventsRequest
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    reschedule_events_request = webrobot.RescheduleEventsRequest() # RescheduleEventsRequest |  (optional)

    try:
        api_instance.reschedule_events(reschedule_events_request=reschedule_events_request)
    except Exception as e:
        print("Exception when calling DefaultApi->reschedule_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reschedule_events_request** | [**RescheduleEventsRequest**](RescheduleEventsRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollup**
> rollup(day=day)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    day = 'day_example' # str |  (optional)

    try:
        api_instance.rollup(day=day)
    except Exception as e:
        print("Exception when calling DefaultApi->rollup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **day** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_charges**
> run_charges(period=period, dry_run=dry_run)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    period = 'period_example' # str |  (optional)
    dry_run = False # bool |  (optional) (default to False)

    try:
        api_instance.run_charges(period=period, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling DefaultApi->run_charges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**|  | [optional] 
 **dry_run** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_health_check**
> run_health_check()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.run_health_check()
    except Exception as e:
        print("Exception when calling DefaultApi->run_health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_orchestration_charges**
> run_orchestration_charges(period=period, dry_run=dry_run)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    period = 'period_example' # str |  (optional)
    dry_run = False # bool |  (optional) (default to False)

    try:
        api_instance.run_orchestration_charges(period=period, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling DefaultApi->run_orchestration_charges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**|  | [optional] 
 **dry_run** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_payouts**
> run_payouts(period=period, dry_run=dry_run)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    period = 'period_example' # str |  (optional)
    dry_run = False # bool |  (optional) (default to False)

    try:
        api_instance.run_payouts(period=period, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling DefaultApi->run_payouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**|  | [optional] 
 **dry_run** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_provider_endpoint_charges**
> run_provider_endpoint_charges(period=period, dry_run=dry_run)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    period = 'period_example' # str |  (optional)
    dry_run = False # bool |  (optional) (default to False)

    try:
        api_instance.run_provider_endpoint_charges(period=period, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling DefaultApi->run_provider_endpoint_charges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**|  | [optional] 
 **dry_run** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_revenue_share**
> run_revenue_share(period=period, dry_run=dry_run)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    period = 'period_example' # str |  (optional)
    dry_run = False # bool |  (optional) (default to False)

    try:
        api_instance.run_revenue_share(period=period, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling DefaultApi->run_revenue_share: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**|  | [optional] 
 **dry_run** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_generated_pipeline**
> save_generated_pipeline(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.save_generated_pipeline(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->save_generated_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_job**
> schedule_job(country, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    country = 'country_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.schedule_job(country, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->schedule_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_demo_app**
> serve_demo_app()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.serve_demo_app()
    except Exception as e:
        print("Exception when calling DefaultApi->serve_demo_app: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_static_file**
> serve_static_file(filename)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    filename = 'filename_example' # str | 

    try:
        api_instance.serve_static_file(filename)
    except Exception as e:
        print("Exception when calling DefaultApi->serve_static_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_schedule**
> set_project_schedule(project_id, project_schedule_request=project_schedule_request)

### Example


```python
import webrobot
from webrobot.models.project_schedule_request import ProjectScheduleRequest
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    project_schedule_request = webrobot.ProjectScheduleRequest() # ProjectScheduleRequest |  (optional)

    try:
        api_instance.set_project_schedule(project_id, project_schedule_request=project_schedule_request)
    except Exception as e:
        print("Exception when calling DefaultApi->set_project_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **project_schedule_request** | [**ProjectScheduleRequest**](ProjectScheduleRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> start(start_request=start_request)

### Example


```python
import webrobot
from webrobot.models.start_request import StartRequest
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    start_request = webrobot.StartRequest() # StartRequest |  (optional)

    try:
        api_instance.start(start_request=start_request)
    except Exception as e:
        print("Exception when calling DefaultApi->start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_request** | [**StartRequest**](StartRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_export_all**
> start_export_all()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.start_export_all()
    except Exception as e:
        print("Exception when calling DefaultApi->start_export_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_export_organization**
> start_export_organization(organization_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        api_instance.start_export_organization(organization_id)
    except Exception as e:
        print("Exception when calling DefaultApi->start_export_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_export_organization_with_options**
> start_export_organization_with_options(organization_id, export_options_dto=export_options_dto)

### Example


```python
import webrobot
from webrobot.models.export_options_dto import ExportOptionsDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    organization_id = 'organization_id_example' # str | 
    export_options_dto = webrobot.ExportOptionsDto() # ExportOptionsDto |  (optional)

    try:
        api_instance.start_export_organization_with_options(organization_id, export_options_dto=export_options_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->start_export_organization_with_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **export_options_dto** | [**ExportOptionsDto**](ExportOptionsDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_export_project**
> start_export_project(project_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_instance.start_export_project(project_id)
    except Exception as e:
        print("Exception when calling DefaultApi->start_export_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_import_all**
> start_import_all()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.start_import_all()
    except Exception as e:
        print("Exception when calling DefaultApi->start_import_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_import_all_with_options**
> start_import_all_with_options(import_options_dto=import_options_dto)

### Example


```python
import webrobot
from webrobot.models.import_options_dto import ImportOptionsDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    import_options_dto = webrobot.ImportOptionsDto() # ImportOptionsDto |  (optional)

    try:
        api_instance.start_import_all_with_options(import_options_dto=import_options_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->start_import_all_with_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_options_dto** | [**ImportOptionsDto**](ImportOptionsDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_import_organization**
> start_import_organization(organization_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        api_instance.start_import_organization(organization_id)
    except Exception as e:
        print("Exception when calling DefaultApi->start_import_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_import_organization_with_options**
> start_import_organization_with_options(organization_id, filename=filename, import_options_dto=import_options_dto)

### Example


```python
import webrobot
from webrobot.models.import_options_dto import ImportOptionsDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    organization_id = 'organization_id_example' # str | 
    filename = 'filename_example' # str |  (optional)
    import_options_dto = webrobot.ImportOptionsDto() # ImportOptionsDto |  (optional)

    try:
        api_instance.start_import_organization_with_options(organization_id, filename=filename, import_options_dto=import_options_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->start_import_organization_with_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **filename** | **str**|  | [optional] 
 **import_options_dto** | [**ImportOptionsDto**](ImportOptionsDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_import_project**
> start_import_project(project_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_instance.start_import_project(project_id)
    except Exception as e:
        print("Exception when calling DefaultApi->start_import_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_import_project_with_options**
> start_import_project_with_options(project_id, filename=filename, import_options_dto=import_options_dto)

### Example


```python
import webrobot
from webrobot.models.import_options_dto import ImportOptionsDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    filename = 'filename_example' # str |  (optional)
    import_options_dto = webrobot.ImportOptionsDto() # ImportOptionsDto |  (optional)

    try:
        api_instance.start_import_project_with_options(project_id, filename=filename, import_options_dto=import_options_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->start_import_project_with_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **filename** | **str**|  | [optional] 
 **import_options_dto** | [**ImportOptionsDto**](ImportOptionsDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_task**
> start_task(project_id, job_id, task_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    task_id = 'task_id_example' # str | 

    try:
        api_instance.start_task(project_id, job_id, task_id)
    except Exception as e:
        print("Exception when calling DefaultApi->start_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_training**
> start_training(provider, training_request_bean=training_request_bean)

### Example


```python
import webrobot
from webrobot.models.training_request_bean import TrainingRequestBean
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider = 'provider_example' # str | 
    training_request_bean = webrobot.TrainingRequestBean() # TrainingRequestBean |  (optional)

    try:
        api_instance.start_training(provider, training_request_bean=training_request_bean)
    except Exception as e:
        print("Exception when calling DefaultApi->start_training: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **training_request_bean** | [**TrainingRequestBean**](TrainingRequestBean.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> status(eid)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    eid = 'eid_example' # str | 

    try:
        api_instance.status(eid)
    except Exception as e:
        print("Exception when calling DefaultApi->status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_job**
> stop_job(project_id, job_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        api_instance.stop_job(project_id, job_id)
    except Exception as e:
        print("Exception when calling DefaultApi->stop_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_task**
> stop_task(project_id, job_id, task_id)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    task_id = 'task_id_example' # str | 

    try:
        api_instance.stop_task(project_id, job_id, task_id)
    except Exception as e:
        print("Exception when calling DefaultApi->stop_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggest_stages**
> suggest_stages(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.suggest_stages(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->suggest_stages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test**
> test()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.test()
    except Exception as e:
        print("Exception when calling DefaultApi->test: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test1**
> test1()

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)

    try:
        api_instance.test1()
    except Exception as e:
        print("Exception when calling DefaultApi->test1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_cloud_credential**
> test_cloud_credential(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.test_cloud_credential(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->test_cloud_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(table, id, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    table = 'table_example' # str | 
    id = 'id_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.update(table, id, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**|  | 
 **id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_adapter**
> update_adapter(provider_key, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider_key = 'provider_key_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.update_adapter(provider_key, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->update_adapter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_key** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent**
> update_agent(category_id, agent_id, agent_dto=agent_dto)

### Example


```python
import webrobot
from webrobot.models.agent_dto import AgentDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    category_id = 'category_id_example' # str | 
    agent_id = 'agent_id_example' # str | 
    agent_dto = webrobot.AgentDto() # AgentDto |  (optional)

    try:
        api_instance.update_agent(category_id, agent_id, agent_dto=agent_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->update_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **agent_id** | **str**|  | 
 **agent_dto** | [**AgentDto**](AgentDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_python_extensions**
> update_agent_python_extensions(agent_id, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.update_agent_python_extensions(agent_id, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->update_agent_python_extensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_plan**
> update_billing_plan(id, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.update_billing_plan(id, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->update_billing_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> update_category(category_id, job_category_dto=job_category_dto)

### Example


```python
import webrobot
from webrobot.models.job_category_dto import JobCategoryDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    category_id = 'category_id_example' # str | 
    job_category_dto = webrobot.JobCategoryDto() # JobCategoryDto |  (optional)

    try:
        api_instance.update_category(category_id, job_category_dto=job_category_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->update_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **job_category_dto** | [**JobCategoryDto**](JobCategoryDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_credential**
> update_cloud_credential(credential_id, cloud_credential=cloud_credential)

### Example


```python
import webrobot
from webrobot.models.cloud_credential import CloudCredential
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    credential_id = 'credential_id_example' # str | 
    cloud_credential = webrobot.CloudCredential() # CloudCredential |  (optional)

    try:
        api_instance.update_cloud_credential(credential_id, cloud_credential=cloud_credential)
    except Exception as e:
        print("Exception when calling DefaultApi->update_cloud_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 
 **cloud_credential** | [**CloudCredential**](CloudCredential.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> update_dataset(dataset_id, dataset_dto=dataset_dto)

### Example


```python
import webrobot
from webrobot.models.dataset_dto import DatasetDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    dataset_dto = webrobot.DatasetDto() # DatasetDto |  (optional)

    try:
        api_instance.update_dataset(dataset_id, dataset_dto=dataset_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->update_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **dataset_dto** | [**DatasetDto**](DatasetDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_installation**
> update_installation(id, plugin_installation=plugin_installation)

### Example


```python
import webrobot
from webrobot.models.plugin_installation import PluginInstallation
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 
    plugin_installation = webrobot.PluginInstallation() # PluginInstallation |  (optional)

    try:
        api_instance.update_installation(id, plugin_installation=plugin_installation)
    except Exception as e:
        print("Exception when calling DefaultApi->update_installation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **plugin_installation** | [**PluginInstallation**](PluginInstallation.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job**
> update_job(project_id, job_id, job_dto=job_dto)

### Example


```python
import webrobot
from webrobot.models.job_dto import JobDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    job_dto = webrobot.JobDto() # JobDto |  (optional)

    try:
        api_instance.update_job(project_id, job_id, job_dto=job_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->update_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **job_dto** | [**JobDto**](JobDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization**
> update_organization(id, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 'id_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.update_organization(id, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->update_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> update_profile(id, agentic_profile=agentic_profile)

### Example


```python
import webrobot
from webrobot.models.agentic_profile import AgenticProfile
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 
    agentic_profile = webrobot.AgenticProfile() # AgenticProfile |  (optional)

    try:
        api_instance.update_profile(id, agentic_profile=agentic_profile)
    except Exception as e:
        print("Exception when calling DefaultApi->update_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **agentic_profile** | [**AgenticProfile**](AgenticProfile.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> update_project(project_id, job_project_dto=job_project_dto)

### Example


```python
import webrobot
from webrobot.models.job_project_dto import JobProjectDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_project_dto = webrobot.JobProjectDto() # JobProjectDto |  (optional)

    try:
        api_instance.update_project(project_id, job_project_dto=job_project_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_project_dto** | [**JobProjectDto**](JobProjectDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_python_extension**
> update_python_extension(extension_id, request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    extension_id = 'extension_id_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.update_python_extension(extension_id, request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->update_python_extension: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> update_task(project_id, job_id, task_id, task_dto=task_dto)

### Example


```python
import webrobot
from webrobot.models.task_dto import TaskDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    job_id = 'job_id_example' # str | 
    task_id = 'task_id_example' # str | 
    task_dto = webrobot.TaskDto() # TaskDto |  (optional)

    try:
        api_instance.update_task(project_id, job_id, task_id, task_dto=task_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->update_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 
 **task_dto** | [**TaskDto**](TaskDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version**
> update_version(id, etl_library_version_api_dto=etl_library_version_api_dto)

### Example


```python
import webrobot
from webrobot.models.etl_library_version_api_dto import EtlLibraryVersionApiDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    id = 56 # int | 
    etl_library_version_api_dto = webrobot.EtlLibraryVersionApiDto() # EtlLibraryVersionApiDto |  (optional)

    try:
        api_instance.update_version(id, etl_library_version_api_dto=etl_library_version_api_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->update_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **etl_library_version_api_dto** | [**EtlLibraryVersionApiDto**](EtlLibraryVersionApiDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_csv**
> upload_csv(country, organization_code=organization_code, content_disposition=content_disposition, entity=entity, headers=headers, media_type=media_type, message_body_workers=message_body_workers, parent=parent, providers=providers, body_parts=body_parts, fields=fields, parameterized_headers=parameterized_headers)

### Example


```python
import webrobot
from webrobot.models.body_part import BodyPart
from webrobot.models.body_part_media_type import BodyPartMediaType
from webrobot.models.content_disposition import ContentDisposition
from webrobot.models.form_data_body_part import FormDataBodyPart
from webrobot.models.multi_part import MultiPart
from webrobot.models.parameterized_header import ParameterizedHeader
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    country = 'country_example' # str | 
    organization_code = 'organization_code_example' # str |  (optional)
    content_disposition = webrobot.ContentDisposition() # ContentDisposition |  (optional)
    entity = None # object |  (optional)
    headers = None # Dict[str, List[str]] |  (optional)
    media_type = webrobot.BodyPartMediaType() # BodyPartMediaType |  (optional)
    message_body_workers = None # object |  (optional)
    parent = webrobot.MultiPart() # MultiPart |  (optional)
    providers = None # object |  (optional)
    body_parts = [webrobot.BodyPart()] # List[BodyPart] |  (optional)
    fields = None # Dict[str, List[FormDataBodyPart]] |  (optional)
    parameterized_headers = None # Dict[str, List[ParameterizedHeader]] |  (optional)

    try:
        api_instance.upload_csv(country, organization_code=organization_code, content_disposition=content_disposition, entity=entity, headers=headers, media_type=media_type, message_body_workers=message_body_workers, parent=parent, providers=providers, body_parts=body_parts, fields=fields, parameterized_headers=parameterized_headers)
    except Exception as e:
        print("Exception when calling DefaultApi->upload_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | 
 **organization_code** | **str**|  | [optional] 
 **content_disposition** | [**ContentDisposition**](ContentDisposition.md)|  | [optional] 
 **entity** | [**object**](object.md)|  | [optional] 
 **headers** | [**Dict[str, List[str]]**](Dict.md)|  | [optional] 
 **media_type** | [**BodyPartMediaType**](BodyPartMediaType.md)|  | [optional] 
 **message_body_workers** | [**object**](object.md)|  | [optional] 
 **parent** | [**MultiPart**](MultiPart.md)|  | [optional] 
 **providers** | [**object**](object.md)|  | [optional] 
 **body_parts** | [**List[BodyPart]**](BodyPart.md)|  | [optional] 
 **fields** | [**Dict[str, List[FormDataBodyPart]]**](Dict.md)|  | [optional] 
 **parameterized_headers** | [**Dict[str, List[ParameterizedHeader]]**](Dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dataset**
> upload_dataset(pipeline_name, content_disposition=content_disposition, entity=entity, headers=headers, media_type=media_type, message_body_workers=message_body_workers, parent=parent, providers=providers, body_parts=body_parts, fields=fields, parameterized_headers=parameterized_headers)

### Example


```python
import webrobot
from webrobot.models.body_part import BodyPart
from webrobot.models.body_part_media_type import BodyPartMediaType
from webrobot.models.content_disposition import ContentDisposition
from webrobot.models.form_data_body_part import FormDataBodyPart
from webrobot.models.multi_part import MultiPart
from webrobot.models.parameterized_header import ParameterizedHeader
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    pipeline_name = 'pipeline_name_example' # str | 
    content_disposition = webrobot.ContentDisposition() # ContentDisposition |  (optional)
    entity = None # object |  (optional)
    headers = None # Dict[str, List[str]] |  (optional)
    media_type = webrobot.BodyPartMediaType() # BodyPartMediaType |  (optional)
    message_body_workers = None # object |  (optional)
    parent = webrobot.MultiPart() # MultiPart |  (optional)
    providers = None # object |  (optional)
    body_parts = [webrobot.BodyPart()] # List[BodyPart] |  (optional)
    fields = None # Dict[str, List[FormDataBodyPart]] |  (optional)
    parameterized_headers = None # Dict[str, List[ParameterizedHeader]] |  (optional)

    try:
        api_instance.upload_dataset(pipeline_name, content_disposition=content_disposition, entity=entity, headers=headers, media_type=media_type, message_body_workers=message_body_workers, parent=parent, providers=providers, body_parts=body_parts, fields=fields, parameterized_headers=parameterized_headers)
    except Exception as e:
        print("Exception when calling DefaultApi->upload_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_name** | **str**|  | 
 **content_disposition** | [**ContentDisposition**](ContentDisposition.md)|  | [optional] 
 **entity** | [**object**](object.md)|  | [optional] 
 **headers** | [**Dict[str, List[str]]**](Dict.md)|  | [optional] 
 **media_type** | [**BodyPartMediaType**](BodyPartMediaType.md)|  | [optional] 
 **message_body_workers** | [**object**](object.md)|  | [optional] 
 **parent** | [**MultiPart**](MultiPart.md)|  | [optional] 
 **providers** | [**object**](object.md)|  | [optional] 
 **body_parts** | [**List[BodyPart]**](BodyPart.md)|  | [optional] 
 **fields** | [**Dict[str, List[FormDataBodyPart]]**](Dict.md)|  | [optional] 
 **parameterized_headers** | [**Dict[str, List[ParameterizedHeader]]**](Dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dataset1**
> upload_dataset1(provider, dataset_upload_request=dataset_upload_request)

### Example


```python
import webrobot
from webrobot.models.dataset_upload_request import DatasetUploadRequest
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    provider = 'provider_example' # str | 
    dataset_upload_request = webrobot.DatasetUploadRequest() # DatasetUploadRequest |  (optional)

    try:
        api_instance.upload_dataset1(provider, dataset_upload_request=dataset_upload_request)
    except Exception as e:
        print("Exception when calling DefaultApi->upload_dataset1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **dataset_upload_request** | [**DatasetUploadRequest**](DatasetUploadRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dataset2**
> upload_dataset2(dataset_upload_api_dto=dataset_upload_api_dto)

### Example


```python
import webrobot
from webrobot.models.dataset_upload_api_dto import DatasetUploadApiDto
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    dataset_upload_api_dto = webrobot.DatasetUploadApiDto() # DatasetUploadApiDto |  (optional)

    try:
        api_instance.upload_dataset2(dataset_upload_api_dto=dataset_upload_api_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->upload_dataset2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_upload_api_dto** | [**DatasetUploadApiDto**](DatasetUploadApiDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dataset_file**
> upload_dataset_file(content_disposition=content_disposition, entity=entity, headers=headers, media_type=media_type, message_body_workers=message_body_workers, parent=parent, providers=providers, body_parts=body_parts, fields=fields, parameterized_headers=parameterized_headers)

### Example


```python
import webrobot
from webrobot.models.body_part import BodyPart
from webrobot.models.body_part_media_type import BodyPartMediaType
from webrobot.models.content_disposition import ContentDisposition
from webrobot.models.form_data_body_part import FormDataBodyPart
from webrobot.models.multi_part import MultiPart
from webrobot.models.parameterized_header import ParameterizedHeader
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    content_disposition = webrobot.ContentDisposition() # ContentDisposition |  (optional)
    entity = None # object |  (optional)
    headers = None # Dict[str, List[str]] |  (optional)
    media_type = webrobot.BodyPartMediaType() # BodyPartMediaType |  (optional)
    message_body_workers = None # object |  (optional)
    parent = webrobot.MultiPart() # MultiPart |  (optional)
    providers = None # object |  (optional)
    body_parts = [webrobot.BodyPart()] # List[BodyPart] |  (optional)
    fields = None # Dict[str, List[FormDataBodyPart]] |  (optional)
    parameterized_headers = None # Dict[str, List[ParameterizedHeader]] |  (optional)

    try:
        api_instance.upload_dataset_file(content_disposition=content_disposition, entity=entity, headers=headers, media_type=media_type, message_body_workers=message_body_workers, parent=parent, providers=providers, body_parts=body_parts, fields=fields, parameterized_headers=parameterized_headers)
    except Exception as e:
        print("Exception when calling DefaultApi->upload_dataset_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_disposition** | [**ContentDisposition**](ContentDisposition.md)|  | [optional] 
 **entity** | [**object**](object.md)|  | [optional] 
 **headers** | [**Dict[str, List[str]]**](Dict.md)|  | [optional] 
 **media_type** | [**BodyPartMediaType**](BodyPartMediaType.md)|  | [optional] 
 **message_body_workers** | [**object**](object.md)|  | [optional] 
 **parent** | [**MultiPart**](MultiPart.md)|  | [optional] 
 **providers** | [**object**](object.md)|  | [optional] 
 **body_parts** | [**List[BodyPart]**](BodyPart.md)|  | [optional] 
 **fields** | [**Dict[str, List[FormDataBodyPart]]**](Dict.md)|  | [optional] 
 **parameterized_headers** | [**Dict[str, List[ParameterizedHeader]]**](Dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> upload_file(file=file)

### Example


```python
import webrobot
from webrobot.models.form_data_content_disposition import FormDataContentDisposition
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    file = webrobot.FormDataContentDisposition() # FormDataContentDisposition |  (optional)

    try:
        api_instance.upload_file(file=file)
    except Exception as e:
        print("Exception when calling DefaultApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**FormDataContentDisposition**](FormDataContentDisposition.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_plugin**
> upload_plugin(file=file, plugin_id=plugin_id, plugin_type=plugin_type, build_type=build_type, build_number=build_number, organization_ids=organization_ids)

### Example


```python
import webrobot
from webrobot.models.form_data_content_disposition import FormDataContentDisposition
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    file = webrobot.FormDataContentDisposition() # FormDataContentDisposition |  (optional)
    plugin_id = 'plugin_id_example' # str |  (optional)
    plugin_type = 'api' # str |  (optional) (default to 'api')
    build_type = 'development' # str |  (optional) (default to 'development')
    build_number = 56 # int |  (optional)
    organization_ids = 'organization_ids_example' # str |  (optional)

    try:
        api_instance.upload_plugin(file=file, plugin_id=plugin_id, plugin_type=plugin_type, build_type=build_type, build_number=build_number, organization_ids=organization_ids)
    except Exception as e:
        print("Exception when calling DefaultApi->upload_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**FormDataContentDisposition**](FormDataContentDisposition.md)|  | [optional] 
 **plugin_id** | **str**|  | [optional] 
 **plugin_type** | **str**|  | [optional] [default to &#39;api&#39;]
 **build_type** | **str**|  | [optional] [default to &#39;development&#39;]
 **build_number** | **int**|  | [optional] 
 **organization_ids** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate**
> validate(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.validate(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_python_extension**
> validate_python_extension(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.validate_python_extension(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->validate_python_extension: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wizard_infer_actions**
> wizard_infer_actions(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.wizard_infer_actions(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->wizard_infer_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wizard_infer_fields**
> wizard_infer_fields(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.wizard_infer_fields(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->wizard_infer_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wizard_infer_segment**
> wizard_infer_segment(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.wizard_infer_segment(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->wizard_infer_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wizard_infer_selector**
> wizard_infer_selector(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.wizard_infer_selector(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->wizard_infer_selector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wizard_proxy**
> wizard_proxy(url=url, strategy=strategy)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    url = 'url_example' # str |  (optional)
    strategy = 'strategy_example' # str |  (optional)

    try:
        api_instance.wizard_proxy(url=url, strategy=strategy)
    except Exception as e:
        print("Exception when calling DefaultApi->wizard_proxy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | [optional] 
 **strategy** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wizard_suggest_field_names**
> wizard_suggest_field_names(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.wizard_suggest_field_names(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->wizard_suggest_field_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wizard_validate**
> wizard_validate(request_body=request_body)

### Example


```python
import webrobot
from webrobot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webrobot.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webrobot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webrobot.DefaultApi(api_client)
    request_body = None # Dict[str, object] |  (optional)

    try:
        api_instance.wizard_validate(request_body=request_body)
    except Exception as e:
        print("Exception when calling DefaultApi->wizard_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

