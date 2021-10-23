def insert (listaA , listaB , indice: int):
    """
    
    """
    return listaA[:indice] + listaB + listaA[indice:]

    
def ate_o_primeiro (lista , objec):
    """
    
    """
    if objec not in lista:
        return lista
    else:
        local = lista.index(objec)
        for i in range(len(lista[:local])):
            return lista[:local]
    
        
    
def corta_lista(lista , indice):
    """
    
    """
    if isinstance(lista, str):
        nova_lista = lista[indice+1:] + lista[indice] + lista[:indice]
        return nova_lista
    elif isinstance(lista, list):
        nova_lista = lista[indice + 1:]
        nova_lista.append(lista[indice])
        nova_lista.extend(lista[:indice])
        return nova_lista
