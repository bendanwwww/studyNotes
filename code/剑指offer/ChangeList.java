public class ChangeList {

    public static Node change(Node head) {
        Node node = head;
        Node last = null;
        while (node != null) {
            Node tmp = node.next;
            node.next = last;
            last = node;
            node = tmp;
        }
        return last;
    }

    public static void main(String[] args) {
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);
        Node newHead = ChangeList.change(head);
        System.out.println(newHead);
    }
    
}

class Node {
    int val;
    Node next;

    Node (int val) {
        this.val = val;
    }
}