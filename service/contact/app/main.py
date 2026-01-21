from fastapi import FastAPI
from .api.company_contact import router

app = FastAPI(title="Company contact Service")

app.include_router(router)
 