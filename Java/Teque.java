package Java;

import java.util.ArrayList;

class Teque {

    ArrayList<Integer> front;
    ArrayList<Integer> back;

    public Teque() {
        front = new ArrayList<Integer>();
        back = new ArrayList<Integer>();
    }

    public void balance() {
        if (this.size() == 1 && back.size() == 0) {
            return;
        }
        int diff = front.size() - back.size();

        if (diff > 1) {
            back.add(0, front.remove(front.size() - 1));
        }

        if (diff <= -1) {
            front.add(back.remove(0));
        }
    }

    public void push_front(int x) {
        front.add(0, x);
        this.balance();
    }

    public void push_back(int x) {
        back.add(x);
        this.balance();
    }

    public void push_middle(int x) {
        int frontSize = front.size();
        int middle = Math.round((frontSize + back.size() + 1) / 2);

        if (frontSize <= middle) {
            back.add(0, x);
        } else {
            front.add(middle, x);
        }
        this.balance();
    }

    public int size() {
        return front.size() + back.size();
    }

    public int get(int x) {
        int front_size = front.size();
        if (x < front_size) {
            return front.get(x);
        }
        return back.get(x - front_size);
    }
}