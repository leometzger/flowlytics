from .models import Filters
from .interfaces import FilterCommand

"""
  RwFilter is a basic command from Silk
"""
class RwFilter(FilterCommand):

  def __init__(self, filters: Filters):
    self.filters = filters

    assert self.filters.sensor or self.filters.input_file

  def cmd_as_array(self) -> [str]:
    command = [
      'rwfilter', 
      '--type=all', 
      '--all=stdout', 
    ]

    if self.filters.sensor:
      command.append('--sensor=' + self.filters.sensor)

    if self.filters.port:
      command.append('--aport=' + self.filters.port)

    if self.filters.protocol:
      command.append('--protocol=' + self.filters.protocol)

    if self.filters.start_date:
      command.append('--start-date=' + self.filters.start_date)

    if self.filters.end_date:
      command.append('--end-date' + self.filters.end_date)

    if self.filters.input_file:
      command.append(self.filters.input_file)

    return command


"""
  RwCount is responsible to create a Time Series
  output with Silk
"""
class RwCount(FilterCommand):
  
  def __init__(self, fields='', bin_size=300):
    self.bin_size = bin_size
    self.fields = fields

  def cmd_as_array(self):
    command = [
      'rwcount',
      '--type=all', 
      '--all=stdout', 
    ]

    if self.fields:
      command.append('--field=' + self.fields)

    return command


"""
  RwUnique is like a counter grouped_by
  something.
"""
class RwUnique(FilterCommand):

  def __init__(self, fields=''):
    self.fields = fields


  def cmd_as_array(self) -> [str]:
    command = [
      'rwunique',
      '--bytes',
      '--packets'
    ]

    if self.fields:
      command.append('--field=' + self.fields)

    return command
