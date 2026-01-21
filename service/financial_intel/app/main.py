from fastapi import FastAPI
from .api.company_financial_route import router

app = FastAPI(title="Company Financial Service")

app.include_router(router)
 