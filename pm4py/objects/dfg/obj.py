from typing import Tuple, List


class DirectlyFollowsGraph:

    def __init__(self):
        self._graph = list()
        self._start_activities = list()
        self._end_activities = list()

    @property
    def graph(self) -> List[Tuple[str, str, int]]:
        return self._graph

    @property
    def start_activities(self) -> List[Tuple[str, int]]:
        return self._start_activities

    @property
    def end_activities(self) -> List[Tuple[str, int]]:
        return self._end_activities


DFG = DirectlyFollowsGraph
