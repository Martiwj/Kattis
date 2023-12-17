package Java;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class MainTeque {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Teque tq = new Teque();
        int range = Integer.parseInt(br.readLine());

        for (int i = 0; i < range; i++) {
            String[] linje = br.readLine().split(" ");
            String komando = linje[0];
            int verdi = Integer.parseInt(linje[1]);

            switch (komando) {
                case "push_back":
                    tq.push_back(verdi);
                    break;

                case "push_front":
                    tq.push_front(verdi);
                    break;

                case "push_middle":
                    tq.push_middle(verdi);
                    break;

                case "get":
                    bw.write(tq.get(verdi) + "\n");
                    break;

                default:
                    System.exit(0);
            }
        }

        bw.flush(); 
        br.close();
        bw.close();
    }
}
