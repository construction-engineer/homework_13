import json
import pprint


def data_load(link):
    with open(link, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    return data


def get_tags(data):
    results = set()

    for post in data:
        content = post['content']
        words = content.split()
        for word in words:
            if word.startswith('#'):
                results.add(word[1:])
    return results


def get_posts_by_tag(data, tag):
    results = []
    for post in data:
        if f'#{tag}' in post['content']:
            results.append(post)
    return results


def add_post(link, post):
    data = data_load(link)
    data.append(post)
    with open(link, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4, sort_keys=True)