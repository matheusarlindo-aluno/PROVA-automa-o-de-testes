import pytest
import unittest
from unittest.mock import patch   
from main.gerenciador_tarefas import GerenciadorTarefas


class TestUsuario(unittest.TestCase):
    def setUp(self):
        self.mock_tarefas = [
            {'id': 1, 'titulo': 'Tarefa 1', 'descricao': 'Descrição da tarefa 1', 'status': 'pendente'},
            {'id': 2, 'titulo': 'Tarefa 2', 'descricao': 'Descrição da tarefa 2', 'status': 'pendente'},
            {'id': 3, 'titulo': 'Tarefa 3', 'descricao': 'Descrição da tarefa 3', 'status': 'concluída'},
            {'id': 4, 'titulo': 'Tarefa 4', 'descricao': 'Descrição da tarefa 4', 'status': 'pendente'}
        ]

    @patch('main.gerenciador_tarefas.GerenciadorTarefas', return_value= {'id': 1, 'titulo': 'Tarefa 1', 'descricao': 'Descrição da tarefa 1', 'status': 'pendente'})
    def test_adicionar_tarefa(self, mock_adicionar_tarefa):
        mock_adicionar_tarefa.return_value = self.mock_tarefas[0]
        gerenciador = GerenciadorTarefas()
        response = gerenciador.adicionar_tarefa('Tarefa 1', 'Descrição da tarefa 1')
        self.assertEqual(response,{'id': 1, 'titulo': 'Tarefa 1', 'descricao': 'Descrição da tarefa 1', 'status': 'pendente'})


    @patch('main.gerenciador_tarefas.GerenciadorTarefas', return_value= {'id': 1, 'titulo': 'Tarefa 1', 'descricao': 'Descrição da tarefa 1', 'status': 'pendente'})    
    def test_listar_tarefas(self, mock_listar_tarefas):
        mock_listar_tarefas.return_value = self.mock_tarefas
        gerenciador = GerenciadorTarefas()
        response = gerenciador.listar_tarefas()
        self.assertEqual(response, self.mock_tarefas)


    @patch('main.gerenciador_tarefas.GerenciadorTarefas', return_value= {'id': 2, 'titulo': 'Tarefa 2', 'descricao': 'Descrição da tarefa 2', 'status': 'pendente'},)
    def test_marcar_como_concluida(self, mock_marcar_como_concluida):
        mock_marcar_como_concluida.return_value =  [1]
        gerenciador = GerenciadorTarefas()
        response = gerenciador.marcar_como_concluida(2)
        self.assertEqual(response, {'id': 2, 'titulo': 'Tarefa 2', 'descricao': 'Descrição da tarefa 2', 'status': 'concluída'},)


    @patch('main.gerenciador_tarefas.GerenciadorTarefas', return_value= {'id': 3, 'titulo': 'Tarefa 3', 'descricao': 'Descrição da tarefa 3', 'status': 'concluída'},)
    def test_filtrar_por_status(self, mock_filtrar_por_status):
        mock_filtrar_por_status.return_value = self.mock_tarefas[2]
        gerenciador = GerenciadorTarefas()
        response = gerenciador.filtrar_por_status('concluída')
        self.assertEqual(response, {'id': 3, 'titulo': 'Tarefa 3', 'descricao': 'Descrição da tarefa 3', 'status': 'concluída'})


    @patch('main.gerenciador_tarefas.GerenciadorTarefas', return_value= {'erro': 'Tarefa não encontrada.'},)
    def test_marcar_tarefa_inexistente(self, mock_marcar_tarefa_inexistente):
        mock_marcar_tarefa_inexistente.return_value = {'erro': 'Tarefa não encontrada.'}
        gerenciador = GerenciadorTarefas()
        response = gerenciador.encontrar_tarefa_por_id(8)
        self.assertEqual(response, {'erro': 'Tarefa não encontrada.'})


if __name__ == '__main__':
    unittest.main()


