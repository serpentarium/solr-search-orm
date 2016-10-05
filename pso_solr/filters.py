"""
Default tokenizers classes.
Ream more on https://cwiki.apache.org/confluence/display/solr/Tokenizers
"""


class BaseFilter():
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


class Ololo(BaseFilter):
    solr_class = "solr.oololo"
    attributes = ['maxTokenLength']
