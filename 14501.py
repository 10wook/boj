# 삼성 문제 퇴사

day = int(input())
days_pay = []

for i in range (day) :
    days_pay.append(input().split())
    days_pay[-1][0] =int(days_pay[-1][0])
    days_pay[-1][1] =int(days_pay[-1][1])
# 여기서는 재귀적으로 짜면 좋을듯?
def get_paid(days_pay,last_days):
    if days_pay == [] :
        return 0
    pay = 0
    if days_pay[-1][0] > last_days:# 남은 날짜가 없는 경우
        
        return get_paid(days_pay[:-1],last_days+1)
    else: # 일단 할 수 있기는 한 경우  => 앞에 날짜들이랑 일정 조율이 필요
        
        #pay = max(get_paid(days_pay[:-1],0,tot_pay),days_pay[-1][1]) 
        # 하는 경우 가능한 돈 VS 못하는 경우 가능한 돈 비교를 해야함
        #하는 경우 계산 법 => 이번건 금액 + 뒤에 내용 재귀 
        # get_paid(days_pay[:-1],0)+days_pay[-1][1]
        # 이번거 안하는 경우 계산 법
        # get_paid(days_pay[:-1],last_days+1)
        # 두개 비교해서 큰거 갖기
        pay = max((get_paid(days_pay[:-1],1)+days_pay[-1][1]), (get_paid(days_pay[:-1],last_days+1)))
        
        return pay 


print(get_paid(days_pay,1))