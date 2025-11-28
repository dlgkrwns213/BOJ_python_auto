import java.util.*;

public class Main {
    public static void main(String[] args) {
        String s = new Scanner(System.in).next();
        int[] w = {1,3,1,3,1,3,1,3,1,3,1,3,1};
        int idx = s.indexOf('*');

        for(int d = 0; d < 10; d++){
            int sum = 0;
            for(int i = 0; i < 13; i++){
                int val = (i == idx) ? d : s.charAt(i) - '0';
                sum += val * w[i];
            }
            if(sum % 10 == 0){
                System.out.println(d);
                break;
            }
        }
    }
}