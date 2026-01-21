from fastapi import FastAPI
from .api.company_partnership_routes import router

app = FastAPI(title="Company Indygx-Assessment Service")

app.include_router(router)
 