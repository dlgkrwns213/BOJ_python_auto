import java.util.*;

class Solution {
    public String[] solution(String[] expressions) {
        int maxNumber = 0;
        List<Integer> know = new ArrayList<>();
        List<Integer> unknow = new ArrayList<>();
        
        for (int idx = 0; idx < expressions.length; idx++) {
            String[] expArr = expressions[idx].split(" ");
            
            boolean isKnow = true;
            for (int i = 0; i < 5; i += 2) {
                for (char c: expArr[i].toCharArray()) {
                    if (c != 'X')
                        maxNumber = Math.max(maxNumber, c - '0');
                    else
                        isKnow = false;
                }
            }
            
            if (isKnow)
                know.add(idx);
            else
                unknow.add(idx);
        }
        
        // 가능한 진법 찾기
        List<Integer> possible = new ArrayList<>();
        for (int num = maxNumber+1; num < 10; num++) {
            boolean isPossible = true;
            for (int idx: know) {
                String[] expArr = expressions[idx].split(" ");
                int a = change(expArr[0], num);
                String sign = expArr[1];
                int b = change(expArr[2], num);
                int x = change(expArr[4], num);
                                
                if ((sign.equals("+") && a + b != x) || (sign.equals("-") && (a - b != x))) {
                    isPossible = false;
                    break;
                }
            }
            if (isPossible)
                possible.add(num);
        }
                    
        // 진법에 대해 X값이 하나인지 확인
        String[] answer = new String[unknow.size()];
        int answerIdx = 0;
        for (int idx: unknow) {
            String[] expArr = expressions[idx].split(" ");
            HashSet<String> candX = new HashSet<>();
            for (int num: possible) {
                int a = change(expArr[0], num);
                String sign = expArr[1];
                int b = change(expArr[2], num);
                int xInt = sign.equals("+") ? a + b : a - b;
                candX.add(reChange(xInt, num));
            }
            
            String xStr = candX.size() == 1 ? candX.iterator().next() : "?";
            answer[answerIdx++] = expArr[0] + " " + expArr[1] + " " + expArr[2] + " = " + xStr;
        }
        return answer;
    }
    
    public int change(String numberString, int x) {
        int ret = 0;
        for (int i = 0; i < numberString.length(); i++) {
            ret *= x;
            ret += numberString.charAt(i) - '0';
        }
        return ret;
    }
    
    public String reChange(int number, int x) {
        StringBuilder ret = new StringBuilder();
        while (number > 0) {
            ret.append(number % x);
            number /= x;
        }
        return ret.length() > 0 ? ret.reverse().toString() : "0";
    } 
}