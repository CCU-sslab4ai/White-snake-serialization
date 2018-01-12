import re
import json

f = open('./raw.txt', encoding='utf8')
a = f.readlines()

total = []
chapter = 1
nowCh = None

for i in a:
    result = re.search(r'第.*?場:(.*)]', i)
    if result:
        if nowCh is not None:
            total.append(nowCh)
        nowCh = {
            "chapter": chapter,
            "title": result.groups()[0],
            "contents": []
        }
        chapter+=1
        continue
    result = re.search(r'(.*?):(.*)', i)
    if result:
        content = {
            "speaker": result.groups()[0],
            "content": result.groups()[1]
        }
        nowCh["contents"].append(content)

total.append(nowCh)

f.close()

f = open('result.json', mode='w', encoding='utf-8')
f.write(json.dumps(total, ensure_ascii=False))
f.close()
