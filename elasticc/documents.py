from django_elasticsearch_dsl import (
    Document ,
    fields,
    Index,
)
from django_elasticsearch_dsl.registries import registry
from .models import DemoElastic


PUBLISHER_INDEX = Index('demo_elastic') # db name for elastic search

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)


@PUBLISHER_INDEX.doc_type
class NewsDocument(Document):
    
    id = fields.IntegerField(attr='id')
    fielddata=True
    title = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    content = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
   

    class Django(object):
        model = DemoElastic
        # fields = [
        #     'title',
        #     'content',
        # ]