#%% Greedy-1
#잔돈문제
n=int(input())
coin =[500,100,50,10]
num=0

for i in coin:
    num=n//i
    n%=i
    print(str(i)+"원 "+str(num)+"개")
    
#%% Greedy
# 그리디 실전 문제 1, 92p
# =============================================================================
# 배열의 크기 n, 숫자 합 횟수 m, 연속합 횟수 k
# 입력예시 
# 5 8 3
# 2 4 5 4 6
# 출력 46
# 
# 24 20 12
# =============================================================================
n,m,k=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort(reverse=True)

num=0
while(m>0):
    for i in range(k):
        num+=arr[0]
        m-=1
        if m==0:
            break
    num+=arr[1]    
    m-=1
        
print(num)

    

# =============================================================================
# 
# 반복되는 수열
# =>
# 연속 가능한 횟수 k, 전체 합의 수 m
# m번 까지 
# k+1=(arr[0]*K+arr[1]*1)
# 
# m//(k+1)
# 
# m>k 
# =============================================================================

#%%
n,m,k=map(int,input().split())
data=list(map(int,input().split()))
data.sort(reverse=True)

count=m//(k+1)*k
count+=m%(k+1)
result=0
result+=(count)*data[0]
result+=(m-count)*data[1]

print(result)

#%%








