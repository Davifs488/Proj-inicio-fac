def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
    
    for i,valor in enumerate(Args):
        print(f"posição = {1}, valor = {valor}")
        
        
        print("\nChamada 1")
        imprimir_parametros("São Paulo" , 10 , 23 , 78 ,"João")
        print("\nChamar 2")
        imprimir_parametros( 10 , "São Paulo")