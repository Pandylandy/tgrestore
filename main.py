from bs4 import BeautifulSoup, NavigableString
import subprocess


contents = open('ChatExport/messages.html', encoding='utf-8')
soup = BeautifulSoup(contents, 'lxml')


def get_info(content):
    info = []
    for i in content:
        if isinstance(i, NavigableString):
            continue
        info.append(i)
    return info


def has_class_and_id(tag):
    if tag.has_attr('class') and tag.has_attr('id'):
        if 'message' in tag['id'] and 'message' in tag['class'] and 'default' in tag['class']:
            return True
    return False


h = soup.findChild('body').findAll(class_='history')[0]
history = h.find_all(has_class_and_id)
info = get_info(history[0].find(class_='body'))
groups = []
group = []
for n, obj in enumerate(history):
    if n == 10:
        break
    start = False
    print(obj.attrs)
    if 'joined' not in obj.attrs['class']:
        start = True
        print('!')
    if start:
        if len(group):
            groups.append(group)
        group = []
    group.append(get_info(obj.find(class_='body')))

subprocess.run(['ls'], stdout=subprocess.PIPE, universal_newlines=True).stdout.split()

# telegram-cli -W -e "msg User1 1"
