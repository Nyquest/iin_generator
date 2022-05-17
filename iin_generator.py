import random
import datetime

SECONDS_IN_DAY = 24 * 60 * 60
IIN_COUNT = 20_000_000

# распарсить строку статистики
def parse_stat(line, ages):
    both_dict = {}
    for i, v in enumerate(line.rstrip().split('\t')):
        v = v.strip()
        if headers[i] in ages:
            v = int(v.replace(' ', '')) * 1000
        both_dict[headers[i]] = v    
    return both_dict

# проверить суммы статистик по обоим полам в разрезе возрастов 
def check_stat(ages, both_dict, male_dict, female_dict):
    for age in ages:
        if both_dict[age] != male_dict[age] + female_dict[age]:
            return False
    return True

# высокосный ли год
def is_leap(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

# создать дату из года, месяца и дня месяца
def create_date(year, month, day):
    if month == 2 and day > 28 and not is_leap(year):
        day = 28
    return datetime.datetime(year, month, day)

# прибавить к дате несколько дней
def plus_day(date, days):
    return datetime.datetime.fromtimestamp(
        date.timestamp() + days * SECONDS_IN_DAY)

# случайная дата в заданном диапазоне
def random_date(date_from, date_to):
    return datetime.datetime.fromtimestamp(
        random.randrange(
            int(date_from.timestamp()), int(date_to.timestamp()) + 1, 
            SECONDS_IN_DAY))

# расчет контрольного разряда
def calc_sum(value):
    sm = sum([(i + 1) * (ord(value[i]) - ord('0')) for i in range(11)])
    k = sm % 11;
    if k == 10:
        sm = sum([(i + 3 if i + 3 <= 11 else i - 8) * (ord(value[i]) - ord('0')) for i in range(11)])
        k = sm % 11;
        if k == 10:
            return None
    return k

# дополнение ведущими нулями
def leading_zeros(value, length):
    return str(value).rjust(length, '0')

# вывести строку таблицы
def print_table_row(values):
    print('| ', end='')
    print(*values, sep=' | ', end='')
    print(' |')

# вывести таблицу возраст+пол
def print_table(ages, both_dict, male_dict, female_dict):
    headers = ['Age', 'Both', 'Male', 'Femail']
    lens = [len(header) for header in headers]

    for age in ages:
        lens[0] = max(lens[0], len(age))
        lens[1] = max(lens[1], len(str(both_dict[age])))
        lens[2] = max(lens[2], len(str(male_dict[age])))
        lens[3] = max(lens[3], len(str(female_dict[age])))

    print_table_row([str(val).rjust(length) for length, val in zip(lens, headers)])
    print_table_row([''.join(['-'] * length) for length in lens])

    for age in ages:
        print_table_row([str(val).rjust(length) for length, val in zip(lens, [age, both_dict[age], male_dict[age], female_dict[age]])])

# сгенерировать ИИН
def generate_iin(male, age_range, date_dict):
    age_range = [int(s) for s in age_range.split('-')]
    diff = random.randint(age_range[0], age_range[1])  
    now = datetime.datetime.now()
    begin_date = create_date(now.year - diff - 1, now.month, now.day)
    begin_date = plus_day(begin_date, 1)
    end_date = create_date(now.year - diff, now.month, now.day)
    birth_date = random_date(begin_date, end_date);    
    facet12 = leading_zeros(birth_date.year % 100, 2)
    facet34 = leading_zeros(birth_date.month, 2)
    facet56 = leading_zeros(birth_date.day, 2)
    
    if male == 'm':
        if birth_date < XX:
            facet7 = '1'
        elif birth_date >= XX and birth_date < XXI:
            facet7 = '3'
        else:
            facet7 = '5'
    else:
        if birth_date < XX:
            facet7 = '2'
        elif birth_date >= XX and birth_date < XXI:
            facet7 = '4'
        else:
            facet7 = '6'
            
    date_key = f'{facet12}{facet34}{facet56}'
    
    while True:
        counter = date_dict.get(date_key, 0) + 1
        date_dict[date_key] = counter
        if counter > 9999:
            raise Exception('Counter overflow')
        facet8_11 = leading_zeros(date_dict[date_key], 4)    
        
        result = f'{date_key}{facet7}{facet8_11}'        
        control_sum = calc_sum(result)
        if control_sum is not None:
            break
            
    
    
    return f'{result}{control_sum}'
    
# random.seed(111)

XX = create_date(1901, 1, 1)
XXI = create_date(2001, 1, 1)

with open('qaz_population_2020.txt') as file, open('iin.txt', 'w') as out:
    headers = file.readline().rstrip().split('\t')
    print(headers)
    ages = [header for header in headers if header[0].isdigit()]
    print(ages)
    file.readline()
    both_dict = parse_stat(file.readline(), ages)
    file.readline()
    male_dict = parse_stat(file.readline(), ages)
    file.readline()
    female_dict = parse_stat(file.readline(), ages)
    print(both_dict)
    print(male_dict)
    print(female_dict)
    if check_stat(ages, both_dict, male_dict, female_dict):
        raise Exception('Incorrect Stat')

    print_table(ages, both_dict, male_dict, female_dict)
        
    male_counts = []
    count = 0
    for age in ages:
        count += male_dict[age]
        male_counts.append(count)
    male_count = count
    print(male_counts)
    print(f'male_count = {male_count}')    
    
    female_counts = []
    count = 0
    for age in ages:
        count += female_dict[age]
        female_counts.append(count)
    female_count = count    
    print(female_counts)
    print(f'female_count = {female_count}')    
    
    both_count = male_count + female_count
    print(f'both_count = {both_count}')
    
    date_dict = {}
    
    for num in range(IIN_COUNT):
        rnd = random.randint(1, both_count)
        male = 'm'
        counts = male_counts
        if rnd > male_count:
            rnd -= male_count
            male = 'f'
            counts = female_counts
        for i, v in enumerate(ages):
            if rnd <= counts[i]:
                iin = generate_iin(male, ages[i], date_dict)
                print(f'{num + 1}) {iin}')
                print(iin, file=out)
                break   
        
    