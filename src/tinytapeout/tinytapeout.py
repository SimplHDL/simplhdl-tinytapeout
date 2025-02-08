import logging

from argparse import Namespace
from pathlib import Path
from simplhdl.flow import FlowFactory, FlowBase
from simplhdl.pyedaa.project import Project


logger = logging.getLogger(__name__)


@FlowFactory.register('tinytapeout')
class TinyTapeoutFlow(FlowBase):
    def __init__(self):
        pass

    @classmethod
    def parse_args(self, subparsers) -> None:
        parser = subparsers.add_parser('tinytapeout', help='Tiny Tapeout development Flow')
        parser.add_argument(
            '--step',
            action='store',
            choices=[
                'lint',
                'elaborate',
                'synthesis',
                'place',
                'route',
                'gds'],
            default='gds',
            help="flow step to run"
        )
        parser.add_argument(
            '--gui',
            action='store_true',
            help="Open project in GUI"
        )
        parser.add_argument(
            '--archive',
            choices=[
                'project'
            ],
            default='project',
            help="Archive project"
        )

    def __init__(self, name, args: Namespace, project: Project, builddir: Path):
        super().__init__(name, args, project, builddir)

    def run(self):
        raise NotImplementedError("TinyTapeoutFlow.run() not implemented")
