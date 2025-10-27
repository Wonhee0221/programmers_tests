class Solution {
    public int solution(int n) {
        int answer = 0;
        if (n % 2 == 0){
            for (int i = 2; i <= n; i+=2){
                answer = answer + (i*i);
            };
        } else {
             for (int i = n; i > 0; i-= 2){
                answer = answer + i;
            };
        };
        
        return answer;
    }
}