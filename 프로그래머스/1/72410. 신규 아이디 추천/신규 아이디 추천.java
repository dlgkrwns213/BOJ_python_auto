import java.util.*;

public class Solution {
    public String solution(String new_id) {
        new_id = step1(new_id);
        new_id = step2(new_id);
        new_id = step34(new_id);
        new_id = step5(new_id);
        new_id = step6(new_id);
        new_id = step7(new_id);
        return new_id;
    }

    private String step1(String id) {
        return id.toLowerCase();
    }

    private String step2(String id) {
        StringBuilder sb = new StringBuilder();
        for (char c : id.toCharArray()) {
            if (Character.isLowerCase(c) || Character.isDigit(c) || c == '-' || c == '_' || c == '.') {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    private String step34(String id) {
        String temp = id.replaceAll("\\.{2,}", ".");
        return temp.replaceAll("^\\.|\\.$", "");
    }

    private String step5(String id) {
        return id.isEmpty() ? "a" : id;
    }

    private String step6(String id) {
        id = id.length() > 15 ? id.substring(0, 15) : id;
        return id.replaceAll("\\.$", "");
    }

    private String step7(String id) {
        StringBuilder sb = new StringBuilder(id);
        while (sb.length() < 3) {
            sb.append(sb.charAt(sb.length() - 1));
        }
        return sb.toString();
    }
}