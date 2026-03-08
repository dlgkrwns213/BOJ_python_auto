import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] ck = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int c = ck[0];
        int k = ck[1];

        int u = (int) Math.pow(10, k);

        System.out.println(((c + u/2) / u) * u);
    }
}