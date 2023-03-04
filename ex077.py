import re

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for paulavras in palavras:
    paulav = re.sub('[^aeiou]', " ", paulavras)
    print(f'na palavra {paulavras}, temos {paulav}')