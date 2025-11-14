import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        float w = Float.parseFloat(br.readLine());
        float h = Float.parseFloat(br.readLine());

        float bmi = w / (h * h);

        if (bmi > 25) {
            System.out.println("Overweight");
        } else if (bmi >= 18.5) {
            System.out.println("Normal weight");
        } else {
            System.out.println("Underweight");
        }
    }
}