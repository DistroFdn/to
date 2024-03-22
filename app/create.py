import markdown
import initer
import os
import json
from markdown.extensions.toc import TocExtension

User=None
conf_path = None
if os.name == "nt":
    conf_path = str(initer.Whoami()) + '\\to.conf'
else:
    conf_path = str(initer.Whoami()) + '/.local/share/to.conf'
with open(conf_path, 'r') as fli:
    fli = json.load(fli)
    User = str(fli['username'])

text =f'''
# {User} Tasks
'''
HederText = markdown.markdown(text, extensions=[TocExtension(baselevel=3)])

repo_path = None
READMEfile = None
if os.name == "nt":
    repo_path = str(initer.Whoami()) + '\\PathReadme.conf'
else:
    repo_path = str(initer.Whoami()) + '/.local/share/PathReadme.conf'

with open(repo_path, 'r') as read:
    read = json.load(read)
    READMEfile = str(read['PathFileRepo'])


with open(".to", "r", encoding="utf-8") as input_file:
    text = input_file.read()

html = markdown.markdown(text)

hich = markdown.markdown(html, extensions=['nl2br'])


with open(READMEfile, "w", encoding="utf-8") as input_file:
    input_file.write(HederText)
    input_file.write("\n")
    input_file.write("\n")
    input_file.write("```bash")
    input_file.write("\n")
    input_file.write(hich)
    input_file.write("\n")
    input_file.write("```")
