class Solution {
    public int[] solution(int[] numbers) {
        
        int[] answer = new int[numbers.length];
                
        for(int i = 0; i < numbers.length ; i++ ){
            int addNum = numbers[i] * 2;
            answer[i] = addNum;
        }
        return answer;
    }
}