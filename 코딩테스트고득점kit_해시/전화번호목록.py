# 내 처음풀이
# def solution(phone_book):
#     count = []
#     babble = phone_book
#     for utter in phone_book: 
#         for text in babble:
#             if utter == text:
#                 continue
#             else:
#                 utter = utter.replace(text,' ')
#         count.append(utter)
#     if count == phone_book:
#         answer = True
#     else:
#         answer = False
#     return answer

#정답
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True

# 이건 hash를 사용해서 푼 것.
def solution(phone_book):
  answer = True
  hash = {}
  
  for i in phone_book:    # 모든 요소를 (전화번호) { '전화번호' : 1} 이렇게 담는다 
    hash[i] = 1
  print(hash)
  for i in phone_book:
    temp=''
    for j in i:
      temp += j
      if temp in hash and temp != i:           #담아놓은 hash에서 요소 찾기 
        answer = False
  return print(answer)
  
print(solution(["119", "97674223", "1195524421"]))