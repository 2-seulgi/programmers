import java.util.Arrays;

class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        int[][] index = new int[emergency.length][2];
        for(int i = 0 ; i < emergency.length; i++){
            index[i][0] =  emergency[i];
            index[i][1] = i;    
        }
        Arrays.sort(index, (a, b) -> b[0] - a[0]); 
        
        for(int i = 0 ; i < index.length; i++){
            int originalIndex = index[i][1]; 
            answer[originalIndex] = i+1;
        }
        return answer;
    }
}