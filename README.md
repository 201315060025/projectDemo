
## 2022-5-8
###增加爬虫代码
| 标题         | 内容 |
| ----------- | ----------- |
| 目录      |    AdilCrawler/spiderGuJi    |
| 数据源1   | [中国哲学书电子化计划](https://ctext.org/zhs)  |
| 数据源2   | [古诗词](https://so.gushiwen.cn/guwen/s)  |
| 数据源3   | [诗词](https://gj.zdic.net/list.php?caid=47)  |

## 2022-07-11
* docker 练习
  * redis 打包
  * mysql 打包
  * flask项目打包

## 多进程读取数据库中的某一个数并修改
目的：查看每个进程读取的数据是不是一行的？
思路：
  * 创建一张数据库表， 有一个字段mum， 当前值是0
  * 使用orm 关系对象模型， SQLAlearn 把关系表映射出来
  * 单个程序能够嗲偶用成功
  * 优化：使用多进程
  
