from fastapi import APIRouter, HTTPException
from ..repository.company_indygx_repo import IndygxAssessmentRepository
from ..schemas.company_indygx_assessment_schema import IndygxAssessmentRead,IndygxAssessmentCreateUpdate

router = APIRouter()

@router.get("/{company_id}", response_model=IndygxAssessmentRead)
def get_indygx_assessment(company_id: int):
    obj = IndygxAssessmentRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.put("/{company_id}", response_model=IndygxAssessmentRead)
def upsert_indygx_assessment(
    company_id: int,
    payload: IndygxAssessmentCreateUpdate
):
    return IndygxAssessmentRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )

@router.delete("/{company_id}")
def delete_indygx_assessment(company_id: int):
    ok = IndygxAssessmentRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
