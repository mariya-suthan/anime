from fastapi import APIRouter

router = APIRouter()

@router.get("/sos")
def sos_test():
    return {"message": "SOS route working"}