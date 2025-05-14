class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        double sum = 0;
        double length = arr.length;
        for(double i : arr){
            sum += i;
        }
        answer = (sum / length);
        return answer;
    }
}