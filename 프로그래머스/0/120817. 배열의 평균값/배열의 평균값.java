class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int sum  = 0;
        int length = numbers.length;
        
        for (int i = 0; i < length ; i++){
            sum += numbers[i];
        }
        answer = (double)sum/length;
        return answer;
    }
}