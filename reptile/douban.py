import requests
import os 
import time
import xlwt
# 用字典来存用户信息
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

# 构造请求URL
urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start={}'.format(str(i)) for i in range(0, 100, 20)]

def get_url_view(urls):
    data = []
    details = []
    for uri in urls:
        result = requests.get(uri, headers).json()
        data += result['subjects']
        time.sleep(2)
    data = sorted(data, key=lambda item : float(item['rate']),reverse=True)
    for item in data:
        id = item['id']
        url = 'https://movie.douban.com/j/subject_abstract?subject_id={}'.format(str(id))
        result = requests.get(url, headers).json()
        print(result)
        details.append(result['subject'])
    print(len(data))
    print(len(details))
    save_excel(data, details)

def save_excel(data, details):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('豆瓣前100的电影')
    sheet.write(0, 0, '电影名称')
    sheet.write(0, 1, '评分')
    sheet.write(0, 2, '演员列表')
    sheet.write(0, 3, '导演')
    sheet.write(0, 4, '产地')
    sheet.write(0, 5, '上映时间')
    sheet.write(0, 6, '类型')
    sheet.write(0, 7, '详情')
    for index in range(len(data)):
        sheet.write(index + 1, 0, data[index]['title'])
        sheet.write(index + 1, 1, data[index]['rate'])
        sheet.write(index + 1, 2, ','.join(details[index]['actors']))
        sheet.write(index + 1, 3, ','.join(details[index]['directors']))
        sheet.write(index + 1, 4, details[index]['region'])
        sheet.write(index + 1, 5, details[index]['release_year'])
        sheet.write(index + 1, 6, ','.join(details[index]['types']))
        sheet.write(index + 1, 7, data[index]['url'])
    if (os.path.exists('豆瓣.xls')):
        os.remove('豆瓣.xls')
        wbk.save('豆瓣.xls')
    else:
        wbk.save('豆瓣.xls')

if __name__ == "__main__":
    try:
        get_url_view(urls)
    except BaseException as e :
        print('爬取失败', e)