from __future__ import annotations

from .. import db
from ..domain.cats import Cat
from datetime import datetime
from pytz import timezone

class CatModel(db.Model):
    __tablename__ = 'cats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text())
    created = db.Column(db.Date())

    def __init__(self, cat: Cat) -> None:
        self.name = cat.name
        self.description = cat.description
        self.created = datetime.now(timezone('Europe/Stockholm'))

    def save(self) -> int:
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def get_all(cls) -> list[CatModel]:
        return cls.query.all()

    @classmethod
    def get_cat(cls, cat_id: int) -> CatModel:
        return cls.query.get(cat_id)

    def to_cat(self) -> Cat:
        return Cat(self.name, self.description)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: {self.id}>'
