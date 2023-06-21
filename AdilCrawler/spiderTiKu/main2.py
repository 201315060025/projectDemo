# coding: utf-9
"""
爬取题库的试题
https://www.tiku.cn/index/index/questions.html?cid=14&cno=1&vid=800023&typeid=600126
"""
import logging

logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S"


class TiKuSpider(object):
    def __init__(self, url, logger, parser):
        self.url = url
        self.parser = parser
        self.logger = logger

    def get_version_list(self) -> []:
        """获取不同版本的url"""
        base_url = "https://www.tiku.cn/index/index/questions.html?cid=14&cno=1&vid=800016"
        version_list = [
            {"name": "人教版", "vid": 800016},
            {"name": "北师大版", "vid": 800023},
            {"name": "冀教版", "vid": 800136},
            {"name": "苏教版", "vid": 800139},
            {"name": "西师版", "vid": 800140},
            {"name": "青岛六三版", "vid": 800137},
            {"name": "青岛五四版", "vid": 800138},
        ]
        return version_list

    def get_course_list(self) -> list:
        """获取每个版本下的课程url"""
        base_url = "https://www.tiku.cn/index/index/questions.html?cid=14&cno=1&vid=800139&bid="
        course_list = [
            {"name":'三年级上册', 'bid': "801013"},
            {"name": '三年级下册', 'bid': "801020"},
            {"name": '四年级上册', 'bid': "801021"},
            {"name": '四年级下册', 'bid': "801022"},
            {"name": '五年级上册', 'bid': "801023"},
            {"name": '五年级下册', 'bid': "801024"},
            {"name": '六年级上册', 'bid': "801031"},
            {"name": '六年级下册', 'bid': "801032"},
        ]
        return course_list

    def get_topic_type(self) -> list:
        """
        获取题型
        """
        topic_type = [{
            "name": '应用题', "typeid": 600126
        }]

    def get_content_by_page(self, url, page=1):
        """获取详情"""


        pass

    def get_page_list(self, url) -> int:
        """获取总共有多少页"""

        return 1

    def get_detail_by_category(self, category_url):
        """获取某一个类型下面所有的数据"""



    def main(self):
        """"""
        base_url = "https://www.tiku.cn/index/index/questions.html?cid=14&cno=1&vid={}&bid={}&typeid={}&page={}"
        # 获取不同类型的版本
        version_list = self.get_version_list()
        self.logger.info("版本信息：" )
        self.logger.info(version_list)
        # 获取不同的课本
        course_list = self.get_course_list()
        self.logger.info("课程信息：")
        self.logger.info(course_list)
        topic_type_list = self.get_topic_type()
        self.logger.info("题目类型：")
        self.logger.info(topic_type_list)
        result = {}
        for version in version_list:
            for course in course_list:
                for topic in topic_type_list:
                    cur_url = base_url.format(str(version), str(course), str(topic), '1')




        pass


if __name__ == "__main__":
    obj = TiKuSpider("https://www.tiku.cn/index/index/questions.html", logger=)
    obj.main()


