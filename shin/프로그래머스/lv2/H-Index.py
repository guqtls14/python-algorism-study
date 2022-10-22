

def solution(citations):
    citations.sort()
    article_count = len(citations)
    
    for i in range(article_count):
        if citations[i] >= article_count-i:
            return article_count-i
    return 0

li=[5,5,5,2]

print(solution(li))

# https://yunaaaas.tistory.com/56
# https://jokerldg.github.io/algorithm/2021/06/01/h-index.html