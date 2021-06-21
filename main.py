from bs4 import BeautifulSoup, NavigableString


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
