from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['bms-kb']
collection = db['syllabus-data']

course_title = ""
course_code = ""
course_credits = ""
course_department = ""
course_u1_topics = ""
course_u2_topics = ""
course_u3_topics = ""
course_u4_topics = ""
course_u5_topics = ""

class Course:
    def __init__(self, title: str, code: str, ) -> None:
        """A BMS Course is taught by a faculty in one semester. It has a course code, title, credits, department, syllabus, and course objectives."""
        pass