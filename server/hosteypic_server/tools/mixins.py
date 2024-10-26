class ModelMixin():
    async def update(self, **values):
        for k, v in values.items():
            setattr(self, k, v)
