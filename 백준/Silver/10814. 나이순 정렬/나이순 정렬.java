import java.io.*;
import java.util.*;

public class Main {
    private static class Person {
        int age;
        String name;

        Person(int age, String name) {
            this.age = age;
            this.name = name;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Person[] people = new Person[n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            people[i] = new Person(Integer.parseInt(st.nextToken()), st.nextToken());
        }

        Arrays.sort(people, Comparator.comparing((Person person) -> person.age));

        StringBuilder answer = new StringBuilder();
        for (Person person: people)
            answer.append(person.age).append(' ').append(person.name).append('\n');
        System.out.println(answer);
    }
}