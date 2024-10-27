from sqlalchemy.ext.asyncio import AsyncAttrs

class ModelMixin(AsyncAttrs):
    async def update(self, **values):
        for k, v in values.items():
            setattr(self, k, v)
