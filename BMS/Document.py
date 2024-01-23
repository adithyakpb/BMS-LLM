
class Document:
    def __init__(self, name):
        """A BMS Document can be one of the following:
        1. Circular
        2. Syllabus
        3. Textbook
        4. Question Paper
        5. Notes
        6. Assignment
        7. Reports
        This class contains all methods to define and manipulate a document."""
        self.name = name