import datetime
from pymongo import MongoClient
from databases.knowledgebase import KnowledgeBase
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
    def __init__(self, title: str, start_dt: str, end_dt: str, venue: str | None, organizers: str, fee: int | list, link: str | None, contact: str | None, description: str | None) -> None:
        super().__init__("events-calendar")
        try:
            start_dt = datetime.datetime.strptime(start_dt, "%d-%m-%Y %H:%M")
            end_dt = datetime.datetime.strptime(end_dt, "%d-%m-%Y %H:%M")
        except ValueError:
            print("Please follow the format: DD-MM-YYYY HH:MM (24 hour format)")
            return
        self.title = title
        self.start_datetime = start_dt
        self.end_datetime = end_dt
        self.venue = venue
        self.organizers = organizers
        self.fee = fee
        self.link = link
        self.contact = contact
        self.description = description

        
    def __str__(self) -> str:
        return self.event_template
    
    def __repr__(self) -> str:
        return self.event_template
    
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
            "Title": self.title,
            "Start DateTime": self.start_datetime,
            "End DateTime": self.end_datetime,
            "Venue": self.venue,
            "Organizers": self.organizers,
            "Registration Fee": self.fee,
            "Link": self.link,
            "Contact": self.contact,
            "Description": self.description
        }

    @property
    def event_template(self):
        self.event_template = f"The event named {self.title} is scheduled to be held from {self.start_datetime} to {self.end_datetime} at {self.venue}. The event is organized by {self.organizers} and the registration fee is {self.fee}. For more details, visit {self.link} or contact {self.contact}. The description of the event is as follows: {self.description}."
        return self.event_template

    @property
    def event_id(self):
        self.event_id = hashlib.md5(self.event_template.encode()).hexdigest()
        return self.event_id
    def insert_to_db(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['bms-kb']
        collection = db['events-calendar']
        collection.insert_one(self.__dict__)


