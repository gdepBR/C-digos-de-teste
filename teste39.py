input_n = int(input('digite um número de 1 a 10: '))

if input_n > 10:
    print('numero maior que 10')

elif input_n <= 10:
        
        for n in range(1, 11):
        
            if n % 2 == 0: # "%" = compara se sobrou algo da divisão. se não sobrar = par.
                print(f"{n} -> par")

            else:
                 continue # pula os números impares.

else:
     print('opção inválida')