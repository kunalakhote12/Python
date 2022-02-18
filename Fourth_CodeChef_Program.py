T=int(input())
for tc in range(T):
	li = list(map(int, input().split(' ')))
	li.sort()
	print(li[1])
	
