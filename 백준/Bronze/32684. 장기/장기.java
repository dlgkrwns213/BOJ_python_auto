import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] score = {13, 7, 5, 3, 3, 2};

        int[] a = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] b = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        double aScore = IntStream.range(0, 6)
                .mapToDouble(i -> a[i] * score[i])
                .sum();

        double bScore = IntStream.range(0, 6)
                .mapToDouble(i -> b[i] * score[i])
                .sum() + 1.5;

        System.out.println(aScore > bScore ? "cocjr0208" : "ekwoo");
    }
}