import databases
import ormar
import sqlalchemy

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Customer(ormar.Model):
    class Meta(BaseMeta):
      	tablename = "customers"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=128, unique=True, nullable=False)
    age: int = ormar.Integer(nullable=False)
    street: str = ormar.String(max_length=128, nullable=False)
    number: str = ormar.String(max_length=8, nullable=False)
    neighborhood: str = ormar.String(max_length=32, nullable=False)
    complement: str = ormar.String(max_length=128, nullable=False)
    city: str = ormar.String(max_length=32, nullable=False)
    state: str = ormar.String(max_length=16, nullable=False)
    country: str = ormar.String(max_length=32, nullable=False)
    active: bool = ormar.Boolean(default=True, nullable=False)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
