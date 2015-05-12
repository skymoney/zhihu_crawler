# zhihu_crawler
simple crawler to crawl data from zhihu

ID|版本|修改者|修改时间
--|--:|--:|--
1|1.0|Cheng|2015-04-21

First, use native python without any spyder frames such as scrapy.

##Native crawler
使用原始python进行网页抓取

1，访问登录页面，模拟登录获取cookie
2，给定种子页(seed url)，开始抓取
3，访问每个页面后，提取出后续页面，放到队列中
4，队列可以直接内存中维护，可以mq服务，目前通过
一个sheduler维护一个队列

数据存储：

1，设为两类数据，question&answer
2，question

    * q_id
    * title
    * content
    * author
    * answers（OneToMany）

3， answer

    * a_id
    * author
    * votes
    * content
    * last_modify_date

4, 对于问题和回答的评论暂不记录，全网页另外保存

5, 根据url分为几类，
    
    * /explore  explore
    * /topics  topic
    *
    * /question/123456   question
    * /question/123456/answer/123456 answer
    * /people/abc      people
    * more update

6, 提取url后，去重后每个有效url生成一个URL对象，包含该url和url类型，
    URL对象放到维护的队列里。

7，爬取时，每次取得一个URL对象，根据url类型，分配到不同的爬虫处理中。

8，对于爬去得到的结构数据，包括question和answer，持久化。

9，得到的结构数据传入到pipe中，pipe定义操作

10，
