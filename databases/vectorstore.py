import lancedb
#vectorstore functions
class Vectorstore():
    """A class to interact with the vectorstore."""
    def __init__(self,) -> None:
        """Initialize the vectorstore object."""
        
        uri = "data/sample-lancedb"
        db = lancedb.connect(uri)
        
        
        self.name = name