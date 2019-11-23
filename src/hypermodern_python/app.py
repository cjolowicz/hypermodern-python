"""Web application."""
from typing import AsyncIterator

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse

from . import splines


app = Starlette()


@app.route("/")
async def index(request: Request) -> Response:
    """Main endpoint."""
    count = int(request.query_params.get("count", 1))

    async def content() -> AsyncIterator[str]:
        async for spline in splines.reticulate(count):
            yield f"Reticulating spline {spline}...\n"

    return StreamingResponse(
        content(),
        media_type="text/plain",
        headers={"X-Content-Type-Options": "nosniff"},
    )
