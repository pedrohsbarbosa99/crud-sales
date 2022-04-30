from datetime import datetime
from ninja import Schema


class SaleSchema(Schema):
    sale_id: int
    created_at: datetime
    total: float
    status: str
    products_count: int
    state: str

class SaleByStateSchema(Schema):
    total: float
    state: str

class NotFoundSchema(Schema):
    message: str