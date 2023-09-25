from bson import ObjectId
from pydantic.json import pydantic_encoder

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, model):
        return {"type": "string", "format": "objectid"}

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self)

    def __json_encode__(self):
        return str(self)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string", format="objectid")
