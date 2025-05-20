class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;
        double d_answer = (double)num1/num2 ;
        answer = (int)(d_answer * 1000);
        return answer;
    }
}