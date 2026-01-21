from fastapi import APIRouter, HTTPException
from ..repository.company_contact_repo import ContactInformationRepository
from ..schemas.company_contact_schema import (
    ContactInformationCreateUpdate,
    ContactInformationRead,
)

router = APIRouter()

@router.get("/{company_id}", response_model=ContactInformationRead)
def get_contact_information(company_id: int):
    obj = ContactInformationRepository.get(company_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.put("/{company_id}", response_model=ContactInformationRead)
def upsert_contact_information(
    company_id: int,
    payload: ContactInformationCreateUpdate
):
    return ContactInformationRepository.upsert(
        company_id,
        payload.model_dump(exclude_unset=True)
    )

@router.delete("/{company_id}")
def delete_contact_information(company_id: int):
    ok = ContactInformationRepository.delete(company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}
