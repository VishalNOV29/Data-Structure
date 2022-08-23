public class RemoveDuplicateSortedLinkedList {
    class Node {
        int data;
        Node next;

        Node(int num) {
            data = num;
            next = null;
        }
    }

    Node head;

    RemoveDuplicateSortedLinkedList() {
        head = null;
    }

    void insertNode(int num) {
        Node newNode = new Node(num);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + "->");
            current=current.next;
        }
        System.out.println("null");
    }
    void removeDuplicates(){
        Node temp=head;
        while (temp.next!=null){
            Node current=temp.next;
            while (current.next!=null){
                if (current.data!=temp.data){
                    break;
                }
                current=current.next;
                if (current.next==null){
                    break;
                }
            }

            // This case for a single repeating element. There may be a case in which only a single element repeats many time and the 
            // current pointer also contain the same element. Hence if this case arises then this code will be executed.
            if (temp.data==current.data){
                temp.next=null;
                return ;
            }
            temp.next=current;
            temp=temp.next;

        }
    }
    public static void main(String[] args) {
        System.out.println("Code is running well");
        RemoveDuplicateSortedLinkedList obj=new RemoveDuplicateSortedLinkedList();
       obj.insertNode(3);
       obj.insertNode(3);
       obj.insertNode(3);
       obj.insertNode(4);
       obj.insertNode(5);
       obj.insertNode(5);
        obj.display();
        obj.removeDuplicates();
        obj.display();

    }
}
