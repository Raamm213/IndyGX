from fastapi import APIRouter, HTTPException
from ..repository.company_partnership_repo import PartnershipsEcosystemRepository
from ..schemas.company_partnership_schemas import PartnershipsEcosystemCreateUpdate,PartnershipsEcosystemRead

router = APIRouter()

@router.get("/{company_id}", response_model=PartnershipsEcosystemRead)
def get_partnerships_ecosystem(company_id: int):
    obj = PartnershipsEcosystemRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.put("/{company_id}", response_model=PartnershipsEcosystemRead)
def upsert_partnerships_ecosystem(
    company_id: int,
    payload: PartnershipsEcosystemCreateUpdate
):
    return PartnershipsEcosystemRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )

@router.delete("/{company_id}")
def delete_partnerships_ecosystem(company_id: int):
    ok = PartnershipsEcosystemRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
