from pathlib import Path

import yaml
from fastapi import FastAPI

app: FastAPI = FastAPI(
    debug=True, openapi_url="/openapi/textdrop.json", docs_url="/docs/textdrop"
)

oas_doc = yaml.safe_load((Path(__file__).parent / "../oas.yaml").read_text())
app.openapi = lambda: oas_doc

from text_storage.api import api  # noqa: F401, E402
