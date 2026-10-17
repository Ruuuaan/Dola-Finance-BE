from fastapi import APIRouter

name = __name__.rsplit(".", 1)[-1]
router = APIRouter(prefix=f"/{name}", tags=[name])


@router.get("/hello")
def hello():
    return {"message": f"hello world from router: {__name__}"}