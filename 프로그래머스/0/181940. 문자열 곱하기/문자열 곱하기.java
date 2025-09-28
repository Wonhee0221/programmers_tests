class Solution {
    public String solution(String my_string, int k) {
        String answer = "";
        for(int c=0; c<k; c++){
            answer = answer + my_string;
        };
        return answer;
    }
}