from fastapi import APIRouter, HTTPException
from ..repository.competitive_intelligence_repo import CompetitiveIntelligenceRepository
from ..schemas.competitiveIntelligence import (
    CompetitiveIntelligenceCreateUpdate,
    CompetitiveIntelligenceRead,
)

router = APIRouter()

@router.get("/{company_id}", response_model=CompetitiveIntelligenceRead)
def get_item(company_id: int):
    obj = CompetitiveIntelligenceRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.put("/{company_id}", response_model=CompetitiveIntelligenceRead)
def upsert_item(company_id: int, payload: CompetitiveIntelligenceCreateUpdate):
    return CompetitiveIntelligenceRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )

@router.delete("/{company_id}")
def delete_item(company_id: int):
    ok = CompetitiveIntelligenceRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
