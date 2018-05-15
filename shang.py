# coding:utf-8
import requests
import pymssql
import sys
from bs4 import BeautifulSoup
import  time
def inquery(comp ,pos ,ad,ed ,ex ,l,h ,av,cm):

      conn=psycopg2.connect(database="whc_first", user="sa",password="wjnQG976WL", host="LAPTOP-3UQ4BV68")
      if(conn==False):
          print("连接数据库失败,退出程序")
          exit()
      cur=conn.cursor()
      '''if( cur.execute("CREATE TABLE myanalyse (company CHAR(30),position CHAR(30),adr CHAR(30),edu CHAR(10),exp INT,\
                         lowmoney INT,highmoney INT,avermoney INT,curmon INT )") ):#,unique(company ,position ,adr ,edu ,exp ,lowmoney,highmoney ,avermoney,curmon)
          print("建表成功")'''

      try:
          cur.execute("INSERT INTO myanalyse(company ,position ,adr ,edu ,exp ,lowmoney,highmoney ,avermoney,curmon) \
                                           values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",\
                                           (comp ,pos ,ad,ed ,int(ex) ,int(l),int(h) ,int(av),int(cm)))
      except:
          {}
      conn.commit()
      cur.close()
      conn.close()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
proxies = {
  "http": "http://101.73.56.207",   "https": "http://60.13.74.211",   "https": "http://222.209.185.148","https": "http://125.85.164.106",
  "https": "http://125.69.28.143",  "https": "http://111.120.216.231","https": "http://111.120.25.181", "https": "http://111.120.217.173",
  "https": "http://116.226.136.135","https": "http://111.76.129.158", "https": "http://111.76.133.74",  "https": "http://1.31.43.123",
  "https": "http://182.120.51.106","https": "http://115.49.111.20",   "https": "http://36.249.192.240",  "https": "183.190.38.50",

}
def get(urls):
    n=1
    while (n< 176):
        time.sleep(6)
        print("******************************************************************************第%d页**********************************************************************************" % (n))
        try:
            #urls =u"http://www.chinahr.com/sou/?orderField=relate&keyword=Java+Python+PHP+.NET+C%23+C%2B%2B+C+Delphi+Perl+Ruby+Hadoop+Node.js+MySQL+SQLServer&city=398&refreshTime=5&page="
            url=urls+str(n)
            print(n)
            n=n+1
            response = requests.get(url,headers=headers)#,proxies=proxies)
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            positions= soup.find_all('li', class_="l1")
            companys=soup.find_all('li', class_="l1")
            adresses=soup.find_all('li',class_='l2')
            moneys=soup.find_all('li',class_='l2')
            i=0
            while( i < len(positions) ):
                position =positions[i].find('span', class_="e1").text.replace(" ",'')
                company=companys[i].find('span', class_="e3").text.replace("\n",'').replace(" ",'')
                adrexp=adresses[i].find('span', class_="e1")
                money = moneys[i].find('span', class_="e2")#薪资
                adr=adrexp.text.split("[")[1].split("]")[0].split("/")[0].replace(" ",'')#工作地址
                exp=adrexp.text.split("[")[1].split("]")[1].replace("\r\n\t\t\t\t\t\t\t",'').split("/")[0].replace(" ",'').replace("年",'').replace("应届生",'0')#经验
                edu=adrexp.text.split("[")[1].split("]")[1].replace("\r\n\t\t\t\t\t\t\t", '').split("/")[1].replace(" ",'')#学历
                lowmoney=money.text.split("-")[0].replace("面议",'0')
                higmony=money.text.split("-")[1].replace("面议",'0')
                avermoney=(int(lowmoney)+int(higmony))/2
                print("公司:  "+company)
                print("职位:  "+position)
                print("工作地点:  "+adr)
                print("学历:  "+edu)
                print("经验:  " + exp)
                print("工资下限:  "+lowmoney)
                print("工资上限:  "+higmony)
                print("平均工资： "+str(int(avermoney)))
                inquery(company, position, adr, edu, exp, lowmoney, higmony, avermoney,3)
                print("************************我是分隔符***********************")
                i = i + 1

        except:
             continue
#inquery("123","123","123","123","123","123","123","123","123")
             u"http://www.chinahr.com/sou/?orderField=relate&keyword=Java+Python+PHP+.NET+C%23+C%2B%2B+C+Delphi+Perl+Ruby+Hadoop+Node.js+MySQL+SQLServer&city=398&industrys=1100&refreshTime=1&page=3"

beijingurls =u"http://www.chinahr.com/sou/?orderField=relate&keyword=Java+Python+PHP+.NET+C%23+C%2B%2B+C+Delphi+Perl+Ruby+Hadoop+Node.js+MySQL+SQLServer&city=398&refreshTime=5&page="
shanghaiurls = u"http://www.chinahr.com/sou/?orderField=relate&keyword=Java+Python+PHP+.NET+C%23+C%2B%2B+C+Delphi+Perl+Ruby+Hadoop+Node.js+MySQL+SQLServer&city=400&refreshTime=5&page="
hangzhouurls = u"http://www.chinahr.com/sou/?orderField=relate&keyword=Java+Python+PHP+.NET+C%23+C%2B%2B+C+Delphi+Perl+Ruby+Hadoop+Node.js+MySQL+SQLServer&city=182&refreshTime=5&page="
guangzhouurls = u"http://www.chinahr.com/sou/?orderField=relate&keyword=Java+Python+PHP+.NET+C%23+C%2B%2B+C+Delphi+Perl+Ruby+Hadoop+Node.js+MySQL+SQLServer&city=291&refreshTime=5&page="
shenzhenurls = u"http://www.chinahr.com/sou/?orderField=relate&keyword=Java+Python+PHP+.NET+C%23+C%2B%2B+C+Delphi+Perl+Ruby+Hadoop+Node.js+MySQL+SQLServer&city=292&refreshTime=5&page="
chengduurls = u"http://www.chinahr.com/sou/?orderField=relate&keyword=Java+Python+PHP+.NET+C%23+C%2B%2B+C+Delphi+Perl+Ruby+Hadoop+Node.js+MySQL+SQLServer&city=312&refreshTime=5&page="

get(beijingurls)
get(shanghaiurls)
get(hangzhouurls)
get(guangzhouurls)
get(shenzhenurls)
get(chengduurls)

