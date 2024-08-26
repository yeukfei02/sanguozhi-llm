from fastapi import APIRouter, Request
from controller.sanguozhi_data_controller import sanguozhi_data_controller

data_router = APIRouter()


@data_router.get("/sanguozhi-data")
def get_sanguozhi_data(request: Request):
    return sanguozhi_data_controller(request)
