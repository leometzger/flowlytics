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
    output = ''

    with Popen(filter_cmd.cmd_as_array(), stdout=PIPE) as cmd:
      with Popen(selector.cmd_as_array(), stdin=cmd.stdout, stdout=PIPE) as selector:
        output += str(selector.stdout.read())

    return self._parse_flows(output)


  def _parse_flows(self, flows_as_string) -> [Flow]:
    flows = flows_as_string.split('\\n')
    flows = flows[1:len(flows)-1]
    parsed_flows = []

    for flow in flows:
      cols = flow.split('|')
      flow = Flow(
        source_ip=cols[0],
        destination_ip=cols[1],
        port=cols[2],
        protocol=cols[3],
        packets=cols[4],
        flow_bytes=cols[5]
      )
      parsed_flows.append(flow)

    return parsed_flows

  