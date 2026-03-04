import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int[] u = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        
        int[] d = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        
        int[] p = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        
        int h = Integer.parseInt(br.readLine());
        
        int t = 0;
        int damage = 0;
        while (true) {
            if (t % u[0] == 0) damage += u[1];
            if (t % d[0] == 0) damage += d[1];
            if (t % p[0] == 0) damage += p[1];
            
            if (damage >= h) {
                System.out.println(t);
                break;
            }
            
            t++;
        }
    }
}