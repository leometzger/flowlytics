from flowlytics.core.models import Filters


class Query:

  def __init__(self, id: str, name: str, query_filter: Filters):
    self.id = id
    self.name = name
    self.filter = query_filter
