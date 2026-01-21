from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class IndygxAssessment(SQLModel, table=True):
    __tablename__ = "indygx_specific_assessment"

    company_id: int = Field(primary_key=True)
    previous_interactions_with_indygx: str | None
    partnership_potential_rating: str | None
    collaboration_opportunity_score: str | None
    complementary_services_match_score: str | None