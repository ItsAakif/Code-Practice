// Program to check  if entered number is prime or not by Aakif Mudel 
import java.util.Scanner;

public class PrimeNumberChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = scanner.nextInt();

        boolean isPrime = true;

        if (number <= 1) {
            isPrime = false;
        } else if (number <= 3) {
            // Numbers 2 and 3 are prime, no need to check further
            isPrime = true;
        } else if (number % 2 == 0 || number % 3 == 0) {
            // Numbers divisible by 2 or 3 are not prime
            isPrime = false;
        } else {
            int divisor = 5;
            int divisorSquared = divisor * divisor;
            while (divisorSquared <= number) {
                if (number % divisor == 0 || number % (divisor + 2) == 0) {
                    isPrime = false;
                    break;
                }
                divisor += 6;
                divisorSquared = divisor * divisor;
            }
        }

        if (isPrime) {
            System.out.println(number + " is a prime number.");
        } else {
            System.out.println(number + " is not a prime number.");
        }

        scanner.close();
    }
}
