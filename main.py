from database.conn import CONN
from database.init import initialize_events_table
from database.queries import get_events_as_kvm
from utils.event_operations import event_preload_calculation
from database.facts import generate_event_facts

initialize_events_table(CONN)
ep_list = get_events_as_kvm(CONN)
event_preload_calculation(ep_list)

final_list = [e.to_event() for k, e in ep_list.items()]

events_sorted = sorted(final_list, key=lambda event: (event.year, event.month, event.day))
generate_event_facts(CONN, events_sorted)
