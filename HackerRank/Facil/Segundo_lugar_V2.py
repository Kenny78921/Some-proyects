
#% https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

n = int(input())
arr = map(int, input().split(" "))

print(sorted(set(arr))[-2])
