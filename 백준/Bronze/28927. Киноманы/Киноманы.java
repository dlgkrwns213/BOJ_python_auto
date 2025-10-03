import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] maxData = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] melData = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int maxTime = maxData[0] * 3 + maxData[1] * 20 + maxData[2] * 120;
        int melTime = melData[0] * 3 + melData[1] * 20 + melData[2] * 120;

        if (maxTime > melTime) {
            System.out.println("Max");
        } else if (melTime > maxTime) {
            System.out.println("Mel");
        } else {
            System.out.println("Draw");
        }
    }
}