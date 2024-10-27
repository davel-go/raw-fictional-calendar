from entity.EventPreload import EventPreload
from utils.date_operations import *


def event_preload_calculation(ep_list: dict):
    for k in ep_list:
        calculate_dates(ep_list, k)
    return True


def calculate_dates(ep_list: dict, event_id: int = 1):
    event: EventPreload = ep_list.get(event_id)
    if event.is_event:
        return True
    else:
        anchor_event: EventPreload = ep_list.get(event.anchor_event)
        if anchor_event.is_event is True:
            event.get_anchor_date_list()
            date_to_add = event.get_anchor_date_list()
            data = date_operation(anchor_event.get_date_list(), date_to_add, event.before)
            event.day = data[0]
            event.month = data[1]
            event.year = data[2]
            event.is_event = True
            return True
        else:
            return calculate_dates(ep_list, anchor_event.id)
