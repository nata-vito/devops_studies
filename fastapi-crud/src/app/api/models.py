from pydantic import BaseModel, Field

class NoteSchema(BaseModel):
    title: str
    description: str
    
class NoteDB(NoteSchema):
    id: int
    
class NoteSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)