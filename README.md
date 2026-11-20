# StructDesk 

<p>Esse projeto foi feito para aplicação teórica do que foi estudado em sala de aula na matéria de estutura de dados e algoritmos 2</p>

<p>O projeto é um gerenciador de chamados de uma empresa em que será gerenciado somente por algoritmos de busca, ordenação e árvores sem o uso de um banco de dado para realizar as tarefas de  busca , inserção , atualização e exclusão de dados o famoso CRUD. A nossa única base de dados será um arquivo com extensão .csv</p>


## 1. Estruturas de dados
- Lista encadeada: armazenar dinamicamente os chamados e seus históricos de movimentação.

- Fila (Queue): controlar a ordem de atendimento dos chamados, seguindo o princípio FIFO (First In, First Out).
- Heap (Fila de prioridade): organizar os chamados de acordo com sua prioridade, permitindo que os casos mais urgentes sejam atendidos primeiro.
- Tabela hash: permitir a busca, inserção e remoção de chamados por meio de um identificador único, como o ID do chamado.
- Árvore AVL: organizar os chamados por ID, data ou outro critério, mantendo a árvore balanceada para garantir operações eficientes.
- Grafo: representar dependências entre chamados, permitindo identificar quais solicitações precisam ser resolvidas antes de outras.
## 2. Algoritmos
- Merge Sort: ordenar chamados por data de abertura, prioridade ou prazo.
- Busca binária: localizar chamados em coleções previamente ordenadas.
- BFS (Busca em Largura): explorar relações e dependências entre chamados.
- DFS (Busca em Profundidade): investigar cadeias de dependências e conexões entre solicitações.
- Ordenação topológica: determinar uma sequência válida de execução para chamados que possuem dependências, desde que o grafo não contenha ciclos.
## 3. Funcionalidades do sistema
- CRUD :
    - Cadastrar
    - consultar
    - atualizar 
    - remover
- Atribuir um identificador único a cada chamado.
- Definir prioridades: baixa, média, alta e crítica.
- Gerenciar a fila de atendimento.
- Buscar chamados por ID utilizando uma tabela hash.
- Ordenar e filtrar chamados por data, prioridade e status.
- Registrar o histórico de alterações de cada chamado.
- Associar chamados que dependem da resolução de outras solicitações.
- Gerar relatórios de chamados abertos, em andamento e concluídos.

## 4. Análise de complexidade

<p>Nós também iremos ver a eficiência dos algoritmos que usaremos no nosso projeto</p>

| Estrutura/Algoritmo | Complexidade |
|---------------------|--------------|
| Lista encadeada     | Busca por valor: O(n) |
| Fila                | Inserção e remoção: O(1) |
| Heap                | Inserção e remoção prioritária: O(log n) |
| Tabela hash         | Busca média: O(1); pior caso: O(n) |
| Árvore AVL          | Busca, inserção e remoção: O(log n) |
| Merge Sort          | Ordenação: O(n log n) |
| BFS                 | Percurso em grafo: O(V + E) |
| DFS                 | Percurso em grafo: O(V + E) |

<p>Porque ultilizar essas estrutura ?, existem estruturas acimas que resolvem o mesmo problema, mas a questão é que quando vamos usar estrutura de dados,
precisamos pensar no Big(O) em que aquela tarefa executa em certa operação , um exemplo disso é a imagem a seguir:</p>

| Operação           | Pilha | Fila | Lista Encadeada | Hash Table |
| ------------------ | ----- | ---- | --------------- | ---------- |
| Inserir            | O(1)  | O(1) | O(1)\*          | O(1)\*\   |
| Remover            | O(1)  | O(1) | O(1)\*          | O(1)\*\   |
| Buscar             | O(n)  | O(n) | O(n)            | O(1)\*\   |
| Consultar elemento | O(1)  | O(1) | O(n)            | O(1)\*\   |

- **O(1):** tempo constante.
- **O(n):** tempo linear.
- **\* Lista encadeada:** considerando operações no início.
- **\*\* Hash Table:** complexidade média.

## 5. Objetivo acadêmico

<p>O objetivo será implementar os conhecimento adquiridos no curso e ver como a implementação pode ser feita por baixo dos panos no dia a dia</p>

### Extra ( se der tempo ) !!!!!

<p>Implementar uma interface gráfica no projeto para o uso simples do usuário</p>
