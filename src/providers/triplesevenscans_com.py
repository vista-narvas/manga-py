from src.providers.pzykosis666hfansub_com import Pzykosis666HFansubCom


class _Template(Pzykosis666HFansubCom):
    _name_re = '/reader/[^/]+/([^/]+)/'
    _content_str = '{}/reader/series/{}/'


main = _Template
