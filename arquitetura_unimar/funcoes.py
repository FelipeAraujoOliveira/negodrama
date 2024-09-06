from unidecode import unidecode

def menu():
  soma_final= []
  print("""Bem vindo à inscrição para o vestibular da UNIMAR

Precisarei de algumas informações para computar e verificar se é válida sua inscrição
""")

def converter_cpf(cpf1):
  cpf_convertido = []
  while True:
    cpf1 = input("")
    if len(cpf1) < 11 or len(cpf1) > 11:
      print("CPF invalido, Tente Novamente")
    else:
     break
  i = 0
  for number in cpf1:
    if i == 2 or i == 5:
      cpf_convertido.append(number)
      cpf_convertido.append('.')
    elif i == 8: 
      cpf_convertido.append(number)
      cpf_convertido.append('-')
    else:
      cpf_convertido.append(number)
    i += 1
    cpf_convertido = ''.join(cpf_convertido)
    return cpf_convertido

def genero():
  while True:
    print("Qual seu sexo biologico? ")
    sexo = input("(F/M) ").lower()
    if sexo == "f" or sexo == "m":
      return sexo
    else:
      print("Não entendi, Tente Novamente")

def nome():
  print("")
  print("Preciso de seu nome completo: ")
  while True:
    nome2 = input("")
    if valida_vazio(nome2):
      print("Por favor, Digite seu nome")
    else:
      
      return nome2
    
  

def idade():
  print("")
  print("Agora por favor sua idade: ")
  while True:
     try:
       idade1 = int(input("Exemplo:(18) "))
       if idade1 < 15 or idade1 > 100:
         raise ValueError()
       return idade1
     except ValueError:
      print("Seu numero não foi validado, verifique se tem a idade minima necessaria para fazer o vestibular")

def raca():
  print("")
  print("Por favor, me informe sua raça")
  while True:
    racas  = ["negro", "branco", "amarelo", "indigena"]
    raca1 = unidecode(input("(Negro/Branco/Amarelo/Indigena)").lower())
    if raca1 in racas:
      return raca1
    else:
      print("Não entendi, Tente novamente")

def cpf():
  print("")
  print("Legal, Agora preciso de seu CPF")
  converter_cpf(cpf)
  print("")

def endereço():
  print("Agora, preciso de seu endereço""")
  while True:
    endereço1 = input("Exemplo: Av: Higino Muzi filho ")
    if valida_vazio(endereço1):
      print("Não entendi, Tente novamente")
    else:
      break
  numero_endereço = (input("Numero: "))
  while True:
    if valida_vazio(numero_endereço):
      print("Não entendi, Tente novamente")
    else:
      break

def converter_cep(cep):
  cep_convertido = []
  while True:
    cep = input("")
    if len(cep) < 8 or len(cep) > 8:
      print("CEP invalido, Tente Novamente")
    else:
      break
  i = 0
  for number in cep:
    if i == 2 or i == 5:
      print(number + '.',end = "")
  i += 1
  
def cep():
  print("")
  print("Agora, por favor confirme seu CEP")
  while True:
     try:
       converter_cep(cep)
       break
     except ValueError:
       print("Não consigui Achar seu ddd, tente novamente")

def telefone():
  print("Primeiramente, Seu ddd: ")
  while True:
     try:
       ddd = int(input(""))
       if ddd <= 0 or ddd > 100:
        raise ValueError()
       with open('usuarios.txt', 'a+') as arquivo:
        arquivo.write(f"{ddd}")
       break
     except ValueError:
       print("Não consigui Achar seu ddd, tente novamente")
  print("Seu numero agora: ")
  while True:
     try:
       telefone = int(input(""))
       if telefone < 90000000 or telefone > 999999999:
         raise ValueError()
       with open('usuarios.txt', 'a+') as arquivo:
        arquivo.write(f"{telefone}")
       break
     except ValueError:
       print("Não consigui Achar seu numero, tente novamente")

def email():
   print("")
   print("Agora Seu Email: ")
   while True:
    email1 = input("Exemplo: unimar@unimar.br ")
    if email1 == None or email1 == "":
      print("Insira um Email")
    else:
      break

def senha():
   print("""
Seu cadastro está quase pronto, só falta criar uma senha para sua conta
Lembre-se, nunca compartilhe essa senha com ninguem

Crie sua senha:
   """)
   while True:   
    senha = input("")
    if len(senha) < 8 or len(senha) > 8:
      print("sua senha deve ter pelo menos 8 Digitos")
    else:
      break

def final_cadastro(sexo,nome2,idade1,raca1,cpf1,endereço1,endereço_numero,cep1,ddd,email1):
   usuario = {"genero": sexo, "nome": nome2, "idade": idade1, "Raça": raca1, "cpf": cpf1, "endereço": endereço1, "numero": endereço_numero, "cep": cep1, "ddd": ddd, "telefone": telefone, "email": email1}
   print("Parabens você foi cadastrado")
   print(f"Aqui estão suas informações {usuario} ")
   print("Releia bem para ver se não ficou algo errado para tras")
   print("Tudo certo?")
   while True:
    a = input("(S/N)").lower()
    if a == "s":
      print("Otimo, Vamos para proxima etapa então")
      break
    elif a == "n":
      print("Ah, tudo bem erros acontecem, Digite pra mim oque você errou")
      caso_nao()
      print("Vamos Continuar? ")
    else:
      print("Não entendi, Está tudo certo?")

def menu2():
  print("Coloque 0 caso seja a primeira escolha")
  print("Coloque 1 caso seja a segunda escolha")
  print("Coloque 2 caso seja a terceira escolha")
  print("Coloque 3 caso seja a quarta escolha")
  print("Coloque 4 caso seja a quinta escolha")

def alter():
  resposta = input("Resposta: ")
  if resposta == "0":
    soma_final.append("0")
    return resposta
  elif resposta == "1":
    soma_final.append("1")
    return
  elif resposta == "2":
    soma_final.append("2")
    return
  elif resposta == "3":
    soma_final.append("3")
    return
  elif resposta == "4":
    soma_final.append("4")
    return
  else:
    print("Resposta não é valida, Tente Novamente")
    alter()

def caso_nao():
  while True:
    nao = input("")
    if nao == "sexo":
      genero()
      break
    if nao == "nome":
      nome()
      break
    if nao == "idade":
      idade()
      break
    if nao == "raça":
      raca()
      break
    if nao == "cpf":
      cpf()
      break
    if nao == "endereço":
      endereço()
      break
    if nao == "cep":
      cep()
      break
    if nao == "telefone":
      telefone()
      break
    if nao == "email":
      email()
      break
    else:
      print("Não entendi, oque esta errado?")

def cadastro():
  menu()
  genero()
  nome()
  idade()
  raca()
  cpf()
  print("Otimo, falta pouco para finalizamos seu cadastro")
  print("")
  endereço()
  cep()
  print("")
  print("Para manter-mos contato caso algo ocorra, escreva seu numero e seu Email")
  print("")
  telefone()
  email()
  senha()
  sexo = genero()
  final_cadastro(sexo,"nome","idade1","raca1","cpf1","endereço1","endereço_numero","cep1","ddd","email1")

def valida_vazio(string):
  if string == "" or string == None or string == " ":
    return True
  else:
    return False