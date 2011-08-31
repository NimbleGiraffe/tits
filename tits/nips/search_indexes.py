from haystack.indexes import *
from haystack import site
from nips.models import Nipple


class NippleIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Nipple.objects.all()


site.register(Nipple, NippleIndex)