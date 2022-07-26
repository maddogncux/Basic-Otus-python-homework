from dataclasses import dataclass
"""
create dataclass `Engine`
"""


@dataclass(frozen=True)
class Engine:
    pistons: int = None
    volume: int = None
    # def __init__(self, pistons, volume):
    #     self.pistons = pistons
    #     self.volume = volume
