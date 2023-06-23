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
            img_context_list = one_detail_element.section.find_all("img")
            img_str = ""
            if img_context_list:
                img_src_list = [i.attrs["src"] for i in img_context_list]
                img_str = "\n".join(img_src_list)
                img_str = "图片内容：" + img_str
            context = one_detail_element.section.text + img_str
            analysis = self.get_answer_detail(cur_id.replace("ana", ""))
            return {"diff_value": diff_value, "cur_id": cur_id, 'context': context, "analysis": analysis}
        except:
            return {}

    def get_answer_detail(self, id) -> dict:
        """获取当前的详情"""
        url = "https://www.tiku.cn/tikuapi/question/anylysis/"
        header = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Cookie": "PHPSESSID=2mnj85ehv3bsq08qr8nlvcamn7; Hm_lvt_02f32149c7ea90d0cd47ed89025e457c=1686917647; think_var=zh-cn; uid=54681; token=e44a179d-9d50-45df-bfed-758eb5b1fe76; Hm_lpvt_02f32149c7ea90d0cd47ed89025e457c=1687336251",
            "Origin": "https://www.tiku.cn",
            "Referer": "https://www.tiku.cn/index/index/questions.html?cid=14&cno=1&vid=800016&bid=800110",
            "X-Requested-With": "XMLHttpRequest"
        }
        res = requests.post(url, headers=header, data={"id": id})
        return json.loads(res.text)


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


def get_answer_detail_test():
    id = "3012447"
    res = parse.get_answer_detail(id)


if __name__ == '__main__':
    get_answer_detail_test()








