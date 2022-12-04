from scipy.stats import chi2

def common_sample_ratio(a, b):
    return a / b

def expectation_frequency(n, p):
    return n * p

def chi2_test(o, e):
    print("관측도수와 기대도수의 차:", o - e)
    return ((o - e) ** 2) / e

x, y = map(int, input("행과 열의 수를 입력하십시오: ").split())
table = []
for i in range(x):
    row = list(map(int, input('한 행의 값들을 입력하십시오: ').split()))
    table.append(row)
        
for i in range(len(table)):
    table[i].append(sum(table[i]))
    
column_sum_line = []
for i in range(y + 1):
    column_sum = 0
    for j in range(x):
        column_sum += table[j][i]
    column_sum_line.append(column_sum)
table.append(column_sum_line)

for i in range(x + 1):
    print(table[i])

n = table[x][y]
print(n)
ratio_list = [[] for i in range(x)]
for i in range(x):
    sample_num = table[i][y]
    for j in range(y):
        ratio_list[i].append(expectation_frequency(sample_num, common_sample_ratio(table[x][j], n)))
        
for row in ratio_list:
    print(row)

chi2_star = 0
for i in range(x):
    for j in range(y):
        each_sum = chi2_test(table[i][j], ratio_list[i][j])
        print(each_sum)
        chi2_star += each_sum

print("계산된 검정통계량의 값:", chi2_star)

dof = (x - 1) * (y - 1)
alpha = float(input("유의수준을 입력하십시오: "))
chi2_alpha = chi2.ppf(1 - alpha, dof)
print("자유도 %d인 카이제곱분포에서 윗쪽 꼬리의 확률이 %f가 되는 지점은 %f입니다."%(dof, alpha, chi2_alpha))

if chi2_alpha <= chi2_star:
    print(f"유의수준 {int(alpha * 100)}%하에서 귀무가설을 기각할 수 있는 유의미한 증거가 된다.")
else:
    print(f"유의수준 {int(alpha * 100)}%하에서 귀무가설을 기각할 수 있는 유의미한 증거가 될 수 없다.")