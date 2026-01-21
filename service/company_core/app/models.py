from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class CompanyPrimary(SQLModel, table=True):
    __tablename__ = "company_primary"

    company_id: int = Field(primary_key=True)
    company_name: Optional[str] = None
    year_of_incorporation: Optional[str] = None
    industry_segment: Optional[str] = None
    nature_of_company: str
    website_url: Optional[str] = None
    linkedin_profile_url: Optional[str] = None
    ceo_name: Optional[str] = None
    ceo_linkedin_url: Optional[str] = None
    employee_size: Optional[str] = None
    services_offerings: Optional[str] = None
    core_value_proposition: Optional[str] = None
    focus_sectors_industries: Optional[str] = None
    countries_operating_in: Optional[str] = None
    geographic_coverage_india: Optional[str] = None

    # secondary: Optional["CompanySecondary"] = Relationship(back_populates="company")
    # competitive_intelligence: Optional["CompetitiveIntelligence"] = Relationship(back_populates="company")
    # contact_information: Optional["ContactInformation"] = Relationship(back_populates="company")
    # digital_presence_brand: Optional["DigitalPresenceBrand"] = Relationship(back_populates="company")
    # financials_funding: Optional["FinancialsFunding"] = Relationship(back_populates="company")
    # indygx_assessment: Optional["IndygxAssessment"] = Relationship(back_populates="company")
    # partnerships_ecosystem: Optional["PartnershipsEcosystem"] = Relationship(back_populates="company")
