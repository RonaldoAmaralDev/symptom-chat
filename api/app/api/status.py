from fastapi import APIRouter
from app.services.status_service import check_status

router = APIRouter()

@router.get("/status")
def get_status():
    return check_status()