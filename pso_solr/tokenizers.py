"""
Default tokenizers classes.
Ream more on https://cwiki.apache.org/confluence/display/solr/Tokenizers
"""


class BaseTokenizer():
    attributes = []
    _config = {}
    solr_class = None

    def __init__(self, *args, **kwargs):
        for ndx, arg in enumerate(args):
            try:
                self._config[self.attributes[ndx]] = arg
            except IndexError:
                raise ValueError('Wrong configuration. Too much arguments')

        for key, arg in kwargs.items():
            if key in self.attributes:
                self._config[key] = arg
            else:
                raise ValueError(
                    'Unsupported setting <{key}> for {cls}'.format(
                        key=key, cls=self.__class__)
                )

    @property
    def config(self):
        conf = dict(self._config)
        conf.update({'class': self.solr_class})


class StandardTokenizer(BaseTokenizer):
    solr_class = "solr.StandardTokenizerFactory"
    attributes = ['maxTokenLength']


class ClassicTokenizer(BaseTokenizer):
    solr_class = "solr.ClassicTokenizerFactory"
    attributes = ['maxTokenLength']


class KeywordTokenizer(BaseTokenizer):
    solr_class = "solr.KeywordTokenizerFactory"


class LetterTokenizer(BaseTokenizer):
    solr_class = "solr.LetterTokenizerFactory"


class LowerCaseTokenizer(BaseTokenizer):
    solr_class = "solr.LowerCaseTokenizerFactory"


class NGramTokenizer(BaseTokenizer):
    solr_class = "solr.NGramTokenizerFactory"
    attributes = ['minGramSize', 'maxGramSize']


class EdgeNGramTokenizer(BaseTokenizer):
    solr_class = "solr.EdgeNGramTokenizerFactory"
    attributes = ['minGramSize', 'maxGramSize', 'side']


class ICUTokenizer(BaseTokenizer):
    solr_class = "solr.ICUTokenizerFactory"
    attributes = ['minGramSize', 'maxGramSize']


class PathHierarchyTokenizer(BaseTokenizer):
    solr_class = "solr.PathHierarchyTokenizerFactory"
    attributes = ['delimiter', 'replace']


class PatternTokenizer(BaseTokenizer):
    solr_class = "solr.PatternTokenizerFactory"
    attributes = ['pattern', 'group']

class URLEmailTokenizer(BaseTokenizer):
    solr_class = "solr.UAX29URLEmailTokenizerFactory"
    attributes = ['maxTokenLength']

class WhitespaceTokenizer(BaseTokenizer):
    solr_class = "solr.WhitespaceTokenizerFactory"
    attributes = ['rule']  # java|unicode

