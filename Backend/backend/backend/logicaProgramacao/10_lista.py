
#Lista inicial de tarefas
minhas_tarefas = ["Estudar Python", "Fazer exercicios", "Comprar pão", "Revisar matéria"]
(f"Tarefas pendentes: {minhas_tarefas}")

#Adicionando uma nova tarefa ao final da lista
minhas_tarefas.append("Lavar a louça")
print(f"Tarefa adicionada: {minhas_tarefas}")

#Adicionando uma tarefa em uma posição especifica (indice 1)
minhas_tarefas.insert(1, "Responder e-mails")
print(f"Tarefa inserida em posição especifica: {minhas_tarefas}")

#Removendo uma tarefa que já foi feita (pelo nome)
minhas_tarefas.remove("Comprar pão")
print(f"Tarefa 'Comprar pão' removida: {minhas_tarefas}")

#Removendo a última tarefa (útil para pilhas)
tarefa_removida = minhas_tarefas.pop() # Remove "Revisar matéria
print(f"Última tarefa removida ('{tarefa_removida}'): {minhas_tarefas}")