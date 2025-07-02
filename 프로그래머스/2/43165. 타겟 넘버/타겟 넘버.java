class Solution {
    public int count = 0;
    
    public int solution(int[] numbers, int target) {
        backtracking(numbers, target, 0, 0);
        return count;
    }
    
    public void backtracking(int[] numbers, int target, int idx, int make) {
        if (numbers.length == idx) {
            if (make == target)
                count++;
            return;
        }
        
        backtracking(numbers, target, idx+1, make + numbers[idx]);
        backtracking(numbers, target, idx+1, make - numbers[idx]);
    }
}