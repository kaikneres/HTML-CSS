eQuadrado = False;

lado1 =input("Informe o valor primeiro lado:")
lado2 =input("Informe o valor segundo lado :")
lado3 =input("Informe o valor terceiro lado:")
lado4 =input("Informe o valor do último lado:")

if(lado1==lado2==lado3==lado4):
  eQuadrado = True
if(eQuadrado):
    print("O retângulo informado é um quadrado")
if(not eQuadrado):
   print("O retângulo informado NÃO é um quadrado")
