import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://ge.globo.com/')
except urllib.error.URLError:
    print(f'Não foi possivel acessar o Site {"https://ge.globo.com/"} no momento')
else:
    print('Site acessado com sucesso!')
