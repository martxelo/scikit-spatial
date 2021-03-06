from typing import Tuple

from matplotlib.axes import Axes
from matplotlib.figure import Figure

from skspatial.typing import array_like


class Circle:

    def __init__(self, xy: array_like, radius: float = 5, **kwargs) -> None: ...


def figure(**kwargs) -> Figure: ...

def subplots(**kwargs) -> Tuple[Figure, Axes]: ...
