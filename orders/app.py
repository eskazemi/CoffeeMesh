from fastapi import FastAPI
from pathlib import Path
import yaml

oas_doc = yaml.safe_load(
    (Path(__file__).parent / '../oas.yaml').read_text()
)

app = FastAPI(debug=True, openapi_url='/openapi/orders.json', docs_url='/docs/orders')

# We override FastAPI’s openapi property so that it returns our API specification.
app.openapi = lambda: oas_doc



from orders.api import api
