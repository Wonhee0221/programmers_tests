class Solution {
    public int solution(int order) {
        int answer = 0;
        String orderStr = ""+order;
        for (int i = 0; i< orderStr.length(); i++){
            char x = orderStr.charAt(i);
            if ( x == '3' || x == '6' || x == '9' ) answer++;
        };
        return answer;
    }
}