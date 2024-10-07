LINK PARA O VIDEO DO YOUTUBE: https://youtu.be/HFAi-YSoCcQ

Explicação
Definição dos parâmetros: Definimos os parâmetros do problema, como o número de financiadores, cedentes, tamanho da população, número de gerações, taxa de crossover e taxa de mutação.

Simulação de dados: Criamos dados simulados para os financiadores e cedentes.

Função de aptidão: Calcula o retorno total e o risco total para uma dada alocação e retorna a aptidão como a diferença entre retorno e risco.

Criação de indivíduos e população: Funções para criar um indivíduo (solução) e a população inicial.

Seleção, crossover e mutação: Implementação dos operadores genéticos para seleção por torneio, crossover e mutação.

Algoritmo genético: A estrutura principal do algoritmo genético que cria novas gerações até atingir o número máximo de gerações, retornando a melhor solução encontrada.

O algoritmo genético foi executado com sucesso por 200 gerações. Abaixo estão os principais resultados:

Melhor solução :[13, 5, 13, 13, 15, 13, 4, 11, 13, 13]
Melhor valor de condicionamento físico :-5508639059.566004
Interpretação de resultados
Melhor Solução : A lista representa a alocação de recursos de cada financiador (índice) para o respectivo cedente (valor).
Melhor valor de aptidão : o valor de aptidão indica a qualidade da solução, equilibrando o retorno sobre o investimento e minimizando o risco.
Resumo
Esta solução representa a melhor alocação encontrada pelo algoritmo genético ao longo de 200 gerações, considerando os dados simulados de financiadores e cedentes. O valor de aptidão negativo é devido à alta penalidade associada ao cálculo de risco na função de aptidão, indicando áreas para maior refinamento do modelo.

Próximos passos
Ajuste fino de parâmetros : ajuste parâmetros como tamanho da população, taxa de cruzamento e taxa de mutação para potencialmente melhorar os resultados.
Melhorando a função de aptidão : refine a função de aptidão para equilibrar melhor o retorno e o risco, ou incorpore fatores adicionais, como condições de mercado.
Análise comparativa : implemente e compare com uma solução usando programação linear para avaliar o desempenho e a otimização de ambas as abordagens.
