import json
import requests
import time



def test():
    url = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery112403473268296510956_1531502963311&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1531502963313'

    res = requests.get(url)
    json_string = res.text
    json_string = json_string[json_string.find('{'):-2]
    data = json.loads(json_string)
    commen_list = data['results']['parents']
    for comm in commen_list:
        print(comm['name'] + ':' + comm['content'] + '(IP:%s)' % comm['ipAddress'])

# https://www.toutiao.com/api/search/content/?
# aid=24&app_name=web_search&offset=0&
# format=json&keyword=python&autoload=true&count=20&en_qc=1&
# cur_tab=1&from=search_tab&pd=synthesis&timestamp=1554519458678
#
# https://www.toutiao.com/api/search/content/?
# aid=24&app_name=web_search&offset=20&
# format=json&keyword=python&autoload=true&count=20&en_qc=1&
# cur_tab=1&from=search_tab&pd=synthesis&timestamp=1554519548753

def today_news():
    headers = {
       "UserAgent": 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 69.0.3497.100Safari / 537.36'
    }
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}&format=json&keyword=python&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis'

    #print(data['data'][6]['article_url'])
    with open('./toutiao.txt', 'w') as f:
        for i in range(10):
            uri = url.format(str(i * 20))
            print(uri)
            res = requests.get(uri, headers=headers)
            time.sleep(1)
            json_string = res.text
            data = json.loads(json_string)
            for i in data['data']:
                if 'article_url' in i:
                    f.write(i['title'] + ':' + i['article_url'] + '\n')
                    print(i['title'], i['article_url'])



    f.close()








def main():
    today_news()




if __name__ == '__main__':
  main()