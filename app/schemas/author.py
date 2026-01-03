from pydantic import BaseModel, ConfigDict

class AuthorBase(BaseModel):
    name : str
    bio : str | None = None

class AuthorCreate(AuthorBase):
    """ Schema for create Author """
    pass

class AuthorUpdate(AuthorBase):
    """ Schema for update Author """
    name : str | None = None
    bio : str | None = None

class AuthorInDBBase(AuthorBase):
    id : int

    model_config = ConfigDict(from_attributes=True)

class Author(AuthorInDBBase):
    """Schema return for client"""
    pass