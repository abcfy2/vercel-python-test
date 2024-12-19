from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from .agent import get_answers

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")


@app.get("/api", response_class=PlainTextResponse)
async def index():
    markdown = await get_answers()
    return markdown
