
from fastapi import APIRouter,Depends
from ..schemas.company_filter import CompanyPrimaryFilter
from ..schemas.common import PaginatedResponse,PaginationMeta
from ..repository.company_repository import CompanyRepository
from ..schemas.company_full_profile import CompanyListItem
from ..schemas.company_bulk_upsert import BulkUpsertRequest


router = APIRouter()

@router.get("/", response_model=PaginatedResponse[CompanyListItem])
def list_companies(
    filters: CompanyPrimaryFilter = Depends(),
    page: int = 1,
    page_size: int = 20,
):
    data, total = CompanyRepository.list_companies(
        filters, page, page_size
    )

    return PaginatedResponse(
        data=data,
        meta=PaginationMeta(
            page=page,
            page_size=page_size,
            total_records=total,
            total_pages=(total + page_size - 1) // page_size,
        ),
    )
 

@router.post("/bulk-upsert")
def bulk_upsert(payload: BulkUpsertRequest):
    CompanyRepository.bulk_upsert(payload.items)
    return {"status": "success"}
