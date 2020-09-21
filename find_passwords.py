import random
import string

# 설정한 비밀번호 
password = 'brad1234'

# 비밀번호 최소길이
min_len = 2

# 비밀번호 최대길이
max_len = 10

# random 단어를 생성하는 함수
def generate_word(lenght):

    #
    result=''

    # random 단어를 생성하기 위해 랜덤 아스키코드와 랜덤 숫자를 lenght만큼 생성한다. 
    x = result.join(random.sample(string.ascii_letters + string.digits, k=lenght))
    return x

# 최초 유전자 생성
def generate_population(size, min_len, max_len):

    # 최초로 만들어진 아이들을 리스트 지정
    population = []

    # size값에 따라 2 to 10 크기에 문자열 생성
    for i in range(size):
        length = i % (max_len - min_len +1) + min_len

        # 문자열 결과 population에 append
        population.append(generate_word(length))
    return population



# generate_population(100, min_len, max_len)

# 유전자 성능 점수 측정하기
def fitness(password, test_word):
    
    # 성능 초기값
    score = 0

    # password 길이와 테스트 길이가 다르면
    if len(password) != len(test_word):

        # 점수 유지
        return score
    
    # password 길이와 테스트 길이가 같으면 len_score = 0.5점
    len_score = 0.5
    
    # 기존 점수 + len_score 
    score += len_score

    # password와 test_word 문자를 하나씩 비교
    for i in range(len(password)):

        # password와 test_word 문자가 같다면
        if password[i] == test_word[i]:

            # score 1점
            score += 1

    # 성능을 %로 표기 : 총 점수를 password 문자열 길이 값과 len_score 값의 합으로 나눈다
    return score/ (len(password) + len_score) * 100

# fitness('abcdE','abcde')

# 성능을 측정 후 선발하기 위한 전처리
def compute_performace(population, password):

    # 
    performance_list = []

    # 최초 선발된 아이들의 유전자
    for individual in population:

        # fitness함수를 통해 점수를 받는다
        score = fitness(password, individual)

        # score > 0이면 password와 test_len의 길이가 맞는 아이들
        if score > 0:

            # 유전자 길이를 pred_len에 지정
            pred_len = len(individual)
        
        # performance_list에 유전자 정보, 유전자 길이를 list로 지정 
        performance_list.append([individual, score])
    
    # performance_list의 x[1]은 score이고, 점수를 큰 수부터(내림차순)정렬
    population_sorted = sorted(performance_list, key=lambda x:x[1], reverse=True)

    # 점수로 정렬한 유전자 정보, 유전자 길이
    return population_sorted, pred_len

# 선발할 아이들 뽑기
# population_sorted[i][0] | 유전자 정보
# population_sorted[i][1] | 유전자 점수(성능)
def select_survivors(population_sorted, best_sample, lucky_few, password_len):

    # 다음세대에 전해줄 유전자 정보를 담는 list
    next_generation = []

    # 성능이 좋은 best_sample값 만큼 아이들을 뽑는다 
    for i in range(best_sample):

        # 아이들의 유전자 점수가 > 0 이면
        if population_sorted[i][1] > 0:

            # next_generation(다음 세대)에 성능이 좋은 유전자 정보를 넣는다
            next_generation.append(population_sorted[i][0])

    # population_sorted에서 lucky_few만큼 임의의 lamdom 아이들을 선발  
    lucky_survivors = random.sample(population_sorted, k=lucky_few)
    
    # next_generation(다음 세대)에 성능이 lamdom한 유전자 정보를 넣는다
    for i in lucky_survivors:
        next_generation.append([i][0][0])

    # 선발 결과과 best_sample + lucky_few의 개수 보다 적으면
    if len(next_generation) < best_sample + lucky_few:

        # generate_word에서 password_len만큼 아이들을 landom하게 생성하여 next_generation에 넣는다
        next_generation.append(generate_word(lenght=password_len))

    # next_generation를 landom하게 섞는다
    random.shuffle(next_generation)

    return next_generation

# 아이들 생성을 pop으로 지정
pop = generate_population(size=100, min_len=min_len, max_len=max_len)

# 생성된 아이들과 password을 통해 유전자 정보와 유전자 길이를 지정
pop_sorted, pred_len = compute_performace(population=pop, password=password)

# select_survivors에서 다음 세대로 선발된 아이들을 survivors에 지정
survivors = select_survivors(population_sorted=pop_sorted, best_sample=20, lucky_few=20, password_len=pred_len)

print('Password lengths must be {}'.format(pred_len))
print(survivors)
print(len(survivors))

# 새로운 아이들 만들기 (individual1 : 아이1, individual2 : 아이2)
def create_child(individual1, individual2):
    child = ''

    # 아이1과, 아이2중 유전자 길이가 짧은 유전자 길이를 지정
    min_len_ind = min(len(individual1), len(individual2))

    # 50% 확률로 child에 아이1과 아이2에 유전자를 선택한다
    for i in range(min_len_ind):

        # random값이 < 50 이면
        if(int(100 * random.random()) < 50):

            # individual1[i]
            child += individual1[i]

        else:
            # individual1[i]
            child += individual2[i]
    return child


