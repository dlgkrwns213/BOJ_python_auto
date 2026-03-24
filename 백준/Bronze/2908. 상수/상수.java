import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] ab = br.readLine().split(" ");
        String a = ab[0];
        String b = ab[1];

        String reverseA = new StringBuilder(a).reverse().toString();
        String reverseB = new StringBuilder(b).reverse().toString();

        System.out.println(Integer.parseInt(reverseA) > Integer.parseInt(reverseB) ? reverseA : reverseB);
    }
}