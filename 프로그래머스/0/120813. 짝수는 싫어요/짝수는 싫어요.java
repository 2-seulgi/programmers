class Solution {
    public int[] solution(int n) {
        int[] answer = new int[(n+1)/2];
        int i = 1;
        int idx= 0;
        while(i <= n){
            if(i%2 == 1){
                answer[idx++]= i;
            }
            i++;
        }
        return answer;
    }
}