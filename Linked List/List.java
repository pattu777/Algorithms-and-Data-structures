import java.util.*;


/*
 * Linked List class
 */
public class List<T> {

    private Node<T> head;

    /*
     * Node class
     */
    class Node<T> {

        T data;
        Node<T> next;

        public Node() {}

        public Node(T a) {
            this.data = a;
            this.next = null;
        }

        public Node(Node<T> nd) {
            this.data = nd.data;
            this.next = nd.next;
        }
    }

    /*
     * public constructor
     */
    public List() {
        this.head = null;
    }

    /*
     * Return the number of elements in the list.
     *
     * Time Complexity - O(n)
     * Space Complexity - O(1)
     */
    public int count() {
        Node<T> tmp = this.head;
        int count = 0;
        while(tmp != null) {
            tmp = tmp.next;
            count++;
        }
        return count;
    }

    /*
     * Insert a node at the beginning.
     *
     * Time Complexity - O(1)
     * Space Complexity - O(1)
     */
    public void insertAtHead(T a) {
        Node<T> nd = new Node<T>(a);
        nd.next = this.head;
        this.head = nd;
    }

    /*
     * Insert a node at the end of the linked list.
     *
     * Time Complexity - O(n)
     * Space Complexity - O(1)
     */
    public void insertAtEnd(T a) {
        Node<T> nd = this.head;
        while(nd.next != null) {
            nd = nd.next;
        }

        Node<T> tmp = new Node<T>(a);
        nd.next = tmp;
    }

    /*
     * Remove an element from the head.
     *
     * Time Complexity - O(1)
     * Space Complexity - O(1)
     */
    public void removeFromHead() {
        Node<T> nd = this.head;
        this.head = nd.next;
        nd = null;
    }

    /*
     * Remove an element from the tail.
     *
     * Time Complexity - O(n)
     * Space Complexity - O(1)
     */
    public void removeFromTail() {

    }

    /*
     * Search an element in a linked list.
     *
     * Time Complexity - O(n)
     * Space Complexity - O(1)
     */
    public boolean search(T a) {
        Node<T> nd = this.head;
        while(nd != null) {
            if(nd.data == a) {
                return true;
            }
            nd = nd.next;
        }
        return false;
    }

    /*
     * Reverse a linked list iteratively.
     *
     * Time Complexity - O(n)
     * Space Complexity - O(1)
     */
    public void reverse() {
        Node<T> current = this.head;
        Node<T> prev = null;
        Node<T> tmp = null;
        while(current != null) {
            tmp = current.next;
            current.next = prev;
            prev = current;
            current = tmp;
        }
        this.head = prev;
    }

    /*
     * Display all the elements of the list.
     *
     * Time Complexity - O(n)
     * Space Complexity - O(1)
     */
    public void display() {
        Node<T> tmp = this.head;
        while(tmp != null) {
            System.out.println(tmp.data);
            tmp = tmp.next;
        }
    }

    public static void main(String[] args) {

        List<Integer> nd = new List<Integer>();
        nd.insertAtHead(12);
        nd.insertAtHead(312);
        nd.insertAtHead(-153);
        nd.insertAtHead(678);
        nd.insertAtHead(7854);

        //for(int i=1000; i<1010; i++)
          //  nd.insertAtEnd(i);
        
        nd.display();

        System.out.println("Number of elements - " + nd.count());
        nd.reverse();
        nd.display();
    }
}
