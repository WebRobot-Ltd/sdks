# PluginInstallation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**plugin_id** | **str** |  | [optional] 
**plugin_type** | **str** |  | [optional] 
**build_type** | **str** |  | [optional] 
**build_number** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**jar_path** | **str** |  | [optional] 
**manifest_path** | **str** |  | [optional] 
**ui_zip_path** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**organization_ids_json** | **str** |  | [optional] 
**main_class** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**installed_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**enabled_at** | **datetime** |  | [optional] 
**enabled_by** | **str** |  | [optional] 
**installed_by** | **str** |  | [optional] 

## Example

```python
from webrobot.models.plugin_installation import PluginInstallation

# TODO update the JSON string below
json = "{}"
# create an instance of PluginInstallation from a JSON string
plugin_installation_instance = PluginInstallation.from_json(json)
# print the JSON string representation of the object
print(PluginInstallation.to_json())

# convert the object into a dict
plugin_installation_dict = plugin_installation_instance.to_dict()
# create an instance of PluginInstallation from a dict
plugin_installation_from_dict = PluginInstallation.from_dict(plugin_installation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


