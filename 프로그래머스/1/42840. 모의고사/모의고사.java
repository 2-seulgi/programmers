import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] one = {1, 2, 3, 4, 5};
        int[] two = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] three = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        int[] score = new int[3]; // 수포자별 점수
        
        for(int i = 0; i < answers.length ; i++){
            if(answers[i] == one[i % one.length])  score[0]++;
            if(answers[i] == two[i % two.length])  score[1]++;
            if(answers[i] == three[i % three.length])  score[2]++;
        }
        int max = Math.max(score[0], Math.max(score[1], score[2]));
        
        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < 3; i++){
            if(score[i] == max){
                result.add(i+1);
            }
        }
        
        int[] answer = new int[result.size()];
        for(int i = 0; i< result.size(); i++){
            answer[i] = result.get(i);
        }
        

        return answer;
    }
}