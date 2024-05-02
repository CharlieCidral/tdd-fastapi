from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from store.schemas.product import ProductIn, ProductOut
from store.db.mongo import db_client


class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product = ProductOut(**body.model_dump())
        await self.collection.insert_one(product.model_dump())
        breakpoint()

        return product

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})
        return ProductOut(**result)


product_usecase = ProductUsecase()
