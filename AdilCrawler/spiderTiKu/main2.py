# coding: utf-8
"""
爬取题库的试题
https://www.tiku.cn/index/index/questions.html?cid=14&cno=1&vid=800023&typeid=600126
"""
import logging, os, sys, pandas as pd, random, time, json
sys.path.append(os.getcwd())
from parse_html import ParseHtml

# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%Y-%d-%m %H:%M:%S"
#
# logging.basicConfig(filename='test.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)
rf_handler = logging.StreamHandler(sys.stderr)  # 默认是sys.stderr
rf_handler.setLevel(logging.INFO)
# rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.INFO)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)


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
        return topic_type

    def get_analysis(self):
        """获取解析答案"""
        self.parser.get_answer_detail()
        pass

    def get_content_by_page(self, url):
        """获取详情"""
        # url = "https://www.tiku.cn/index/index/questions.html?cid=14&cno=1&vid=800016&bid=801013&typeid=600126"
        detail_list = self.parser.get_detail_list(url)
        detail_data_list = []
        for detail_one in detail_list:
            detail_data_list.append(self.parser.get_detail_by_one(detail_one))
        return detail_data_list

    def get_page_list(self, url) -> int:
        """获取总共有多少页"""
        return self.parser.get_page(url)



    def main(self):
        """"""
        base_url = "https://www.tiku.cn/index/index/questions.html?cid=14&cno=1&vid={}&bid={}&typeid={}"
        # 获取不同类型的版本
        version_list = self.get_version_list()
        self.logger.info("版本信息：")
        self.logger.info(version_list)
        # 获取不同的课本
        course_list = self.get_course_list()
        self.logger.info("课程信息：")
        self.logger.info(course_list)
        topic_type_list = self.get_topic_type()
        self.logger.info("题目类型：")
        self.logger.info(topic_type_list)

        """
        {'edition':'人教版','book':'三年级上册','level':'0.72', 'original_text':'小明为玉树灾区的小朋友捐了55本故事书，46本连环画，一共是多少本书?','ans':'','resolution':'55+46=101(本)' ,'analysis':''}
        """
        # step1:
        """
        基本url, 最大页码数目，版本， book， 
        """
        step_result = []
        version_list = []
        for version in version_list:
            v_id, v_name = version["vid"], version["name"]
            for course in course_list:
                c_id, c_name = course["bid"], course["name"]
                for topic in topic_type_list:
                    t_id, t_name = topic["typeid"], topic["name"]
                    cur_url = base_url.format(str(v_id), str(c_id), str(t_id))
                    self.logger.info("start: " + cur_url)
                    page_num = self.get_page_list(cur_url)
                    step_result.append({
                        "v_id": v_id,
                        'v_name': v_name,
                        "c_id": c_id,
                        "c_name": c_name,
                        't_id': t_id,
                        "t_name": t_name,
                        "max_page": page_num,
                        "url": cur_url
                    })
        # print(step_result)
        # 把第一步结果保存保存
        # df = pd.DataFrame(data=step_result)
        # df.to_csv("step_result.csv", index=False)
        df = pd.read_csv("step_result.csv")
        cl_list = df.columns.tolist()
        data_list = df.values.tolist()
        step_result = [dict(zip(cl_list, i)) for i in data_list]

        # step 2
        """
        基础url ,页码数字（1， 2），  
        """
        step2_result_ff = "step2_result.csv"
        if os.path.exists(step2_result_ff):
            his_df = pd.read_csv(step2_result_ff)
        else:
            his_df = pd.DataFrame({"page": [], "base_url": [], "cur_url": [], "page_context": []})
        history_cur_url_list = list(his_df["cur_url"])
        step2_result = []
        number = 0
        for stp in step_result:
            max_page, base_url = stp["max_page"], stp["url"]
            for cur_page in range(1, max_page+1):
                cur_url = base_url + "&page=" + str(cur_page)
                if cur_url not in history_cur_url_list:
                    self.logger.info("{} 已经存在".format(cur_url))
                    continue
                cur_result = self.get_content_by_page(cur_url)
                if len(cur_result) == 0:
                    self.logger.error("请求被拒绝， 获取数据为空")
                    continue
                number += 1
                self.logger.info("{} 当前url:{}, 获取结果：{} ".format(str(number), cur_url, len(cur_result)))
                step2_result.append({
                    "page": cur_page,
                    "base_url": base_url,
                    "cur_url": cur_url,
                    "page_context": json.dumps(cur_result)
                })
                # 获取所有也内容
                time.sleep(random.random())
                df = pd.DataFrame(data=step2_result)
                mode = "a" if len(history_cur_url_list) == 0 else 'w'
                df.to_csv("step2_result.csv", mode=mode, index=False)


if __name__ == "__main__":
    parse = ParseHtml(logger=logger)
    obj = TiKuSpider("https://www.tiku.cn/index/index/questions.html", logger=logger, parser=parse)
    obj.main()


