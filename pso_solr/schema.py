"""Schema.xml builder"""
from collections import OrderedDict
from lxml import etree
from lxml.builder import E


class SchemaBuilder():

    user_types = OrderedDict()  # Collect all user defined field types
    models = []
    fields_map = {}
    default_operator = 'OR'
    unique_field = None
    name = ''

    def __init__(self, name):
        self.name = name

    def add_field_type(self, field_type):
        if isinstance(field_type, str):
            return
        if field_type.name in self.user_types:
            return  # Todo: name conflict check.
        self.user_types[field_type.name] = field_type

    def add_analyzer(self):
        pass  # Maybe Elastic required

    def add_model(self, model):
        self.models.append(model)
        for field in model.get_fields():
            self.add_field_type(field.field_type)
            self.add_field(field)

    def add_field(self, field):
        if field.field_name in self.fields_map:
            # TODO normal check
            existing = self.fields_map[field.field_name]
            if type(existing) != type(field) \
               or field.multi_valued != existing.multi_valued:
                raise ValueError(
                    'Two different type fields with same name '
                    '"{name}" within one schema.\n'
                    'Change name or use model prefix'
                    ''.format(name=field.field_name)
                )
        else:
            self.fields_map[field.field_name] = field
    #
    #

    def get_schema_xml(self):
        types = (self.field_type_xml(ft) for ft in self.user_types.values())
        fields = (self.field_xml(field) for field in self.fields_map.values())
        config = self.get_config_xml()
        return(etree.tostring(
            E('schema', *types, *fields, *config, name=self.name),
            pretty_print=True,
            xml_declaration=True,
            encoding="utf-8"))

    def field_type_xml(self, field_type):
        analyzers = (self.analyzer_xml(a) for a in field_type.analyzers)
        return E('fieldType', *analyzers,
                 name=field_type.name, **field_type.config)

    def analyzer_xml(self, analyzer):
        filters = (E('filter', **f.config) for f in analyzer.filters)
        tokenizer = E('tokenizer', **analyzer.tokenizer)

        return E('analyzer', tokenizer, *filters,
                 name=analyzer.name, **analyzer.config)

    def field_xml(self, field):
        return E('field',
                 name=field.field_name,
                 store='true' if field.store else 'false',
                 boost=str(field.boost),
                 index='true' if field.index else 'false',
                 multi_valued='true' if field.multi_valued else 'false')

    def get_config_xml(self):
        config_xml = [
            E('solrQueryParser', {'defaultOperator': self.default_operator}),
        ]
        if self.unique_field:
            config_xml.append(E('uniqueKey', self.unique_field))
        return config_xml

