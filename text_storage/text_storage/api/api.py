import uuid
from datetime import datetime

from starlette import status

from text_storage.api.schemas import TextFragmentResponseSchema, TextFragmentSchema
from text_storage.app import app


@app.post(
    "/text/store",
    status_code=status.HTTP_201_CREATED,
    response_model=TextFragmentResponseSchema,
)
def store_text(text_detail: TextFragmentSchema):
    text = text_detail.dict()
    text["id"] = uuid.uuid4()
    text["created_at"] = datetime.utcnow()
    return text
