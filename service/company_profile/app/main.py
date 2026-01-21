from fastapi import FastAPI
from .api.company_routes import router

app = FastAPI(title="Company Profile Service")

app.include_router(router)
 