from starlette import status

from text_storage.app import app


@app.post("/api/{text}/store")
def store_text(text, status_code=status.HTTP_201_CREATED):
    return text
