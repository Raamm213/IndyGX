from fastapi import APIRouter, HTTPException
from ..repository.company_repositary import CompanySecondaryRepository
from ..schemas.company_secondary_digital import (
    CompanySecondaryCreateUpdate,
    CompanySecondaryRead,
)

from fastapi import APIRouter, HTTPException
from ..repository.company_repositary import DigitalPresenceBrandRepository
from ..schemas.company_secondary_digital import (
    DigitalPresenceBrandCreateUpdate,
    DigitalPresenceBrandRead,
)

router = APIRouter()

@router.get("/{company_id}", response_model=CompanySecondaryRead)
def get_secondary(company_id: int):
    obj = CompanySecondaryRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.put("/{company_id}", response_model=CompanySecondaryRead)
def upsert_secondary(
    company_id: int,
    payload: CompanySecondaryCreateUpdate
):
    return CompanySecondaryRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )

@router.delete("/{company_id}")
def delete_secondary(company_id: int):
    ok = CompanySecondaryRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
 


@router.get("/{company_id}", response_model=DigitalPresenceBrandRead)
def get_digital_presence_brand(company_id: int):
    obj = DigitalPresenceBrandRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.put("/{company_id}", response_model=DigitalPresenceBrandRead)
def upsert_digital_presence_brand(
    company_id: int,
    payload: DigitalPresenceBrandCreateUpdate
):
    return DigitalPresenceBrandRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )

@router.delete("/{company_id}")
def delete_digital_presence_brand(company_id: int):
    ok = DigitalPresenceBrandRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
