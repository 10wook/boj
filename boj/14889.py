#14889 9/5
import itertools
people = int(input())
stats = []

for i in range (people) :
    stats.append(input().split())
    for j in range (people):
        stats[i][j] =int(stats[i][j])
# 인 풋 편한 방향으로 치환하기
# 문제 풀이        
# 모든 경우의 수를 다 탐색해야 할 것으로 추정


# 일단 만들어야 하는거 : 팁 조합 별 스탯 확인 함수        
def stat_check(team,stats): # 여기서 팀은 팀에 소속 되어있는 사람들의 번호로 구성된 리스트
    tot_stat = 0
    for i in team:
        for j in team:
            tot_stat+=stats[i][j]
    return tot_stat
        
        
def stat_compare(team_list):
    compared_stat = 0
    all_list = list(range(people))
    for i in team_list:
        all_list.remove(i)
       
    team1_stat = stat_check(team_list,stats)  
    team2_stat = stat_check(all_list,stats)      
    
    compared_stat = team2_stat - team1_stat
    return max(compared_stat,-compared_stat)


### 이제 할일들이 모두 갖추어 졌으니
## 팀원을 선정하고 점수를 계산해야함
## 팀원을 어떻게 산정하더라....
#일단 경우의 수가 nC2라는건 알겠음

def combinations_recursive(arr, r):
    # 배열이 비었거나, r이 0이면 빈 리스트 반환
    if not arr or r < 0:
        return []
    # r이 0이면 현재까지의 조합을 반환
    if r == 0:
        return [[]]

    # 첫 번째 원소를 포함하는 조합과 포함하지 않는 조합을 재귀적으로 생성
    first = arr[0]
    rest = arr[1:]

    # 첫 번째 원소를 포함하는 조합
    comb_with_first = [[first] + combo for combo in combinations_recursive(rest, r - 1)]

    # 첫 번째 원소를 포함하지 않는 조합
    comb_without_first = combinations_recursive(rest, r)

    # 두 가지 조합을 합쳐 반환
    return comb_with_first + comb_without_first













people_list = list(range(people))    
# teamlists = combinations_recursive(people_list,people/2)
# print(people)
teamlists = itertools.combinations(people_list,people//2)
minimun = float('inf')
for Team in teamlists:
    minimun = min(stat_compare(Team),minimun)

print(minimun)
