import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        double x = Double.parseDouble(br.readLine());
        System.out.println(100 * 3.7854117 / (x * 1.609344));
    }
}