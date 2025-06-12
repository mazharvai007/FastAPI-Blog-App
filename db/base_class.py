# db/base_class.py

import inflect
from typing import Any
from sqlalchemy.ext.declarative import declared_attr

from sqlalchemy.orm import as_declarative

# from sqlalchemy.orm import DeclarativeBase

# Create an inflect engine to convert singular to plural
inflect_engine = inflect.engine()


@as_declarative()
class Base:
    # class Base(DeclarativeBase):
    id: Any
    __name__: str

    # To generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        # Convert class name to lowercase and pluralize it
        singular_name: str = cls.__name__.lower()
        plural_name: str = inflect_engine.plural(singular_name)

        return plural_name
