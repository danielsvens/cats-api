from ..model.models import CatModel
from ..domain.cats import Cat


class CatService:
    
    def save_cat(self, data: dict) -> Cat:
        cat = self._serialize_cat(data)
        model = CatModel(cat)
        cat: CatModel = model.save()
        return cat.to_cat()

    def get_cats(self) -> list[Cat]:
        cats = CatModel.get_all()
        return sorted([c.to_cat() for c in cats], key=lambda e: e.name)

    def _serialize_cat(self, data: dict) -> Cat:
        return Cat(**data)
