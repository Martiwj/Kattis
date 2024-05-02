package Java;

import java.util.Scanner;

class Shandy{

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int beer = sc.nextInt(); 
        int lemonade = sc.nextInt(); 

        sc.close();

        System.out.println(pourShandy(beer, lemonade));

    }

    private static int pourShandy(int beer, int lemonade){
        if(beer == 0 || lemonade == 0){
            return 0;
        }
        return pourShandy(beer-1, lemonade-1) + 2; 
    }
}