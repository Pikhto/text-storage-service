from fastapi import FastAPI

app: FastAPI = FastAPI(debug=True)

from text_storage.api import api  # noqa: F401, E402
