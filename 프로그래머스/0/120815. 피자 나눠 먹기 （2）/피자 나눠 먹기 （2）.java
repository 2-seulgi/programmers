class Solution {
    private int gcd(int a, int b) {
    return b == 0 ? a        
                  : gcd(b, a % b);  
    }
    public int solution(int n) {
        int answer = 0;
        int num = gcd(n, 6);        
        answer = n/num;
        
        return answer;
    }
}