from subprocess import Popen, PIPE

from .interfaces import Runner, FilterCommand, SelectorCommand
from .models import Flow

"""
  Default runner
"""
class SilkRunner(Runner):

  def __init__(self):
    pass

  def run(self, filter_cmd: FilterCommand, selector: SelectorCommand) -> [Flow]:
    with Popen(filter_cmd.cmd_as_array(), stdout=PIPE) as cmd:
      with Popen(selector.cmd_as_array(), stdin=cmd.stdout, stdout=PIPE) as selector:
        for line in selector.stdout.readlines():
          yield self._parse_flow(str(line))



  def _parse_flow(self, flow) -> Flow:
    cols = flow.split('|')
    return Flow(
      source_ip=cols[0],
      destination_ip=cols[1],
      port=cols[2],
      protocol=cols[3],
      packets=cols[4],
      flow_bytes=cols[5]
    )
  