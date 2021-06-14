def solution(triangle):
    # 배열의 마지막에서 두번째 행부터 시작
    for i in range(len(triangle)-2,-1,-1):

        print(i)   # 행을 잘 가리키고 있는지 확인

        # 삼각형 행의 각 배열을 순회하며
        for j in range(len(triangle[i])):

            # 바로 아래의 열의 왼쪽,오른쪽 배열과 더하기 해본 후
            if triangle[i][j]+triangle[i+1][j] > triangle[i][j]+triangle[i+1][j+1]:

                # 더 큰값을 현재 배열에 저장합니다! --> 국소 최대값을 계속해서 얻어가면 전체 최대값을 얻을 수 있습니다
                triangle[i][j] = triangle[i][j]+triangle[i+1][j]

            else:
                triangle[i][j] = triangle[i][j]+triangle[i+1][j+1]

         # 사용한 행은 지워줍니다.
        del triangle[i+1]

    # 마지막으로 삼각형 배열을 출력하여 확인해보기
    print(triangle)

    # 배열의 최상단엔 언제나 최대값이 위치합니다.
    return triangle[0][0]

a =[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

# 최대값은??
print(solution(a))
