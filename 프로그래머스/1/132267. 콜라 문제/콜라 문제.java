class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;

        while(n >= a){
            int ec = n/a; // 교환 횟수
            int newCola = ec*b;
            answer += newCola; // 새 콜라수
            
            int left = n%a; // 교환 후 남은 병
            n = newCola + left;
        }
        
        return answer;
    }
}