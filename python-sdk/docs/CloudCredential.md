# CloudCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**api_secret** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**access_key_id** | **str** |  | [optional] 
**secret_access_key** | **str** |  | [optional] 
**session_token** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**resource_group** | **str** |  | [optional] 
**workspace_name** | **str** |  | [optional] 
**hugging_face_token** | **str** |  | [optional] 
**cohere_api_key** | **str** |  | [optional] 
**azure_ai_studio_endpoint** | **str** |  | [optional] 
**mosaicml_api_key** | **str** |  | [optional] 
**replicate_api_token** | **str** |  | [optional] 
**twitter_bearer_token** | **str** |  | [optional] 
**twitter_api_key** | **str** |  | [optional] 
**twitter_api_secret** | **str** |  | [optional] 
**reddit_client_id** | **str** |  | [optional] 
**reddit_client_secret** | **str** |  | [optional] 
**reddit_user_agent** | **str** |  | [optional] 
**facebook_access_token** | **str** |  | [optional] 
**facebook_app_id** | **str** |  | [optional] 
**facebook_app_secret** | **str** |  | [optional] 
**instagram_access_token** | **str** |  | [optional] 
**linkedin_access_token** | **str** |  | [optional] 
**linkedin_client_id** | **str** |  | [optional] 
**linkedin_client_secret** | **str** |  | [optional] 
**tiktok_client_key** | **str** |  | [optional] 
**tiktok_client_secret** | **str** |  | [optional] 
**youtube_api_key** | **str** |  | [optional] 
**databricks_workspace_url** | **str** |  | [optional] 
**databricks_access_token** | **str** |  | [optional] 
**databricks_cluster_id** | **str** |  | [optional] 
**oauth_access_token** | **str** |  | [optional] 
**oauth_refresh_token** | **str** |  | [optional] 
**oauth_token_expires_at** | **datetime** |  | [optional] 
**oauth_token_type** | **str** |  | [optional] 
**alphavantage_api_key** | **str** |  | [optional] 
**polygon_api_key** | **str** |  | [optional] 
**twelvedata_api_key** | **str** |  | [optional] 
**marketstack_access_key** | **str** |  | [optional] 
**fmp_api_key** | **str** |  | [optional] 
**iexcloud_token** | **str** |  | [optional] 
**cbond_api_key** | **str** |  | [optional] 
**cbond_client_id** | **str** |  | [optional] 
**cbond_client_secret** | **str** |  | [optional] 
**google_search_engine_id** | **str** |  | [optional] 
**bing_search_api_key** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from webrobot.models.cloud_credential import CloudCredential

# TODO update the JSON string below
json = "{}"
# create an instance of CloudCredential from a JSON string
cloud_credential_instance = CloudCredential.from_json(json)
# print the JSON string representation of the object
print(CloudCredential.to_json())

# convert the object into a dict
cloud_credential_dict = cloud_credential_instance.to_dict()
# create an instance of CloudCredential from a dict
cloud_credential_from_dict = CloudCredential.from_dict(cloud_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


