from fastapi import APIRouter

from services.stats_service import (
    get_pass_fail,
    get_marks,
    get_dashboard
)

router = APIRouter()


@router.get("/pass-fail/{reg_no}")
def pass_fail(reg_no: str):
    return get_pass_fail(reg_no)


@router.get("/marks/{reg_no}")
def marks(reg_no: str):
    return get_marks(reg_no)


@router.get("/dashboard/{reg_no}")
def dashboard(reg_no: str):
    return get_dashboard(reg_no)