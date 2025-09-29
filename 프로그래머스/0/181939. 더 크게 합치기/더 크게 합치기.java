class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String str_a  = String.valueOf(a);
        String str_b  = String.valueOf(b);
        int answer_a = Integer.valueOf(str_a.concat(str_b));
        int answer_b = Integer.valueOf(str_b.concat(str_a));
        if (answer_a > answer_b){
            return answer_a;
        } else{
            return answer_b;
        }
    }
}