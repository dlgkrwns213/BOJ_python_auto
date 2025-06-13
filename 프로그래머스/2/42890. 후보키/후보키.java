import java.util.*;

class Solution {
    List<Integer> possible = new ArrayList<>();
    public int solution(String[][] relation) {
        int row = relation.length;
        int col = relation[0].length;
        
        for (int i = 1; i <= row; i++)
            backtracking(relation, i, 0, col, row, 0, 0);
        // System.out.println(possible);
        
        return possible.size();
    }
    
    public void backtracking(String[][] relation, int want, int count, int col, int row, int idx, int use) {
        if (count == want) {
            // System.out.println("use: " + use);
            boolean p = true;
            for (int poss: possible) {
                if ((use & poss) == poss)
                    p = false;
            }
            if (p)
                checking(relation, row, col, use);
            return;
        }
        
        if (col == idx)
            return;
        
        backtracking(relation, want, count, col, row, idx+1, use);
        backtracking(relation, want, count+1, col, row, idx+1, use | (1 << idx));
    }
    
    public void checking(String[][] relation, int row, int col, int use) {
        HashSet<List<String>> set = new HashSet<>();
        for (int idx = 0; idx < row; idx++) {
            List<String> now = new ArrayList<>();
            for (int i = 0; i < col; i++) {
                if (((1 << i) & use) != 0)
                    now.add(relation[idx][i]);
            }
            
            set.add(now);
        }
        
        if (set.size() == row)
            possible.add(use);
    }
}