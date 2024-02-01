from bs4 import BeautifulSoup
import yaml

with open('Prak EnTech Homepage.htm', 'r', encoding='utf-8') as f:html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')
html_data = []

tags = soup.find_all()
for tag in tags:
    tag_info = {}
    tag_info['tag_name'] = tag.name
    if tag.string and tag.string.strip():tag_info['text_content'] = tag.string.strip()
    if tag.name == 'img' and 'src' in tag.attrs:tag_info['image_src'] = tag['src']
    html_data.append(tag_info)

yaml_data = yaml.dump(html_data, default_flow_style=False)

with open('output2.yaml', 'w') as f:
    f.write(yaml_data)