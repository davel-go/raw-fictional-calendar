from entity.EventFact import EventFact

class EventPreload:
    def __init__(self, id, story_arc, character, location_1, location_2, location_3, type, description, day, month, year, anchor_event, before, a_day, a_month,
                 a_year):
        self.id = id
        self.story_arc = story_arc
        self.character = character
        self.location_1 = location_1
        self.location_2 = location_2
        self.location_3 = location_3
        self.type = type
        self.description = description
        self.day = day
        self.month = month
        self.year = year
        self.anchor_event = anchor_event
        self.before = before
        self.a_day = a_day
        self.a_month = a_month
        self.a_year = a_year
        self.is_event = self.anchor_event is None or self.anchor_event is ''

    def get_str_location(self):
        return f"{self.location_1} > {self.location_2} > {self.location_3}"

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Story arc: {self.story_arc}\n"
                f"Character: {self.character}\n"
                f"Event location: {self.get_str_location()}\n"
                f"Description: {self.description}\n"
                f"Date: {self.day}-{self.month}-{self.year}\n"
                f"Anchor Event ID: {self.anchor_event}\n"
                f"Before: {self.before}\n"
                f"Anchor Date: {self.a_day}-{self.a_month}-{self.a_year}")

    def get_anchor_date_list(self):
        return [self.a_day, self.a_month, self.a_year]

    def get_date_list(self):
        return [self.day, self.month, self.year]

    def to_event(self):
        return EventFact(self.id, self.story_arc, self.character, self.location_1, self.location_2, self.location_3, self.type, self.description, self.day, self.month, self.year)

