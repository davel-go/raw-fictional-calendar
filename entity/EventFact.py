class EventFact:
    def __init__(self, id, story_arc, location_1, location_2, location_3, type, description, day, month, year):
        self.id = id
        self.story_arc = story_arc
        self.location_1 = location_1
        self.location_2 = location_2
        self.location_3 = location_3
        self.type = type
        self.description = description
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return (f"ID: {self.id}     --  Type: {self.type}\n"
                f"Story arc: {self.story_arc}   --  Description: {self.description}\n"
                f"Date: [ {self.day}-{self.month}-{self.year} ]")
