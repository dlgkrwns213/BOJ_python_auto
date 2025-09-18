import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] input = br.readLine().split(" ");
        int x = Integer.parseInt(input[0]);
        int y = Integer.parseInt(input[1]);
        
        if (x > y) {
            int temp = x;
            x = y;
            y = temp;
        }
        
        String result = IntStream.range(0, y - x)
                                 .mapToObj(i -> "1")
                                 .collect(Collectors.joining())
                        + IntStream.range(0, x)
                                   .mapToObj(i -> "2")
                                   .collect(Collectors.joining());
        
        System.out.println(result);
    }
}
