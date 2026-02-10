import os
import requests as req

urlhtml = 'https://itakea.github.io/e24_swa/py_intro_3.html'
res = req.get(urlhtml)
html = res.text

urlcss = 'https://itakea.github.io/e24_swa/_static/css/custom.css?v=a5898925'
res = req.get(urlcss)
css = res.text


# DIRECTORY
os.mkdir('mappe')
os.chdir('mappe')

# HTML
with open('index.html','w', encoding='utf-8') as f:
    f.write(html)


# CSS
with open('style.css','w', encoding='utf-8') as f:
    f.write(css)


# Scriptet mangler at ændre stylesheet path så det virker med den hentede css

# Open file 
os.startfile('index.html')
