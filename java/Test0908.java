import java.util.ArrayList;
import java.util.List;

public class Test0908 {

    class Node {
        int val;
        Node next;
    }

    public void changeList(Node head) {
        Node index = head;
        Node last = null;
        while (index != null) {
            Node tmp = index.next;
            index.next = last;
            last = index;
            index = tmp;
        }
        head = last;
    }

    public Node changeList2(Node node) {
        List<Node> list = new ArrayList<>();
        while (node != null) {
            list.add(node);
            node = node.next;
        }
        Node head = list.get(list.size() - 1);
        while (list.size() > 0) {
            Node f = list.remove(list.size() - 1);
            if (list.size() > 0) {
                f.next = list.get(list.size() - 1);
            } else{
                f.next = null;
            }
        }
        return head;
    }
}


