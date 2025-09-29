class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int answer_a = Integer.parseInt(String.valueOf(a) + String.valueOf(b));
        if (answer_a > (2*a*b)){
            return answer_a;
        }
        return (2*a*b);
    }
}