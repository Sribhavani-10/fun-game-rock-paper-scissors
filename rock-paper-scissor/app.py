import java.util.Scanner;
import java.util.Random;

public class RockPaperScissors {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random random = new Random();

        String[] choices = {"Rock", "Paper", "Scissors"};
        System.out.println("Welcome to Rock, Paper, Scissors Game!");
        
        while (true) {
            System.out.print("Enter your choice (Rock, Paper, Scissors or Exit): ");
            String userChoice = sc.nextLine().trim();

            if (userChoice.equalsIgnoreCase("Exit")) {
                System.out.println("Thanks for playing!");
                break;
            }

            // Validate user input
            if (!userChoice.equalsIgnoreCase("Rock") &&
                !userChoice.equalsIgnoreCase("Paper") &&
                !userChoice.equalsIgnoreCase("Scissors")) {
                System.out.println("Invalid input! Try again.");
                continue;
            }

            // Computer's turn
            int computerIndex = random.nextInt(3);
            String computerChoice = choices[computerIndex];
            System.out.println("Computer chose: " + computerChoice);

            // Determine the winner
            if (userChoice.equalsIgnoreCase(computerChoice)) {
                System.out.println("It's a Tie!");
            } else if (
                (userChoice.equalsIgnoreCase("Rock") && computerChoice.equals("Scissors")) ||
                (userChoice.equalsIgnoreCase("Paper") && computerChoice.equals("Rock")) ||
                (userChoice.equalsIgnoreCase("Scissors") && computerChoice.equals("Paper"))
            ) {
                System.out.println("You Win!");
            } else {
                System.out.println("You Lose!");
            }

            System.out.println();
        }

        sc.close();
    }
}