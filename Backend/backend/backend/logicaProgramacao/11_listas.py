lista=[]
lista.append("bola")
lista.append("mesa")
lista.append("raquete")
lista.append("teclado")
lista.append("livro")
lista.append("carro")
lista.insert(1,"fone")
lista.insert(3,"celular")
print(f"objetos em estoque: {lista}")
objeto_removido = lista.pop()
del lista[5]
print(f"Última objeto removida ('{objeto_removido}'): {lista}")
