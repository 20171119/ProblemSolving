n,m,k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)
first = num_list[0]
second = num_list[1]
result = 0

count = m//(k+1) * k
count += m % (k+1)

result += first*count
result += second*(m-count)

print(result)