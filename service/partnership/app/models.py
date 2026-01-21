from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class PartnershipsEcosystem(SQLModel, table=True):
    __tablename__ = "partnerships_ecosystem"

    company_id: int = Field(primary_key=True, foreign_key="company_primary.company_id")
    corporate_partnership_programs: str | None
    university_academic_partnerships: str | None
    industry_associations_memberships: str | None
    strategic_partnerships: str | None
    rd_investment_percentage: str | None
    technology_partners: str | None
