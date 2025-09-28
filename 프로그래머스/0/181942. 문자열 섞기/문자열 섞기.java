class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        for (int c = 0; c < str1.length(); c++ ){
            String t = str1.substring(c,c+1) + str2.substring(c,c+1);
            answer = answer+t;
        };
        return answer;
    }
}