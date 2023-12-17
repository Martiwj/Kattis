package Java;
import java.util.ArrayList;
import java.util.Scanner;

class MainEcho {

    public static ArrayList<String> echoEcho(int antall_ord, String ord) {

        String ordArray[] = ord.split("\n");
        ArrayList<String> list = new ArrayList<String>();

        for (int i = 0; i < ordArray.length; i++) {
            if (i % 2 == 0) {
                list.add(ordArray[i]);
            }
        }
        return list;

    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int antOrd = sc.nextInt();

        String ord = "";
        int teller = 0;

        sc.nextLine();

        if (antOrd >= 1 && antOrd <= 10) {
            while (teller != antOrd) {

                ord += sc.nextLine() + "\n";

                teller++;
            }

        } else {
            System.out.println("Ikke en gyldig lengde ");
            return;

        }
        for (String words : echoEcho(antOrd, ord)) {
            System.out.println(words);
        }

    }
}