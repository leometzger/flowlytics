from abc import ABC, abstractmethod


"""
  Interface to build filter commands, pipes
  the output to Selector
"""
class FilterCommand(ABC):

    @abstractmethod
    def cmd_as_array(self):
      pass


"""
  Interface to build select commands, piped by
  a Filter method
"""
class SelectorCommand(ABC):

    @abstractmethod
    def cmd_as_array(self):
      pass


"""
  Runner Interface responsible to run
  commands
"""
class Runner(ABC):

  @abstractmethod
  def run(self, filter_cmd: FilterCommand, selector_cmd: SelectorCommand):
    pass
  