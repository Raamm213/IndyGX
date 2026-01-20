from fastapi import APIRouter, HTTPException
from ..repository.financials_funding_repo import FinancialsFundingRepository
from ..schemas.financialsFunding import (
    FinancialsFundingCreateUpdate,
    FinancialsFundingRead,
)

router = APIRouter()

@router.get("/{company_id}", response_model=FinancialsFundingRead)
def get_financials_funding(company_id: int):
    obj = FinancialsFundingRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.put("/{company_id}", response_model=FinancialsFundingRead)
def upsert_financials_funding(
    company_id: int,
    payload: FinancialsFundingCreateUpdate
):
    return FinancialsFundingRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )

@router.delete("/{company_id}")
def delete_financials_funding(company_id: int):
    ok = FinancialsFundingRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
