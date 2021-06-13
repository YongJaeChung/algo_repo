answer = -1

def func(N,number,count,result):
    # 현재까지 최고의 해
    global answer

    # 숫자를 카운트 한 값이 8보다 크면 count를 초기화하고 리턴
    if count > 8:
        count = 0
        return
    # 연산 결과가 목표값과 같을때 수행
    if result == number:
        if count < answer or answer == -1:
            answer=count
        return
    # N을 받아 연산을 수행해 줄 노움변수 5 -> 55 이런 식으로 변화한다.
    gnome=0
    for i in range(8):
        gnome=gnome*10+N
        func(N, number,count+len(str(gnome)), result+gnome)
        func(N, number,count+len(str(gnome)), result-gnome)
        func(N, number,count+len(str(gnome)), result*gnome)
        func(N, number,count+len(str(gnome)), result/gnome)

def solution(N, number):
    func(N,number,0,0)
    return answer

solution(5,12)

print(solution(5,12))
