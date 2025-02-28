import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args){
        boolean[] d = new boolean[10001];
        for (int num=1; num<10000; num++) {
            int make = num + String.valueOf(num)
                    .chars()
                    .map(c -> c - '0')
                    .sum();

            if (make < 10001)
                d[make] = true;
        }

        IntStream.range(1, 10000)
                .filter(num -> !d[num])
                .forEach(System.out::println);
    }
}