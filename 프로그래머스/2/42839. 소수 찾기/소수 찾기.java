import java.util.*;


class Solution {
    public HashSet<Integer> ans = new HashSet<>();
    
    public int solution(String numbers) {
        int n = numbers.length();
        
        int[] numberInts = new int[n];
        for (int idx = 0; idx < n; idx++)
            numberInts[idx] = numbers.charAt(idx) - '0';
            
        backtracking(numberInts, n, new boolean[n], 0);    
        return ans.size();
    }
    
    public void backtracking(int[] numberInts, int n, boolean[] visited, int make) {
        if (isPrime(make))
            ans.add(make);
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                backtracking(numberInts, n, visited, make*10 + numberInts[i]);
                visited[i] = false;
            }
        }
    }
    
    public boolean isPrime(int n) {
        if (n == 0 || n == 1)
            return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0)
                return false;
        }
        return true;
    }
}