# file to initialize the vector store and insert all data into the store.
from pymilvus import Collection, FieldSchema, CollectionSchema, DataType

def create_event_collection():
    event_id = FieldSchema(
        name="event_id",
        dtype=DataType.VARCHAR,
        is_primary=True,
        max_length=200,
    )
    event_title = FieldSchema(
        name="event_title",
        dtype=DataType.VARCHAR,
        max_length=200,
    )
    # event start date is the date when the event starts
    event_start_date = FieldSchema(
        name="event_start_date",
        dtype=DataType.VARCHAR,
        max_length=16,
    )
    event_end_date = FieldSchema(
        name="event_end_date",
        dtype=DataType.VARCHAR,
        max_length=16,
    )
    # event template is a large paragraph containing the event details
    event_template = FieldSchema(
        name="event_template",
        dtype=DataType.VARCHAR,
        max_length=20000,
    )
    # event vector is the vector representation of the event template
    event_vector = FieldSchema(
        name="event_vector",
        dtype=DataType.FLOAT_VECTOR,
        dim=768,
    )
    schema = CollectionSchema(
        fields=[event_id, event_title, event_template, event_vector],
        description="Events of BMSCE"
    )
    return schema

def create_document_collection():
    document_name = FieldSchema(
        name="document_name",
        dtype=DataType.VARCHAR,
        is_primary=True,
        max_length=200,
    )
    document_type = FieldSchema(
        name="document_type",
        dtype=DataType.VARCHAR,
        max_length=200,
    )
    document_authors = FieldSchema(
        name="document_authors",
        dtype=DataType.ARRAY,
        max_length=200,
    )
    document_content = FieldSchema(
        name="document_content",
        dtype=DataType.VARCHAR,
        max_length=20000,
    )
    document_course = FieldSchema(
        name="document_course",
        dtype=DataType.VARCHAR,
        max_length=200,
    )
    document_date_created = FieldSchema(
        name="document_date_created",
        dtype=DataType.VARCHAR,
        max_length=16,
    )
    return

def create_course_collection():
    return

def create_faculty_collection():
    return  
