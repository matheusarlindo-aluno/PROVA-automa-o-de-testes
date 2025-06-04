
from flask import Flask, jsonify, request
gerenciador_tarefas= Flask(__name__)

# implementar um gerenciador de tarefas simples que permita:
# 1. Adicionar tarefas
# 2. Listar tarefas
# 3. Marcar tarefas como concluídas
# 4. Filtrar tarefas por status
# Requisitos:
# - Use um array/dicionário para armazenar as tarefas (não use banco de dados)
# - Cada tarefa deve ter: id (automático), título, descrição e status (pendente/concluída)
# Implemente a classe GerenciadorTarefas com os métodos necessários


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = [
                {'id': 1, 'titulo': 'Tarefa 1', 'descricao': 'Descrição da tarefa 1', 'status': 'pendente'},
                {'id': 2, 'titulo': 'Tarefa 2', 'descricao': 'Descrição da tarefa 2', 'status': 'pendente'},
                {'id': 3, 'titulo': 'Tarefa 3', 'descricao': 'Descrição da tarefa 3', 'status': 'concluída'},
                {'id': 4, 'titulo': 'Tarefa 4', 'descricao': 'Descrição da tarefa 4', 'status': 'pendente'}
            ]
        self.contador_id = 1
    
    def adicionar_tarefa(self, titulo, descricao):
        tarefa = {
            'id': self.contador_id,
            'titulo': titulo,
            'descricao': descricao,
            'status': 'pendente'
        }
        self.tarefas.append(tarefa)
        self.contador_id += 1
        return tarefa
    
    def listar_tarefas(self):
        return self.tarefas
    
    def marcar_como_concluida(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa['id'] == id_tarefa:
                tarefa['status'] = 'concluída'
                return tarefa
    
    def filtrar_por_status(self, status):
        for tarefa in self.tarefas:
            if tarefa['status'] == status:
                return tarefa
        if status not in ['pendente', 'concluída']:
            return {'erro': 'Status inválido. Use "pendente" ou "concluída".'} 
        
    def encontrar_tarefa_por_id(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa['id'] == id_tarefa:
                return tarefa
            if tarefa['id'] != id_tarefa:
                return {'erro': 'Tarefa não encontrada.'} 
    
     


