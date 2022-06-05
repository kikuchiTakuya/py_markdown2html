import markdown

# 必要ファイルの読み込み
with open('./template/doctype.html', 'r', encoding='utf-8') as doc:
    doc_file = doc.read()
html = doc_file +'\n'

with open('./template/head.html', 'r', encoding='utf-8') as head:
    head_file = head.read()
html += '<head>' + head_file + '\n' 
html += '<link rel="stylesheet" href='+ './template/py_markdown.css' + '>'
html += '</head>' + '\n'

# マークダウン読み込み
with open('test.md', 'r', encoding='utf-8') as input_file:
    read_file = input_file.read()
# マークダウンをhtmlに変換
html += '<body>\n' + markdown.markdown(read_file) + '\n</body>\n'

# </html>挿入
html += '</html>'

# htmlをhtmlファイルに書き込み
with open('test.html', 'w', encoding='utf-8', errors='xmlcharrefreplace') as output_file:
    output_file.write(html)