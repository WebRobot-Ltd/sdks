# webrobot.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_job_to_project**](DefaultApi.md#add_job_to_project) | **POST** /webrobot/api/projects/id/{projectId}/jobs | 
[**cancel_training**](DefaultApi.md#cancel_training) | **DELETE** /webrobot/api/ai-providers/providers/{provider}/training/{jobId} | 
[**create_agent**](DefaultApi.md#create_agent) | **POST** /webrobot/api/agents | 
[**create_category**](DefaultApi.md#create_category) | **POST** /webrobot/api/categories | 
[**create_project**](DefaultApi.md#create_project) | **POST** /webrobot/api/projects | 
[**create_task**](DefaultApi.md#create_task) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks | 
[**delete**](DefaultApi.md#delete) | **DELETE** /api/strapi-tables/{table}/{id} | 
[**delete_agent**](DefaultApi.md#delete_agent) | **DELETE** /webrobot/api/agents/{agentId} | 
[**delete_category**](DefaultApi.md#delete_category) | **DELETE** /webrobot/api/categories/id/{categoryId} | 
[**delete_dataset**](DefaultApi.md#delete_dataset) | **DELETE** /webrobot/api/datasets/{projectId}/{botId}/{datasetId} | 
[**delete_dataset_version**](DefaultApi.md#delete_dataset_version) | **DELETE** /webrobot/api/datasets/version/id/{versionsetId} | 
[**delete_project**](DefaultApi.md#delete_project) | **DELETE** /webrobot/api/projects/id/{projectId} | 
[**delete_task**](DefaultApi.md#delete_task) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
[**download_model**](DefaultApi.md#download_model) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/download | 
[**estimate_cost**](DefaultApi.md#estimate_cost) | **POST** /webrobot/api/ai-providers/providers/{provider}/cost-estimate | 
[**find_all**](DefaultApi.md#find_all) | **GET** /api/strapi-tables/{table} | 
[**get_agent**](DefaultApi.md#get_agent) | **GET** /webrobot/api/agents/{categoryId}/{agentId} | 
[**get_agent_from_name**](DefaultApi.md#get_agent_from_name) | **GET** /webrobot/api/agents/{categoryId}/name/{agentName} | 
[**get_all_agents**](DefaultApi.md#get_all_agents) | **GET** /webrobot/api/agents/{categoryId} | 
[**get_all_categories**](DefaultApi.md#get_all_categories) | **GET** /webrobot/api/categories | 
[**get_all_dataset_versions**](DefaultApi.md#get_all_dataset_versions) | **GET** /webrobot/api/datasets/{projectId}/{botId}/versions | 
[**get_all_datasets**](DefaultApi.md#get_all_datasets) | **GET** /webrobot/api/datasets/datasets | 
[**get_all_projects**](DefaultApi.md#get_all_projects) | **GET** /webrobot/api/projects | 
[**get_all_tasks**](DefaultApi.md#get_all_tasks) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks | 
[**get_all_versionsets**](DefaultApi.md#get_all_versionsets) | **GET** /webrobot/api/datasets/{datasetId}/versions | 
[**get_by_id**](DefaultApi.md#get_by_id) | **GET** /api/strapi-tables/{table}/{id} | 
[**get_category**](DefaultApi.md#get_category) | **GET** /webrobot/api/categories/id/{categoryId} | 
[**get_category_from_name**](DefaultApi.md#get_category_from_name) | **GET** /webrobot/api/categories/{categoryName} | 
[**get_dataset**](DefaultApi.md#get_dataset) | **GET** /webrobot/api/datasets/{projectId}/{botId}/{datasetId} | 
[**get_dataset_input_file**](DefaultApi.md#get_dataset_input_file) | **GET** /webrobot/api/datasets/{projectId}/{botId}/{datasetId}/input/url | 
[**get_dataset_input_file_pagination**](DefaultApi.md#get_dataset_input_file_pagination) | **GET** /webrobot/api/datasets/{projectId}/{botId}/{datasetId}/input/{offset}/{limit} | 
[**get_dataset_input_file_size**](DefaultApi.md#get_dataset_input_file_size) | **GET** /webrobot/api/datasets/{datasetId}/input/size | 
[**get_dataset_status**](DefaultApi.md#get_dataset_status) | **GET** /webrobot/api/datasets/datasets/{datasetId}/status | 
[**get_dataset_version_input_file**](DefaultApi.md#get_dataset_version_input_file) | **GET** /webrobot/api/datasets/{categoryId}/{jobId}/{datasetId}/versions/{versionsetId}/input/url | 
[**get_dataset_version_input_file_pagination**](DefaultApi.md#get_dataset_version_input_file_pagination) | **GET** /webrobot/api/datasets/{datasetId}/versions/{versionsetId}/input/{offset}/{limit} | 
[**get_health**](DefaultApi.md#get_health) | **GET** /health | 
[**get_html**](DefaultApi.md#get_html) | **GET** /webrobot/api/html/{url}/{protocol} | 
[**get_project**](DefaultApi.md#get_project) | **GET** /webrobot/api/projects/id/{projectId} | 
[**get_project_from_name**](DefaultApi.md#get_project_from_name) | **GET** /webrobot/api/projects/{projectName} | 
[**get_project_jobs**](DefaultApi.md#get_project_jobs) | **GET** /webrobot/api/projects/id/{projectId}/jobs | 
[**get_project_schedule**](DefaultApi.md#get_project_schedule) | **GET** /webrobot/api/projects/id/{projectId}/schedule | 
[**get_supported_models**](DefaultApi.md#get_supported_models) | **GET** /webrobot/api/ai-providers/providers/{provider}/models | 
[**get_supported_providers**](DefaultApi.md#get_supported_providers) | **GET** /webrobot/api/ai-providers/providers | 
[**get_task**](DefaultApi.md#get_task) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
[**get_task_status**](DefaultApi.md#get_task_status) | **GET** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/status | 
[**get_training_logs**](DefaultApi.md#get_training_logs) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/logs | 
[**get_training_status**](DefaultApi.md#get_training_status) | **GET** /webrobot/api/ai-providers/providers/{provider}/training/{jobId}/status | 
[**get_upload_file_url**](DefaultApi.md#get_upload_file_url) | **GET** /webrobot/api/datasets/{categoryId}/{jobId}/upload/{attachmentName} | 
[**get_url_download**](DefaultApi.md#get_url_download) | **GET** /webrobot/api/package/download | 
[**get_url_upload**](DefaultApi.md#get_url_upload) | **GET** /webrobot/api/package/upload | 
[**get_versionset**](DefaultApi.md#get_versionset) | **GET** /webrobot/api/datasets/version/id/{versionsetId} | 
[**get_versionset_from_version**](DefaultApi.md#get_versionset_from_version) | **POST** /webrobot/api/datasets/{datasetId}/versions/version/{version} | 
[**get_versionset_from_version_base**](DefaultApi.md#get_versionset_from_version_base) | **GET** /webrobot/api/datasets/{datasetId}/versions/version/{version}/base | 
[**insert**](DefaultApi.md#insert) | **POST** /api/strapi-tables/{table} | 
[**publish_model**](DefaultApi.md#publish_model) | **POST** /webrobot/api/ai-providers/providers/huggingface/models/publish | 
[**remove_job_from_project**](DefaultApi.md#remove_job_from_project) | **DELETE** /webrobot/api/projects/id/{projectId}/jobs/{jobId} | 
[**set_project_schedule**](DefaultApi.md#set_project_schedule) | **PUT** /webrobot/api/projects/id/{projectId}/schedule | 
[**start_export_all**](DefaultApi.md#start_export_all) | **GET** /webrobot/api/package/export/all | 
[**start_export_project**](DefaultApi.md#start_export_project) | **GET** /webrobot/api/package/export/id/{projectId} | 
[**start_import_all**](DefaultApi.md#start_import_all) | **GET** /webrobot/api/package/import/all | 
[**start_import_project**](DefaultApi.md#start_import_project) | **GET** /webrobot/api/package/import/id/{projectId} | 
[**start_task**](DefaultApi.md#start_task) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/start | 
[**start_training**](DefaultApi.md#start_training) | **POST** /webrobot/api/ai-providers/providers/{provider}/training | 
[**stop_task**](DefaultApi.md#stop_task) | **POST** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId}/stop | 
[**test**](DefaultApi.md#test) | **GET** /webrobot/api/categories/test | 
[**test1**](DefaultApi.md#test1) | **GET** /webrobot/api/projects/test | 
[**update**](DefaultApi.md#update) | **PUT** /api/strapi-tables/{table}/{id} | 
[**update_agent**](DefaultApi.md#update_agent) | **PUT** /webrobot/api/agents/{categoryId}/{agentId} | 
[**update_category**](DefaultApi.md#update_category) | **PUT** /webrobot/api/categories/id/{categoryId} | 
[**update_project**](DefaultApi.md#update_project) | **PUT** /webrobot/api/projects/id/{projectId} | 
[**update_task**](DefaultApi.md#update_task) | **PUT** /webrobot/api/projects/id/{projectId}/jobs/{jobId}/tasks/{taskId} | 
[**upload_dataset**](DefaultApi.md#upload_dataset) | **POST** /webrobot/api/ai-providers/providers/{provider}/datasets | 
[**upload_dataset1**](DefaultApi.md#upload_dataset1) | **POST** /webrobot/api/datasets/{projectId}/{botId} | 


# **add_job_to_project**
> add_job_to_project(project_id, x_rapid_api_user=x_rapid_api_user, job_dto=job_dto)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    job_dto = webrobot.JobDto() # JobDto |  (optional)

    try:
        api_instance.add_job_to_project(project_id, x_rapid_api_user=x_rapid_api_user, job_dto=job_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->add_job_to_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **cancel_training**
> cancel_training(provider, job_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.cancel_training(provider, job_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_training: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **job_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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

# **create_agent**
> create_agent(x_rapid_api_user=x_rapid_api_user, agent_dto=agent_dto)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    agent_dto = webrobot.AgentDto() # AgentDto |  (optional)

    try:
        api_instance.create_agent(x_rapid_api_user=x_rapid_api_user, agent_dto=agent_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->create_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **create_category**
> create_category(x_rapid_api_user=x_rapid_api_user, job_category_dto=job_category_dto)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    job_category_dto = webrobot.JobCategoryDto() # JobCategoryDto |  (optional)

    try:
        api_instance.create_category(x_rapid_api_user=x_rapid_api_user, job_category_dto=job_category_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->create_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **create_project**
> create_project(x_rapid_api_user=x_rapid_api_user, job_project_dto=job_project_dto)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    job_project_dto = webrobot.JobProjectDto() # JobProjectDto |  (optional)

    try:
        api_instance.create_project(x_rapid_api_user=x_rapid_api_user, job_project_dto=job_project_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 
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
> create_task(project_id, job_id, x_rapid_api_user=x_rapid_api_user, task_dto=task_dto)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    task_dto = webrobot.TaskDto() # TaskDto |  (optional)

    try:
        api_instance.create_task(project_id, job_id, x_rapid_api_user=x_rapid_api_user, task_dto=task_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->create_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 
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
> delete_agent(agent_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.delete_agent(agent_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> delete_category(category_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.delete_category(category_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> delete_dataset(dataset_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.delete_dataset(dataset_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> delete_dataset_version(versionset_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.delete_dataset_version(versionset_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_dataset_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionset_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> delete_project(project_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.delete_project(project_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> delete_task(project_id, job_id, task_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.delete_task(project_id, job_id, task_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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

# **download_model**
> download_model(provider, job_id, x_rapid_api_user=x_rapid_api_user, output_path=output_path)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    output_path = 'output_path_example' # str |  (optional)

    try:
        api_instance.download_model(provider, job_id, x_rapid_api_user=x_rapid_api_user, output_path=output_path)
    except Exception as e:
        print("Exception when calling DefaultApi->download_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **job_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **estimate_cost**
> estimate_cost(provider, x_rapid_api_user=x_rapid_api_user, training_request_bean=training_request_bean)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    training_request_bean = webrobot.TrainingRequestBean() # TrainingRequestBean |  (optional)

    try:
        api_instance.estimate_cost(provider, x_rapid_api_user=x_rapid_api_user, training_request_bean=training_request_bean)
    except Exception as e:
        print("Exception when calling DefaultApi->estimate_cost: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **get_agent**
> get_agent(category_id, agent_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_agent(category_id, agent_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **agent_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_agent_from_name(category_id, agent_name, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_agent_from_name(category_id, agent_name, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_agent_from_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **agent_name** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_all_agents(category_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_all_agents(category_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_all_categories(x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_all_categories(x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_all_dataset_versions(x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_all_dataset_versions(x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_dataset_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_all_datasets(x_rapid_api_user=x_rapid_api_user, status=status)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        api_instance.get_all_datasets(x_rapid_api_user=x_rapid_api_user, status=status)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **get_all_projects**
> get_all_projects(x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_all_projects(x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_all_tasks(project_id, job_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_all_tasks(project_id, job_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_all_versionsets(dataset_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_all_versionsets(dataset_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_versionsets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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

# **get_category**
> get_category(category_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_category(category_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_category_from_name(category_name, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_category_from_name(category_name, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_category_from_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_name** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_dataset(dataset_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_dataset(dataset_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_dataset_input_file(dataset_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_dataset_input_file(dataset_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset_input_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_dataset_input_file_pagination(offset, dataset_id, limit, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_dataset_input_file_pagination(offset, dataset_id, limit, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset_input_file_pagination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | 
 **dataset_id** | **str**|  | 
 **limit** | **int**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_dataset_input_file_size(dataset_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_dataset_input_file_size(dataset_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset_input_file_size: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_dataset_status(dataset_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_dataset_status(dataset_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_dataset_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_dataset_version_input_file(category_id, job_id, versionset_id, dataset_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_dataset_version_input_file(category_id, job_id, versionset_id, dataset_id, x_rapid_api_user=x_rapid_api_user)
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
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_dataset_version_input_file_pagination(project_id, bot_id, offset, limit, versionset_id, dataset_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_dataset_version_input_file_pagination(project_id, bot_id, offset, limit, versionset_id, dataset_id, x_rapid_api_user=x_rapid_api_user)
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
 **x_rapid_api_user** | **str**|  | [optional] 

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

# **get_project**
> get_project(project_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_project(project_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_project_from_name(project_name, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_project_from_name(project_name, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_from_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_project_jobs(project_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_project_jobs(project_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_project_schedule(project_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_project_schedule(project_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_supported_models(provider, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_supported_models(provider, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_supported_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_supported_providers(x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_supported_providers(x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_supported_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_task(project_id, job_id, task_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_task(project_id, job_id, task_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_task_status(project_id, job_id, task_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_task_status(project_id, job_id, task_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_task_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_training_logs(provider, job_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_training_logs(provider, job_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_training_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **job_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_training_status(provider, job_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_training_status(provider, job_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_training_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **job_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_upload_file_url(project_id, bot_id, attachment_name, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_upload_file_url(project_id, bot_id, attachment_name, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_upload_file_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **bot_id** | **str**|  | 
 **attachment_name** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_url_download(x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_url_download(x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_url_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_url_upload(x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_url_upload(x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_url_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_versionset(versionset_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_versionset(versionset_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_versionset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionset_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> get_versionset_from_version(dataset_id, version, x_rapid_api_user=x_rapid_api_user, time_period=time_period)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    time_period = webrobot.TimePeriod() # TimePeriod |  (optional)

    try:
        api_instance.get_versionset_from_version(dataset_id, version, x_rapid_api_user=x_rapid_api_user, time_period=time_period)
    except Exception as e:
        print("Exception when calling DefaultApi->get_versionset_from_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **version** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 
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
> get_versionset_from_version_base(dataset_id, version, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.get_versionset_from_version_base(dataset_id, version, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->get_versionset_from_version_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **version** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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

# **publish_model**
> publish_model(x_rapid_api_user=x_rapid_api_user, model_publish_request=model_publish_request)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    model_publish_request = webrobot.ModelPublishRequest() # ModelPublishRequest |  (optional)

    try:
        api_instance.publish_model(x_rapid_api_user=x_rapid_api_user, model_publish_request=model_publish_request)
    except Exception as e:
        print("Exception when calling DefaultApi->publish_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **remove_job_from_project**
> remove_job_from_project(project_id, job_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.remove_job_from_project(project_id, job_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->remove_job_from_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> set_project_schedule(project_id, x_rapid_api_user=x_rapid_api_user, project_schedule_request=project_schedule_request)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    project_schedule_request = webrobot.ProjectScheduleRequest() # ProjectScheduleRequest |  (optional)

    try:
        api_instance.set_project_schedule(project_id, x_rapid_api_user=x_rapid_api_user, project_schedule_request=project_schedule_request)
    except Exception as e:
        print("Exception when calling DefaultApi->set_project_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **start_export_all**
> start_export_all(x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.start_export_all(x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->start_export_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 

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

# **start_export_project**
> start_export_project(project_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.start_export_project(project_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->start_export_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> start_import_all(x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.start_import_all(x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->start_import_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 

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

# **start_import_project**
> start_import_project(project_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.start_import_project(project_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->start_import_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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

# **start_task**
> start_task(project_id, job_id, task_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.start_task(project_id, job_id, task_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->start_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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
> start_training(provider, x_rapid_api_user=x_rapid_api_user, training_request_bean=training_request_bean)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    training_request_bean = webrobot.TrainingRequestBean() # TrainingRequestBean |  (optional)

    try:
        api_instance.start_training(provider, x_rapid_api_user=x_rapid_api_user, training_request_bean=training_request_bean)
    except Exception as e:
        print("Exception when calling DefaultApi->start_training: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **stop_task**
> stop_task(project_id, job_id, task_id, x_rapid_api_user=x_rapid_api_user)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)

    try:
        api_instance.stop_task(project_id, job_id, task_id, x_rapid_api_user=x_rapid_api_user)
    except Exception as e:
        print("Exception when calling DefaultApi->stop_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 

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

# **update_agent**
> update_agent(category_id, agent_id, x_rapid_api_user=x_rapid_api_user, agent_dto=agent_dto)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    agent_dto = webrobot.AgentDto() # AgentDto |  (optional)

    try:
        api_instance.update_agent(category_id, agent_id, x_rapid_api_user=x_rapid_api_user, agent_dto=agent_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->update_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **agent_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **update_category**
> update_category(category_id, x_rapid_api_user=x_rapid_api_user, job_category_dto=job_category_dto)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    job_category_dto = webrobot.JobCategoryDto() # JobCategoryDto |  (optional)

    try:
        api_instance.update_category(category_id, x_rapid_api_user=x_rapid_api_user, job_category_dto=job_category_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->update_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **update_project**
> update_project(project_id, x_rapid_api_user=x_rapid_api_user, job_project_dto=job_project_dto)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    job_project_dto = webrobot.JobProjectDto() # JobProjectDto |  (optional)

    try:
        api_instance.update_project(project_id, x_rapid_api_user=x_rapid_api_user, job_project_dto=job_project_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **update_task**
> update_task(project_id, job_id, task_id, x_rapid_api_user=x_rapid_api_user, task_dto=task_dto)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    task_dto = webrobot.TaskDto() # TaskDto |  (optional)

    try:
        api_instance.update_task(project_id, job_id, task_id, x_rapid_api_user=x_rapid_api_user, task_dto=task_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->update_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **job_id** | **str**|  | 
 **task_id** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **upload_dataset**
> upload_dataset(provider, x_rapid_api_user=x_rapid_api_user, dataset_upload_request=dataset_upload_request)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    dataset_upload_request = webrobot.DatasetUploadRequest() # DatasetUploadRequest |  (optional)

    try:
        api_instance.upload_dataset(provider, x_rapid_api_user=x_rapid_api_user, dataset_upload_request=dataset_upload_request)
    except Exception as e:
        print("Exception when calling DefaultApi->upload_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **x_rapid_api_user** | **str**|  | [optional] 
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

# **upload_dataset1**
> upload_dataset1(x_rapid_api_user=x_rapid_api_user, dataset_upload_api_dto=dataset_upload_api_dto)

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
    x_rapid_api_user = 'x_rapid_api_user_example' # str |  (optional)
    dataset_upload_api_dto = webrobot.DatasetUploadApiDto() # DatasetUploadApiDto |  (optional)

    try:
        api_instance.upload_dataset1(x_rapid_api_user=x_rapid_api_user, dataset_upload_api_dto=dataset_upload_api_dto)
    except Exception as e:
        print("Exception when calling DefaultApi->upload_dataset1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_rapid_api_user** | **str**|  | [optional] 
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

