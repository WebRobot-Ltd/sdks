# RescheduleEventsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_urls** | **List[str]** |  | [optional] 

## Example

```python
from webrobot.models.reschedule_events_request import RescheduleEventsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RescheduleEventsRequest from a JSON string
reschedule_events_request_instance = RescheduleEventsRequest.from_json(json)
# print the JSON string representation of the object
print(RescheduleEventsRequest.to_json())

# convert the object into a dict
reschedule_events_request_dict = reschedule_events_request_instance.to_dict()
# create an instance of RescheduleEventsRequest from a dict
reschedule_events_request_from_dict = RescheduleEventsRequest.from_dict(reschedule_events_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


