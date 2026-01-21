from fastapi import FastAPI
from .api.company_intelligence import router

app = FastAPI(title="Company Interligence Service")

app.include_router(router)
 