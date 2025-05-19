class Solution {
    public long solution(int price, int money, int count) {
        long answer = -1;
        long tp = 0;
        
        for (int i = 1 ; count >= i; i++){
             tp += i * (long)price;
        }
        long shortage = tp - money;
        return (shortage >0 ? shortage : 0);
    }
}