import newspaper
import os

def append_to_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text)

path=os.getcwd()


url = 'https://expresso.pt/'

exp = newspaper.build(url)                                                                                                                      

print(exp.size())

for article in exp.articles:
    
    ar = newspaper.Article(article.url)
    ar.download()
    ar.parse()
    
    ar.publish_date = ar.publish_date.strftime("%Y_%m_%d")
    if not os.path.exists(f"{path}/artigos/{ar.publish_date}"):
        os.makedirs(f"{path}/artigos/{ar.publish_date}")
    append_to_file(f'{path}/artigos/{ar.publish_date}/{ar.title}.xml',f'''
<article>
    <title>{ar.title}</title>
    <url>{article.url}</url>
    <autor>{ar.authors}</autor>
    <data>{ar.publish_date}</data>
    <text>{ar.text}</text>
</article>
    ''')