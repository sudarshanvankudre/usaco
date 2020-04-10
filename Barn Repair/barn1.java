/*
ID: sudarsh11
LANG: JAVA
TASK: barn1
*/
import java.io.*;
import java.util.*;


public class barn1 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new FileReader("barn1.in"));
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("barn1.out")));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int M = Integer.parseInt(st.nextToken()); // number of boards that can be purchased
    int S = Integer.parseInt(st.nextToken()); // total number of stalls
    int C = Integer.parseInt(st.nextToken()); // number of cows in stalls
    Set<Integer> blockedStalls = new HashSet<>();
    int lowestBlockedStall = S;
    int highestBlockedStall = 1;
    String line;
    while ((line = br.readLine()) != null) {
      int stallNum = Integer.parseInt(line);
      lowestBlockedStall = Math.min(lowestBlockedStall, stallNum);
      highestBlockedStall = Math.max(highestBlockedStall, stallNum);
      blockedStalls.add(stallNum);
    }
    // we have a set of all stalls that are blocked. we now need to do the greedy search
    // to use 1 board, we need to simply cover from lowestBlockedStall to highestBlockedStall
    Map<Integer, List<Plank>> greedy = new HashMap<>(); // mapping from number of boards to list of planks
  }

  private static class Plank {
    public int start;
    public int stop;


    public Plank(int start, int stop) {
      this.start = start;
      this.stop = stop;
    }

    public Pair<Plank, Plank> split(int left, int right) {

    }
  }
}
