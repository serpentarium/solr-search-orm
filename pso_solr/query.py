"""
Solr implementation of DML QuerySet
"""
from pso.query import BaseQuerySet


class QuerySet(BaseQuerySet):
    """Extend Solr specific features"""


class StandardQuerySet(QuerySet):
    """
    Query converter for Solr Standard Query Parser
    """

    @classmethod
    def format_q(cls, q):
        boost = '^{}'.format(q.boost) if q.boost != 1 else ''
        if q.is_leaf:
            if q.is_field:
                return "{field}:{value}".format(field=q.field, value=str(q.value))

        else:
            childs = (cls.format_q(i) for i in q.childs)
            return "(" + " {!s} ".format(q.operator).join(childs) + ")" + boost

    def __str__(self):
        return self.format_q(self._filter)
