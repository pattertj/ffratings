from enum import Enum


class Position(Enum):
    QB = 1
    RB = 2
    WR = 3
    TE = 4
    DST = 5
    K = 6
    ALL = 7


class Source(Enum):
    BetIQ = 1
