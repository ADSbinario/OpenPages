import time
import webbrowser

# Para pentest que utilizam windows, esse programa facilita na hora da listagem de vários
#subdominios e você ficar abrindo página por página, basta inserir uma lista no arquivo texto.txt
# e os subdominios serão abertos um por um
with open("texto") as f:
  content = f.readlines()
  print(f)

#print(content)
content = [x.strip('\n') for x in content]
#print(content)

for line in content:
    webbrowser.open(line)
    time.sleep(1)
    print(line)
