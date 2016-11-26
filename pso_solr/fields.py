"""
Sold predefined fields. Details:
https://cwiki.apache.org/confluence/display/solr/Field+Types+Included+with+Solr
And other fields
"""
from pso.fields import BaseField
from pso.fields import FieldType
from pso.analyzers import Analyzer


def solr_auto_field_type(name):
    return FieldType(name, **{'class': 'solr.{name}'.format(name=name)})


# Solr predefined field types
class BinaryField(BaseField):
    field_type = solr_auto_field_type('BinaryField')


class BoolField(BaseField):
    field_type = solr_auto_field_type('BoolField')


class CollationField(BaseField):
    field_type = solr_auto_field_type('CollationField')


class CurrencyField(BaseField):
    field_type = solr_auto_field_type('CurrencyField')


class DateRangeField(BaseField):
    field_type = solr_auto_field_type('DateRangeField')


class ExternalFileField(BaseField):
    field_type = solr_auto_field_type('ExternalFileField')


class EnumField(BaseField):
    field_type = solr_auto_field_type('EnumField')


class ICUCollationField(BaseField):
    field_type = solr_auto_field_type('ICUCollationField')


class LatLonType(BaseField):
    field_type = solr_auto_field_type('LatLonType')


class PointType(BaseField):
    field_type = solr_auto_field_type('PointType')


class PreAnalyzedField(BaseField):
    field_type = solr_auto_field_type('PreAnalyzedField')


class RandomSortField(BaseField):
    field_type = solr_auto_field_type('RandomSortField')


class SpatialRecursivePrefixTreeField(BaseField):
    field_type = solr_auto_field_type('SpatialRecursivePrefixTreeFieldType')


class StrField(BaseField):
    field_type = solr_auto_field_type('StrField')


class TextField(BaseField):
    field_type = solr_auto_field_type('TextField')


class TrieDateField(BaseField):
    field_type = solr_auto_field_type('TrieDateField')


class TrieDoubleField(BaseField):
    field_type = solr_auto_field_type('TrieDoubleField')


class TrieField(BaseField):
    field_type = solr_auto_field_type('TrieField')


class TrieFloatField(BaseField):
    field_type = solr_auto_field_type('TrieFloatField')


class TrieIntField(BaseField):
    field_type = solr_auto_field_type('TrieIntField')


class TrieLongField(BaseField):
    field_type = solr_auto_field_type('TrieLongField')


class UUIDField(BaseField):
    field_type = solr_auto_field_type('UUIDField')


# Aliases
CharField = StrField
DateTimeField = TrieDateField
DoubleField = TrieDoubleField
# TrieField
FloatField = TrieFloatField
IntegerField = TrieIntField
# LongField = TrieLongField
