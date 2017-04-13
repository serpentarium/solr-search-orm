from pso.models import BaseModel
from pso_solr.query import StandardQuerySet


class Model(BaseModel):

    __queryset_class__ = StandardQuerySet
