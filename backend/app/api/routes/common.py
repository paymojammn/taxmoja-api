import structlog
from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.core.config import PROJECT_NAME, VERSION

struct_logger = structlog.get_logger(__name__)

router = APIRouter()

from pathlib import Path

backend = Path().absolute()

jinja_templates = Jinja2Templates(directory=f'{backend}/app/api/static/')


@router.get("/", response_class=HTMLResponse)
async def home_page():
    try:

        return jinja_templates.TemplateResponse(
            "templates/home/index.html", {"request": {"API Name": PROJECT_NAME, "version": VERSION}})

    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    try:

        return jinja_templates.TemplateResponse(
            "/templates/home/dashboard.html", {"request": {"API Name": PROJECT_NAME, "version": VERSION}})

    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))


@router.get("/recon", response_class=HTMLResponse)
async def recon_page():
    try:

        return jinja_templates.TemplateResponse(
            "/templates/home/recon.html", {"request": {"API Name": PROJECT_NAME, "version": VERSION}})

    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))


@router.get("/eula", response_class=HTMLResponse)
async def eula_page():
    try:

        return jinja_templates.TemplateResponse(
            "/templates/home/eula.html", {"request": {"API Name": PROJECT_NAME, "version": VERSION}})

    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))