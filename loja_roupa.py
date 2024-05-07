valor_unitario =12.5 
quantidades = int (input ("quantidade de camisas :"))
valor_total= valor_unitario * quantidades
if quantidades <= 5 : 
    valor_total= valor_total *0.97 
else:
    if quantidades <=  10:
        valor_total= valor_total *0.95
    else:
        valor_total = valor_total *0.93 
print(f" valor total:R$ {valor_total:.02f}")