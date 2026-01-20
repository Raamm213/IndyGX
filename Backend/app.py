from sqlmodel import select, Session
from .database import engine
from .models import CompanyPrimary
from .repository.company_repository import CompanyRepository
from .api.company_secondary_routes import router as company_secondary_router
from .api.competitive_intelligence_routes import router as competitive_intelligence_router
from .api.contact_information_routes import router as contact_information_router
from .api.digital_presence_brand_routes import router as digital_presence_brand_router
from .api.financials_funding_routes import router as financials_funding_router
from .api.indygx_assessment_routes import router as indygx_assessment_router
from .api.partnerships_ecosystem_routes import router as partnerships_ecosystem_router
from .api.comapnay_full_profile import router as company_full_profile


from fastapi import FastAPI



app = FastAPI()

app.include_router(company_full_profile,prefix="/company-full-profile",tags=['company-full-profile'])
app.include_router(company_secondary_router, prefix="/company-secondary", tags=["company-secondary"])
app.include_router(competitive_intelligence_router, prefix="/competitive-intelligence", tags=["competitive-intelligence"])
app.include_router(contact_information_router, prefix="/contact-information", tags=["contact-information"])
app.include_router(digital_presence_brand_router, prefix="/digital-presence-brand", tags=["digital-presence-brand"])
app.include_router(financials_funding_router, prefix="/financials-funding", tags=["financials-funding"])
app.include_router(indygx_assessment_router, prefix="/indygx-assessment", tags=["indygx-assessment"])
app.include_router(partnerships_ecosystem_router, prefix="/partnerships-ecosystem", tags=["partnerships-ecosystem"])



def fetch_all_companies():
    with Session(engine) as session:
        try:
            statement = select(CompanyPrimary.company_id, CompanyPrimary.company_name)
            results = session.exec(statement).all()
            return results
        except Exception as e:
            print(f"An error occurred while fetching companies: {e}")
            return []
        finally:
            print("Database session closed.")

if __name__ == "__main__":
    companies = CompanyRepository.list_companies()
    print("Companies:")
    for c in companies:
        print(c)
 