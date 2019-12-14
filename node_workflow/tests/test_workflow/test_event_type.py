import sys
import bisect
from pathlib import Path
import pandas as pd

node_path = str(Path(Path(Path(Path(__file__).resolve()).parent.resolve()).parent.resolve()).parent.resolve())

sys.path.insert(0, node_path)

from node import BaseTriggerEvent


class MinTriggerEvent(BaseTriggerEvent):
    """测试TriggerEvent；模拟真实workflow环境

    - 定义8个node，node之间进行复杂关联，测试整体稳定性；
        - 其中有1个node每过两次出现一次bug，导致status为FAILED，然后观察其他node状态：
            - 解决该node错误; set_status
            - 不解决该node错误: set_status

    test node link:
        node1 > node2 > node3

        node3 > node4 > node41
        node3 > node5 > node51

        node41 > node6
        node5 > node6

    """
    FMT = '%Y%m%d'

    def __init__(self, name='test_event', **kwargs):
        super().__init__(name, **kwargs)
        self._today = pd.datetime.now()
        self._date_list = list(pd.date_range(start='2019-12-01', end='2019-12-31', freq='D'))

    @property
    def _calendar(self):
        _index = bisect.bisect_left(self._date_list, self._today)
        return self._date_list[_index]

    @property
    def is_run_trigger(self) -> bool:
        return True

    @property
    def is_create_trigger(self) -> bool:
        return True if self._today.weekday() < 5 else False

    def get_event(self, cur_event=None) -> str:
        if cur_event is None:
            self._today = self._date_list[0]
        else:
            self._today = self._date_list[self._date_list.index(pd.to_datetime(cur_event))+1]
        return self._today.strftime(self.FMT)
