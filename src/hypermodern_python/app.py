"""Web application."""
from starlette.applications import Starlette
from starlette.responses import StreamingResponse
from starlette.routing import Route

from . import splines


app = Starlette()


@app.route("/")
async def index(request):
    count = int(request.query_params.get("count", 1))

    async def content():
        async for spline in splines.reticulate(count):
            yield f"Reticulating spline {spline}...\n"

    return StreamingResponse(
        content(),
        media_type="text/plain",
        headers={"X-Content-Type-Options": "nosniff"},
    )
