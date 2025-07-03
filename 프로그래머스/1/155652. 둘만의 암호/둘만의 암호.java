import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {

        StringBuilder result = new StringBuilder();
        List<Character> available = new ArrayList<>();
        
        for( char ch ='a'; ch <= 'z'; ch++){
            if(!skip.contains(String.valueOf(ch))){
                available.add(ch);
            }
        }
        for(char ch: s.toCharArray()){
            int chIndex = available.indexOf(ch);
            int newIndex = (chIndex + index ) % available.size();
            result.append(available.get(newIndex));
        }
        return result.toString();
    }
}