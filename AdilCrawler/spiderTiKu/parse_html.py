# coding: utf-8
"""
解析hmtl 操作
"""
import json, requests, time, os, pickle
import random
from bs4 import BeautifulSoup


class ParseHtml(object):
    def __init__(self, logger):
        self.logger = logger

    def request(self, url) -> BeautifulSoup:
        """请求页面"""
        response = requests.get(url)
        text = response.text if response.status_code == 200 else ""
        soup = BeautifulSoup(text, 'html.parser')
        return soup

    def get_page(self, url) -> int:
        """获取当前的最大页码"""
        soup = self.request(url)
        li_list = [i for i in soup.find(class_="pagination").children if not i.find("li")]
        max_page = li_list[-2].text
        return int(max_page)

    def get_detail_list(self, url) -> list:
        """获取每页详情"""
        soup = self.request(url)
        div_list = list(soup.find_all("div", class_="card mb-3 q-detail rounded-0"))
        return div_list

    def get_detail_by_one(self, one_detail_element):
        """获取当个元素的详情"""
        try:
            diff_value = one_detail_element.div.span.a.text
            cur_id = [i for i in one_detail_element.children if not i.find('div')][-1].attrs["id"]
            context = one_detail_element.section.text
            return {"diff_value": diff_value, "cur_id": cur_id, 'context': context}
        except:
            return {}

    def get_answer_detail(self, id):
        """获取当前的详情"""

        pass



import logging

parse = ParseHtml(logging)


def get_max_page():
    url = "https://www.tiku.cn/index/index/questions.html?"
    max_page = parse.get_page(url)
    print(max_page)


def get_detail_list_test():
    url = "https://www.tiku.cn/index/index/questions.html?"
    detail_list = parse.get_detail_list(url)
    res = parse.get_detail_by_one(detail_list[0])
    print(res)


    pass


if __name__ == '__main__':
    get_detail_list_test()








