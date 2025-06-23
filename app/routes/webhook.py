from fastapi import APIRouter, BackgroundTasks, Depends, Header, Security, status
from fastapi.responses import JSONResponse, Response
from fastapi.security import APIKeyHeader

router = APIRouter(tags=["Web Hooks"], prefix="/webhook")

@router.post("/data-pipeline")
def data_pipeline():
    """Web hook for process profile cadastration"""
