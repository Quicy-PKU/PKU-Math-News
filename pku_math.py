try:
    import requests
    import pickle
    import time
    import re
    home_path = ''  # 代码运行目录
    bark_key = ''  # Bark key

    # 如没有此文件，可将 all_pages 设置为一个空 set，并存储到本地上
    file_path = 'pku_math.pkl'  # 保存已经发布的新闻的 id，格式为 set
    with open(home_path + file_path, 'rb') as f:
        all_pages = pickle.load(f)
        
    urls = [
        'http://portal.math.pku.edu.cn/htdocs/showmodule.php?class=class=1&title=%E5%AD%A6%E9%99%A2%E9%80%9A%E7%9F%A5',  # 学院通知
        'http://portal.math.pku.edu.cn/htdocs/showmodule.php?class=class=5&title=%E6%95%99%E5%8A%A1%E4%BF%A1%E6%81%AF',  # 教务信息
        'http://portal.math.pku.edu.cn/htdocs/showmodule.php?class=class=22%20or%20class=23%20or%20class=13&title=%E5%AD%A6%E9%99%A2%E5%88%B6%E5%BA%A6%E5%8F%8A%E8%A7%84%E5%AE%9A',  # 学院制度及规定
        'http://portal.math.pku.edu.cn/htdocs/showmodule.php?class=class=7&title=%E5%AD%A6%E7%94%9F%E5%9B%AD%E5%9C%B0'  # 学生园地
    ]
    url_prefix = 'http://portal.math.pku.edu.cn/htdocs/showarticle.php?id='

    new_info = []
    for i in range(4):
        text=requests.get(urls[i]).text
        pattern = re.compile(u'<a href=".*?id=(.+?)&.*?"><div class="module_line"><div class="module_item">(.+?)<')
        results = pattern.findall(text)
        for item in results:
            title = item[1]
            href = item[0]
            if title is not None and href is not None and href not in all_pages:
                all_pages.add(href)
                new_info.append((title, url_prefix+href))
        time.sleep(3)

    # 通过 Bark 推送新闻
    for item in new_info:
        requests.get(f'https://api.day.app/{bark_key}/%E6%95%B0%E9%99%A2%E6%96%B0%E9%97%BB%E6%8E%A8%E9%80%81/{item[0]}?url={item[1]}&level=timeSensitive')
        time.sleep(3)

    with open(home_path + file_path, 'wb') as f:
        pickle.dump(all_pages, f, -1)

    import datetime
    print(datetime.datetime.now())
    print('End of the run')

except Exception as e:
    import datetime
    print(datetime.datetime.now())
    print(e)