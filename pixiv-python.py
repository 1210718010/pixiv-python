from flask import Flask
from bs4 import BeautifulSoup
import requests
import json

headers = {
    "cookie": "",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "referer": "https://www.pixiv.net/"
}

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET', 'POST'])
def image(path):
    if '-' in path and '.' in path:
        pid = path.split('-')[0]
        pNum = path.split('-')[1].split('.')[0]
        fileEx = path.split('-')[1].split('.')[1]
    elif '-' in path:
        pid = path.split('-')[0]
        pNum = path.split('-')[1]
    elif '.' in path:
        pid = path.split('.')[0]
        fileEx = path.split('.')[1]
    else:
        pid = path

    requests.packages.urllib3.disable_warnings()
    response = requests.get(f"https://www.pixiv.net/artworks/{pid}", headers=headers, verify=False)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find('meta', id='meta-preload-data')

    jsonData = links.get('content')
    content = json.loads(jsonData)
    illust = content['illust'][f'{pid}']['urls']
    url = illust['original'].replace("i.pximg.net", "i.muxmus.com:5000")

    if 'pNum' in locals().keys() and 'fileEx' in locals().keys():
        url = url.replace('_p0.', f'_p{pNum}.')
        url = url.rsplit('.', 1)[0] + f'.{fileEx}'
    elif 'pNum' in locals().keys():
        url = url.replace('_p0.', f'_p{pNum}.')
    elif 'fileEx' in locals().keys():
        url = url.rsplit('.', 1)[0] + f'.{fileEx}'

    return f"<script>window.location.href='{url}'</script>"

if __name__ == '__main__':
    app.run(port=7000)