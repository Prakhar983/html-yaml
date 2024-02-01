from bs4 import BeautifulSoup
import yaml

with open('Prak EnTech Homepage.htm', 'r', encoding='utf-8') as f:html_content = f.read()
# print(html_content)
soup = BeautifulSoup(html_content, 'html.parser')

html_tags = {}

for tag in soup.find_all(recursive=True):
    tag_name = tag.name
    if((tag_name in ('link','meta'))==False):
        if tag_name not in html_tags:html_tags[tag_name] = []
        tag_attributes = {}
        for attr in tag.attrs:tag_attributes[attr] = tag[attr]
        html_tags[tag_name].append(tag_attributes)

yaml_data = yaml.dump(html_tags, default_flow_style=False)

with open('output.yaml', 'w') as f:
    f.write(yaml_data)