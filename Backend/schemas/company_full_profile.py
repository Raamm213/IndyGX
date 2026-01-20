from pydantic import BaseModel
from .company_primary import CompanyPrimaryRead
from .company_secondary import CompanySecondaryBase
from .competitiveIntelligence import CompetitiveIntelligenceBase
from .contactInformation import ContactInformationBase
from .digitalPresenceBrand import DigitalPresenceBrandBase
from .financialsFunding import FinancialsFundingBase
from .indygxAssessment import IndygxAssessmentBase
from .partnershipsEcosystem import PartnershipsEcosystemBase



class CompanyListItem(BaseModel):
    company_id: int
    company_name: str


class CompanyFullProfile(CompanyPrimaryRead):
    secondary: CompanySecondaryBase | None
    competitive_intelligence: CompetitiveIntelligenceBase | None
    contact_information: ContactInformationBase | None
    digital_presence_brand: DigitalPresenceBrandBase | None
    financials_funding: FinancialsFundingBase | None
    indygx_assessment: IndygxAssessmentBase | None
    partnerships_ecosystem: PartnershipsEcosystemBase | None
 