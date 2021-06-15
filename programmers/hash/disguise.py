## 이번 해답은 고등학교때 배운 순열과 조합의 조합을 사용 했습니다.
 
# 팩토리얼 계산 해주는 함수
def factorial(v):
    result = 1
    for i in range(1,v+1):
        result = result * i
 
    return result
 

# 조합을 계산해 주는 함수
def combination(n,k):
    return factorial(n) / (factorial(k) * factorial(n-k))
 
 
def solution(clothes):
    
    # 물품의 카테고리를 중복없이 가지는 배열 생성
    category = []
 
    # 카테고리 넣어주기
    for item in clothes:
        category.append(item[1])
    
    # 카테고리를 set 형식으로 바꿔서 중복제거
    categories = set(category)
 
    # 카테고리의 출현 빈도를 저장할 딕셔너리    
    dic = {}
 
    # 카테고리의 출현빈도를 세어준다.
    for category in categories:
        dic[category] = 0
        for item in clothes:
            if item[1] == category:
                dic[category] = dic[category] + 1
 
    # 곱을 이용해서 값을 구할 것이고, 한가지 카테고리에 한가지 품목만 있어도 답이 1이기 때문에 1로 초기화
    answer = 1    
 
    # 조합 할 수 있는 가짓수 구하기 예) 2가지, 1가지 => 2C0*1C0 + 2C0*1C1 + 2C1*1C0 + 2C1*1C1
    # 결합법칙을 사용하여 이 식을 정리하면, (2C0+2C1)*(1C0+1C1)이 됩니다.
    for key in dic:
        temp = 0
 
        # 각 카테고리마다 0개 혹은 1개만 선택할 수 있기때문에 0~1 까지만
        for i in range(0,2):
            # (2C0+2C1) 같은 연산 하는 과정 
            temp = temp + combination(dic[key],i)
        # 기존 가짓수에 곱해서 저장
        answer = answer * temp
            
    # 모두 선택 안할 경우의 한가지를 제외
    answer = answer -1
    return answer