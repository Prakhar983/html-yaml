from bs4 import BeautifulSoup
import yaml
from collections import OrderedDict

with open('Prak EnTech Homepage.htm', 'r', encoding='utf-8') as f:html_content = f.read()
soup = BeautifulSoup(html_content, 'html.parser')

dictionary=OrderedDict()

def style(st):
    dit = {}
    st = st.split(";")
    for i in range(len(st)):
        st[i] = st[i].split(":")
        dit[st[i][0]] = st[i][1]
    return dit

def checktags(tag):
    for i in dictionary:
        for j in dictionary[i]["children"]:
            if j == tag.get("id"):
                return (True,dictionary[i]['children'][j])
    return (False,None)

# def traverse_dict(tagid,tag):
#     for key, value in dictionary.items():
#         if key==tagid:
#             dictionary[key]["children"] = children(tag)
#         if isinstance(value, dict):
#             try:traverse_dict(tagid,tag)
#             except:return

def children(tag2):
    dit2 = {}
    for tag in soup.find_all():
        if tag.parent==tag2:
            try:
                dit2[tag['id']]={}
                try:
                    dit2[tag['id']]['css']=style(tag['style'])
                except:
                    dit2[tag['id']]['css']=""
                try:
                    if tag.name=="span":dit2[tag['id']]['type']="text"
                    else:dit2[tag['id']]['type']=tag.name
                except:
                    dit2[tag['id']]['type']=""
                try:
                    dit2[tag['id']]['classname']=tag['class'][0]
                except:
                    dit2[tag['id']]['classname']=""
            except:pass
    return dit2

for k in range(3):
    for tag in soup.find_all():
        if not checktags(tag)[0]:
            try:
                try:
                    dictionary[tag['id']]={}
                    dictionary[tag['id']]['children'] = children(tag)
                    try:
                        dictionary[tag['id']]['css']=style(tag['style'])
                    except:
                        dictionary[tag['id']]['css']=""
                    try:
                        dictionary[tag['id']]['type']=tag.name
                    except:
                        dictionary[tag['id']]['type']=""
                    try:
                        dictionary[tag['id']]['classname']=tag['class'][0]
                    except:
                        dictionary[tag['id']]['classname']=""
                except:pass
            except:pass

        if checktags(tag)[0]:
            dictchild = children(tag)
            checktags(tag)[1]['children'] = dictchild
        # traverse_dict(tag.get('id'),tag)
yaml_data = yaml.dump(dictionary, default_flow_style=False)
yaml_data=yaml_data[yaml_data.index('\n')+1:]

with open('template.yaml', 'w') as f:f.write(yaml_data)
    

    # for child in tag.findChildren():
    #     print(f"Parent Tag: {tag.name}, Child Tag: {child.name}")

# from bs4 import BeautifulSoup
# import yaml

# with open('Prak EnTech Homepage.htm', 'r', encoding='utf-8') as f:html_content = f.read()
# # print(html_content)
# soup = BeautifulSoup(html_content, 'html.parser')

# html_tags = {}

# for tag in soup.find_all(recursive=True):
#     tag_name = tag.name
#     if((tag_name in ('link','meta'))==False):
#         if tag_name not in html_tags:html_tags[tag_name] = []
#         tag_attributes = {}
#         for attr in tag.attrs:tag_attributes[attr] = tag[attr]
#         html_tags[tag_name].append(tag_attributes)

# yaml_data = yaml.dump(html_tags, default_flow_style=False)

# with open('output.yaml', 'w') as f:
#     f.write(yaml_data)