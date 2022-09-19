from fastapi import APIRouter
from models.parse import ParseModel


router = APIRouter()


@router.get('/ping')
async def ping_pong():
    return 'pong'


@router.post('/parse', response_model=ParseModel)
async def parse_parameters(args: ParseModel):
    return args
