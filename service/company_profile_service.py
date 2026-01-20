from database import get_session
from repository import (
    company_repository,
    company_secondary_repo,
    competitive_intelligence_repo,
)

class CompanyProfileService:

    @staticmethod
    def upsert_full_profile(company_id: int, payload: dict):
        with get_session() as session:
            try:
                company_repository.upsert(
                    company_id, payload["primary"], session
                )

                company_secondary_repo.upsert(
                    company_id, payload.get("secondary", {}), session
                )

                competitive_intelligence_repo.upsert(
                    company_id, payload.get("competitive_intelligence", {}),
                    session
                )

                session.commit()
            except:
                session.rollback()
                raise
