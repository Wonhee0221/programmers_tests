def gcd(a, b):
    while b > 0:
        a, b = b, a%b
        print(a,b)
    return a 
def solution(numer1, denom1, numer2, denom2):
    numer = denom1*numer2 + denom2*numer1		#분자
    denom = denom1 * denom2				#분모
    g = gcd(denom, numer)				#최대공약수 구하기
    return [numer//g, denom//g]


print(solution(1, 2, 3, 4))