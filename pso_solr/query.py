"""
Solr implementation of DML QuerySet
"""
from collections import defaultdict
from pso.query import BaseQuerySet
from pso.q import Condition


class QuerySet(BaseQuerySet):
    """Extend Solr specific features"""


class StandardQuerySet(QuerySet):
    """
    Query converter for Solr Standard Query Parser
    """

    ESCAPE_CHARACTERS = str.maketrans({k: '\\' + k for k in [
        '\\', '+', '-', '!', '(',  ')',
        '{', '}', '[', ']', '^', '~', '*', '?', ':'
    ]})

    FORMAT_OPERATIONS = defaultdict(lambda: str, {
        Condition.EQ: '"{}"'.format,
        # TODO: Like, start/end_with ...
    })

    @classmethod
    def escape_value(cls, value):
        return str(value)\
            .translate(cls.ESCAPE_CHARACTERS)\
            .replace('&&', '\\&&')\
            .replace('||', '\\||')\
            .replace('AND ', '\\AND ')\
            .replace('OR ', '\\OR ')\
            .replace('NOT ', '\\NOT ')

    @classmethod
    def format_q(cls, q):
        not_op = 'NOT ' if q.inverted else ''
        boost = '^{}'.format(q.boost) if q.boost != 1 else ''
        field = '{}:'.format(q.field) if q.is_field else ''
        if q.is_leaf:
            value = cls.FORMAT_OPERATIONS[q.operation](cls.escape_value(q.value))

        else:
            childs = (cls.format_q(i) for i in q.childs)
            value = "(" + " {!s} ".format(q.operator).join(childs) + ")"
        return "".join([not_op, field, value, boost])

    def __str__(self):
        return self.format_q(self._filter)
