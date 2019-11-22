"""Web application."""
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from . import splines


app = Starlette()


@app.route("/")
async def index(request):
    count = int(request.query_params.get("count", 1))
    return JSONResponse(
        {"splines": [{"id": spline} async for spline in splines.reticulate(count)]}
    )
