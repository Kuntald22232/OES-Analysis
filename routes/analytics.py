from fastapi import APIRouter
from services.stats_service import get_pass_fail, get_marks

router = APIRouter()

@router.get("/pass-fail/{reg_no}")
def pass_fail(reg_no: str):
    return get_pass_fail(reg_no)

@router.get("/marks/{reg_no}")
def marks(reg_no: str):
    return get_marks(reg_no)