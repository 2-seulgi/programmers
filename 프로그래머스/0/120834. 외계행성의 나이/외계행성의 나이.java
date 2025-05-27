class Solution {
    public String solution(int age) {
        String answer = "";
        String strAge = String.valueOf(age);

        for(int i = 0 ; i < strAge.length(); i++ ){
            int digit = Character.getNumericValue(strAge.charAt(i));
            System.out.println("digit: " + digit);
            char ch = (char)('a'+ digit);
            answer +=ch;
        }
        
        return answer;
    }
}