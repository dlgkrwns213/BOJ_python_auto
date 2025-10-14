import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        double[] first = Arrays.stream(br.readLine().split(" "))
                .mapToDouble(Double::parseDouble)
                .toArray();
        double[] second = Arrays.stream(br.readLine().split(" "))
                .mapToDouble(Double::parseDouble)
                .toArray();

        double a1 = first[0], p1 = first[1];
        double r1 = second[0], p2 = second[1];

        double sr = a1 / p1;
        double wr = Math.PI * r1 * r1 / p2;

        System.out.println(wr > sr ? "Whole pizza" : "Slice of pizza");
    }
}