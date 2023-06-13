

"""
create table tmp_table(
    number int
)
"""

from multiprocessing import Pool
from threading import Thread
from concurrent.futures import ThreadPoolExecutor, as_completed

import os
from model import session, Users

def func():
    # pid = os.getpid()
    print("end func")
    pid = "1"

    record = session.query(Users).filter(Users.name == 'test').first()
    #
    # print("查询")
    # number = record.number
    # print("pid: {}, current number: {}, update number: {}".format(pid, number, number+1))
    # session.query(Users).filter(Users.name == 'test').update({Users.number: Users.number+1})
    # print("更新")
    # session.commit()
    return 1
    pass


def main2():
    pool = Pool(3)
    res_list = []
    for i in range(3):
        res_list.append(pool.apply_async(func, args=()))
    pool.close()
    pool.join()
    for res in res_list:
        print("res", res.get())

def main():
    print("start")
    with ThreadPoolExecutor(3) as thexe:
        obj_list = []
        for i in range(3):
            print("thread", i)
            obj_list.append(thexe.submit(func, ))
        print("2", obj_list)
        for i in as_completed(obj_list):
            print("i", i.result())
        print("end")
    # thexe = ThreadPoolExecutor(3)
    # obj_list = []
    # for i in range(3):
    #     print("thread", i)
    #     obj_list.append(thexe.submit(func,))
    # print("2")
    # for i in as_completed(obj_list):
    #     print("i", i)
    # print("end")





if __name__ == '__main__':
    main()




