from typing import List
from fastapi import APIRouter, status, Body, Depends, Path, HTTPException
from pydantic import UUID4
from store.schemas.product import ProductIn, ProductOut, ProductUpdate
from store.usecases.product import ProductUseCase
from store.core.exceptions import NotFoundException

router = APIRouter(tags=["products"])


@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(
    body: ProductIn = Body(...), usecase: ProductUseCase = Depends()
) -> ProductOut:
    try:
        return await usecase.create(body=body)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))


@router.get(path="/{id}", status_code=status.HTTP_200_OK)
async def get(
    id: UUID4 = Path(alias="id"), usecase: ProductUseCase = Depends()
) -> ProductOut:
    try:
        return await usecase.get(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.get(path="/", status_code=status.HTTP_200_OK)
async def query(usecase: ProductUseCase = Depends()) -> List[ProductOut]:
    return await usecase.query()


@router.patch(path="/{id}", status_code=status.HTTP_200_OK)
async def patch(
    id: UUID4 = Path(alias="id"),
    body: ProductUpdate = Body(...),
    usecase: ProductUseCase = Depends(),
) -> ProductOut:
    return await usecase.update(id=id, body=body)


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: UUID4 = Path(alias="id"), usecase: ProductUseCase = Depends()
) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
