import random

# Definição dos parâmetros do problema
NUM_FINANCIADORES = 10
NUM_CEDENTES = 20
POPULATION_SIZE = 100
NUM_GENERATIONS = 200
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.1

# Simulação de dados dos financiadores e cedentes
financiadores = [{'id': i, 'capital': random.uniform(10000, 100000)} for i in range(NUM_FINANCIADORES)]
cedentes = [{'id': i, 'valor_recebivel': random.uniform(5000, 50000), 'taxa_retorno': random.uniform(0.01, 0.05)} for i in range(NUM_CEDENTES)]

# Função de aptidão
def fitness(individual):
    roi_total = 0
    risco_total = 0
    for i, alocacao in enumerate(individual):
        if alocacao is not None:
            cedente = cedentes[alocacao]
            financiador = financiadores[i]
            roi_total += cedente['taxa_retorno'] * financiador['capital']
            risco_total += (cedente['valor_recebivel'] - financiador['capital'])**2  # Exemplo simples de risco
    return roi_total - risco_total  # Maximiza retorno e minimiza risco

# Criação de um indivíduo (solução)
def create_individual():
    return [random.choice(range(NUM_CEDENTES)) for _ in range(NUM_FINANCIADORES)]

# Criação da população inicial
def create_population(size):
    return [create_individual() for _ in range(size)]

# Seleção por torneio
def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    selected = sorted(selected, key=lambda x: fitness(x), reverse=True)
    return selected[0]

# Operador de crossover
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, NUM_FINANCIADORES - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1, parent2

# Operador de mutação
def mutate(individual):
    if random.random() < MUTATION_RATE:
        point = random.randint(0, NUM_FINANCIADORES - 1)
        individual[point] = random.choice(range(NUM_CEDENTES))
    return individual

# Algoritmo genético
def genetic_algorithm():
    population = create_population(POPULATION_SIZE)
    for generation in range(NUM_GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.append(mutate(offspring1))
            new_population.append(mutate(offspring2))
        population = new_population
        best_individual = max(population, key=fitness)
        print(f'Generation {generation + 1}, Best Fitness: {fitness(best_individual)}')
    return best_individual

# Execução do algoritmo genético
best_solution = genetic_algorithm()
best_solution, fitness(best_solution)
