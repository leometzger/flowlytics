from .interfaces import SelectorCommand

class RwCut(SelectorCommand):

  def __init__(self, fields='1-9'):
    self.fields = fields

    assert fields is not None

  def cmd_as_array(self):
    command = ['rwcut', '--fields', self.fields]

    return command