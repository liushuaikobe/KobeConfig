import webbrowser

urls = [
    'http://www.douban.com',
    'http://weibo.com',
    'http://www.zhihu.com',
    'http://www.v2ex.com/',
    'https://github.com/',
    'https://mail.google.com/',
    'http://instagram.com/',
    'http://stackoverflow.com/users/1108052/liushuaikobe'
]

map(lambda x: webbrowser.open(x), urls)
