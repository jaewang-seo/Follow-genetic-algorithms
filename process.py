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


fitness('abcdE', 'abcde')