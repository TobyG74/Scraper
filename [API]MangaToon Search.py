tobz = url.find('div', class_='recommend-item')
title = tobz.find('div', class_='recommend-comics-title').text.replace('\n                ','').replace('              ','')
link = "https://mangatoon.mobi" + tobz.a['href']
genre = tobz.find('div', class_='comics-type').text.replace('\n                ','').replace('/',', ').replace('             ','')
info = bsoup(link)
star = info.find('div', class_='star').text.replace('\n\n        ','').replace('      ','/5')
information = info.find('div', class_='icon-wrap').text.replace('\n\n      ','').replace('      views','views').replace('      \n      ','\n').replace('      likes      \n','likes\n').replace('     \n','').replace('    ','')
description = info.find('div', class_='description').text.replace('\n      ','')
data.append({"title":title,"link":link,"genre":genre,"star":star,"information":information,"description":description})