import datetime
from pymongo import MongoClient
from databases.KnowledgeBase import KnowledgeBase
import hashlib
class Event(KnowledgeBase):
    """
        title: title of the event
        start_dt: start date and time of the event. Follow the format: DD-MM-YYYY HH:MM (24 hour format)"
        end_dt: end date and time of the event. Follow the format: DD-MM-YYYY HH:MM (24 hour format)
        venue: venue of the event
        org: organizers of the event
        fee: registration fee of the event, can be a list of fees for different categories
        link: link to the event's website
        contact: contact details of the organizers, can be Phone number, email, etc.
        description: description of the event
    """
    #constructor
    def __init__(self, title: str, start_dt: str, end_dt: str, venue: str | None, org: str, fee: int | list, link: str | None, contact: str | None, description: str | None) -> None:
        super().__init__("events-calendar")
        try:
            start_dt = datetime.datetime.strptime(start_dt, "%d-%m-%Y %H:%M")
            end_dt = datetime.datetime.strptime(end_dt, "%d-%m-%Y %H:%M")
        except ValueError:
            print("Please follow the format: DD-MM-YYYY HH:MM (24 hour format)")
            return
        self.set_event_id
        self.set_title(title)
        self.set_start_datetime(start_dt)
        self.set_end_datetime(end_dt)
        self.set_venue(venue)
        self.set_organizers(org)
        self.set_fee(fee)
        self.set_link(link)
        self.set_contact(contact)
        self.set_description(description)

        self.event_template = f"The event named {self.title} is scheduled to be held from {self.start_datetime} to {self.end_datetime} at {self.venue}. The event is organized by {self.organizers} and the registration fee is {self.fee}. For more details, visit {self.link} or contact {self.contact}. The description of the event is as follows: {self.description}."

    def __str__(self) -> str:
        return self.event_template
    
    # def __repr__(self) -> str:
    #     return "Event(title={}, start_datetime={}, end_datetime={}, venue={}, organizers={}, fee={}, link={}, contact={}, description={})".format(self._event_title, self._event_start_datetime, self._event_end_datetime, self._event_venue, self._event_organizers, self._event_fee, self._event_link, self._event_contact, self._event_description)
    def to_vector(self) -> list:
        """Convert the event object to a vector to be inserted to a vectorstore."""
        from langchain_community.embeddings import HuggingFaceEmbeddings
        #embed the event template
        embedding = HuggingFaceEmbeddings()
        return embedding.embed_documents([self.event_template])
    @staticmethod
    def from_db(filter: dict):
        """given a filter, query mongodb and return an event object"""
        #query the database
        a = KnowledgeBase("events-calendar")
        result = a.find(filter)
        #return a list of events
        return Event(result["Title"], result["Start DateTime"], result["End DateTime"], result["Venue"], result["Organizers"], result["Registration Fee"], result["Link"], result["Contact"], result["Description"])
    def __dict__(self) -> dict:
        return {
            "event_title": self._event_title,
            "event_start_datetime": self._event_start_datetime,
            "event_end_datetime": self._event_end_datetime,
            "event_venue": self._event_venue,
            "event_organizers": self._event_organizers,
            "event_fee": self._event_fee,
            "event_link": self._event_link,
            "event_contact": self._event_contact,
            "event_description": self._event_description
        }
    @property
    def title(self):
        return self._event_title
    @property
    def start_datetime(self):
        return self._event_start_datetime
    @property
    def end_datetime(self):
        return self._event_end_datetime
    @property
    def venue(self):
        return self._event_venue
    @property
    def organizers(self):
        return self._event_organizers
    @property
    def fee(self):
        return self._event_fee
    @property
    def link(self):
        return self._event_link
    @property
    def contact(self):
        return self._event_contact
    @property
    def description(self):
        return self._event_description
    
    def insert_to_db(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['bms-kb']
        collection = db['events-calendar']
        collection.insert_one(self.__dict__)
        
    # def __eq__(self, o: object) -> bool:
    #     return self.event_template == o.event_template
    
    # def __hash__(self) -> int:
    #     return

