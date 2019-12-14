# encoding: utf-8
import pandas as pd
import copy
import sys
import os
import time
import random
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from node import NodeManager, TriggerStatus


class WebNodeManager(NodeManager):
    def __init__(self, node_config):
        super().__init__(node_config)

    @staticmethod
    def _print_trigger_status(trigger_event, trigger_map):
        print()
        # print(f'{pd.datetime.now().strftime(DATE_STR_FORMAT)}')
        for trigger_name, status in trigger_map.items():
            print('\t\t{} {}: {}'.format(
                trigger_event,
                trigger_name,
                status.name))
        print()

    def run(self):
        while True:
            # print('=' * 20 + pd.datetime.now().strftime(DATE_STR_FORMAT) + '=' * 20)
            all_trigger_status = copy.deepcopy(self.node_config.all_trigger_status)
            for _trigger_event, _item in all_trigger_status.items():
                # if status is None, node does not start running, so there is no status
                if all(map(lambda x: (x == TriggerStatus.FINISH) or (x is None), _item.values())):
                    continue
                self._print_trigger_status(_trigger_event, _item)
            time.sleep(self.default_interval)
            pass

# output all nodes ..
# config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "node_config/daily_data_update.yaml")
# print(os.path.dirname(os.path.dirname(__file__)))
# ab = WebNodeManager(node_config=r'F:\test\node_workflow\tests\test_workflow\test_config.yaml')
#
# all config
# cd = ab.node_config.get_all_node_config()
#
# result = ab.run()
# print(ab.run())


def geneteate_web_node():
    ab = WebNodeManager(node_config=r'F:\test\node_workflow\tests\test_workflow\test_config.yaml')
    cd = ab.node_config.get_all_node_config()
    result = list()

    node_map = {node: index+1 for index,  node in enumerate(list(cd.keys()))}
    node_list, links_list = list(), list()
    for k, v in cd.items():

        watch_trigger = v["watch_trigger"]
        if watch_trigger == None:
            parents = None
        elif isinstance(watch_trigger, list):
            parents = [parent.split('/')[-1] for parent in v["watch_trigger"]]
        else:
            parents = [v["watch_trigger"].split('/')[-1]]

        node_list.append({"id": node_map[k], "label": k, 'age': 'kid', 'gender': 'male'})

        if watch_trigger == None: continue

        [links_list.append({"from": node_map[p], "to": node_map[k], 'relation': 'parent', 'arrows': 'to','color': { 'color': 'red'}}) for p in parents]
        # if watch_trigger:



    print(node_list)
    print('/n'*3)
    print(links_list)



geneteate_web_node()

