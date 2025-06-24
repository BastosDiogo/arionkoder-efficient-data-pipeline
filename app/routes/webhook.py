from fastapi import APIRouter, BackgroundTasks, status
from fastapi.responses import JSONResponse
from fastapi import Request
from services.stream_process import ProcessData
from fastapi.encoders import jsonable_encoder

router = APIRouter(tags=["Web Hooks"], prefix="/webhook")

@router.post("/data-pipeline")
async def data_pipeline(request: Request, background: BackgroundTasks):
    """Web hook for process profile cadastration
    \nParameters:
    \n`first_name`: User's frist name. Format `str`;
    \n`last_name`: User's last name. Format `str`;
    \n`age`: User's age name. Format `int`;
    \n`document`: User's brazilian documento knowen as CPF. Format `str`. OBS.: With or without special caracters like '.' and '-';
    \n`web_site`: User's professional web site, as Linkdin. Format `str`.
    """
    body = await request.body()
    background.add_task(ProcessData().process_stream, body)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={'message': 'Creating profiles'}
    )


@router.get("/data-pipeline/users")
def data_pipeline_users():
    """Return all users in database"""

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(ProcessData().find_all())
    )


@router.delete("/data-pipeline/delete-users")
def data_pipeline_delete_users():
    """Delete all users in database"""
    ProcessData().clean_database()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={'message': 'Users has been delete.'}
    )