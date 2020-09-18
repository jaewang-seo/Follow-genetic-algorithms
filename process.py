import random
import string

password = 'brad1234'
min_len = 2
max_len = 10

def generate_word(lenght):
    result=''
    x = result.join(random.sample(string.ascii_letters + string.digits, k=lenght))
    return x

def generate_population(size, min_len, max_len):
    population = []
    for i in range(size):
        length = i % (max_len - min_len +1) + min_len
        population.append(generate_word(length))
        print(population)
    return population

def fitness(password, test_word):
    score = 0

    if len(password) != len(test_word):
        return score
    
    len_score = 0.5
    score += len_score

    for i in range(len(password)):
        if password[i] == test_word[i]:
            score +=1
    return score/ (len(password) + len_score) * 100

def compute_performace(population, password):
    performance_list = []

    for individual in population:
        score = fitness(password, individual)

        if score > 0:
            pred_len = len(individual)
        performance_list.append(individual, pred_len)

    population_sorted = sorted(performance_list, key=lambda x:x[1], reverse=True)

    return population_sorted, pred_len

def select_survivors(population_sorted, best_sample, lucky_few, password_len):
    next_generation = []

    for i in range(best_sample):
        if population_sorted[i][1] > 0:
            next_generation.append(population_sorted[i][0])

    lucky_survivors = random.sample(population_sorted, k=lucky_few)
    
fitness('abcdE', 'abcde')