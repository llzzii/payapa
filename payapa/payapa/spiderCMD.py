# 此脚本是爬虫启动脚本(不用去cmd输入命令)

from scrapy.cmdline import execute


class SpiderCMD():

    def createSpider(obj):
        execute(['scrapy', 'crawl', 'jobspider',
                 '-a', 'start_urls=https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare= ',
                 '-a', 'taskid='+str(taskId)])

# result,taskId = td.create(('Java职位数据采集','https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='))
#
# if result>0:
#     execute(['scrapy','crawl','jobspider',
#              '-a','start_urls=https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
#              '-a','taskid='+str(taskId)])


# result,taskId = td.create(('C++职位数据采集','https://search.51job.com/list/000000,000000,0000,00,9,99,c%252B%252B,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='))
# if result>0:
#     execute(['scrapy','crawl','jobspider',
#              '-a','start_urls=https://search.51job.com/list/000000,000000,0000,00,9,99,c%252B%252B,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
#              '-a','taskid='+str(taskId)])

# result,taskId = td.create(('js职位数据采集','https://search.51job.com/list/000000,000000,0000,00,9,99,js,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='))
#
# if result>0:
#     execute(['scrapy','crawl','jobspider',
#              '-a','start_urls=https://search.51job.com/list/000000,000000,0000,00,9,99,js,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
#              '-a','taskid='+str(taskId)])


# result,taskId = td.create(('php职位数据采集','https://search.51job.com/list/000000,000000,0000,00,9,99,php,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='))
#
# if result>0:
#     execute(['scrapy','crawl','jobspider',
#              '-a','start_urls=https://search.51job.com/list/000000,000000,0000,00,9,99,php,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
#              '-a','taskid='+str(taskId)])
