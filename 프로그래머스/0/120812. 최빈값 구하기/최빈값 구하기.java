import java.util.*;

class Solution {
    public int solution(int[] array) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int num : array){
            map.put(num, map.getOrDefault(num, 0)+1);
        }
        int max = Collections.max(map.values());
        
        int mode = -1;
        int count = 0;
        
        for (Map.Entry<Integer, Integer> entry : map.entrySet()){
            if(entry.getValue() == max){
                count++;
                mode = entry.getKey();
            }   
        }
        return count > 1 ? -1 : mode;
    }
}
