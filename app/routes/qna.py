from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

qna_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
qna_router.mount('/static', StaticFiles(directory='views/static'), name='static')

@qna_router.get('/qna', response_class=HTMLResponse)
def qna(req: Request):
    return templates.TemplateResponse('qna/qna.html', {'request': req})


