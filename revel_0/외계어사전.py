spell = ["p", "o", "s"]	
dic= ["sod", "eocd", "qixm", "adio", "soo"]

def solution(spell, dic):
    for d in dic:
        print(d)
        print(set(spell))
        print(set(d))

        if not set(spell) - set(d):
            return 1
    return 2

solution(spell, dic)