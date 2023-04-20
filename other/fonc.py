def transform_title(title):
    tmp_title = ""
    k = 0
    t = ""
    while t != "—":
        t = title[k]
        if t == " ":
            t = "_"
        elif t == ".":
            t = ""
        tmp_title = tmp_title + t
        k += 1
    title = ""
    for j in range(len(tmp_title) - 2):
        title = title + tmp_title[j]
    return title


def remove_wiki(title):
    j = 0
    new_title = ""
    for i in range(len(title)):
        if j == 2:
            new_title += title[i]
        if title[i] == '/':
            j += 1
    return new_title


def md_to_csv(md):
    links = []

    guille = 0
    link = ""
    for i in range(len(md) - 1):
        if md[i] == '"':
            guille += 1
        if guille == 1:
            if md[i] != '"':
                link = link + md[i]
        if guille == 2:
            links.append(link)
            guille = 0
            link = ""
        i += 1
    print(links)
    return links


def create_csv(title, case):
    csv = title
    for c in case:
        csv += "," + c
    return csv


def contain_point(link):
    for l in link:
        if l == ":":
            return True
    return False
