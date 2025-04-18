import java.util.ArrayDeque;

class Solution {
    public int[] solution(int[] prices) {
        int count = prices.length;
        
        int[] answer = new int[count];
        ArrayDeque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{0, count-1});
        for (int i = count - 1; i >= 0; i--) {
            int price = prices[i];
            while (!stack.isEmpty() && stack.peek()[0] >= price) {
                stack.pop();
            }

            if (!stack.isEmpty()) 
                answer[i] = stack.peek()[1] - i;

            stack.push(new int[]{price, i});
        }
        return answer;
    }
}