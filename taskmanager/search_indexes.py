from haystack import indexes
#引入你项目下的model（也就是你要将其作为检索关键词的models）
from .models import Knowledge


# 指定对于摸个类的某些数据建立索引
# 索引类名格式：模型类型+Index
class KnowledgeIndex(indexes.SearchIndex, indexes.Indexable):
    # 索引字段
    # use_template=True：指定根据表中的哪些字段建立索引文件，把说明放在一个文件中
    text = indexes.CharField(document=True, use_template=True)
    product = indexes.CharField(model_attr='product')
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')

    def get_model(self):
        # 返回你的模型类
        return Knowledge

    # 建立索引的数据
    def index_queryset(self, using=None):
        return self.get_model().objects.all()