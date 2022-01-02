from fastapi import FastAPI, Request

from api.version1 import route_users
from api.version1 import route_login 
from api.version1 import route_locations 
from api.version1 import route_items 
from core.config import settings

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    return app

app = start_application()

app.include_router(route_users.router, prefix="/users", tags=["users"])
app.include_router(route_login.router, prefix="/login", tags=["login"])
app.include_router(route_locations.router, prefix="/locations", tags=["locations"])
app.include_router(route_items.router, prefix="/locations/{location_id}/items", tags=["items"])

@app.get("/")
async def root(request: Request):
    return {"message": f"Welcome to the Stuff API! Track your stuff here. Checkout {request.base_url}docs for more information.", "base_url": f"{request.base_url}", "docs_url": f"{request.base_url}docs"}

