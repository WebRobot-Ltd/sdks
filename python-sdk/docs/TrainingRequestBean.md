# TrainingRequestBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] 
**training_file** | **str** |  | [optional] 
**validation_file** | **str** |  | [optional] 
**dataset_id** | **str** |  | [optional] 
**hyperparameters** | **Dict[str, object]** |  | [optional] 

## Example

```python
from webrobot.models.training_request_bean import TrainingRequestBean

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingRequestBean from a JSON string
training_request_bean_instance = TrainingRequestBean.from_json(json)
# print the JSON string representation of the object
print(TrainingRequestBean.to_json())

# convert the object into a dict
training_request_bean_dict = training_request_bean_instance.to_dict()
# create an instance of TrainingRequestBean from a dict
training_request_bean_from_dict = TrainingRequestBean.from_dict(training_request_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


