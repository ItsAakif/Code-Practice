import org.kociemba.twophase.Search;
import org.kociemba.twophase.Tools;
import org.kociemba.twophase.kociemba.SearchResult;

public class RubiksCubeSolver {

    public static void main(String[] args) {
        // Create a scrambled Rubik's Cube configuration
        String scramble = "R U R' U'";

        // Convert the scramble to the cube's facelet format
        String faceletScramble = Tools.fromScramble(scramble);

        // Create a new instance of the cube solver
        Search search = new Search();

        // Initialize the solver with the scrambled cube
        search.solution(faceletScramble, 21, 1000, false, SearchResult.INIT);

        // Find a solution to the cube
        int[] moveArray = new int[21];
        int length = search.solutionSearchPhase(moveArray, 0, 0, 0);

        // If a solution is found, print it
        if (length >= 0) {
            String solution = Tools.movesToString(moveArray, length);
            System.out.println("Scramble: " + scramble);
            System.out.println("Solution: " + solution);
        } else {
            System.out.println("The cube is unsolvable.");
        }
    }
}
