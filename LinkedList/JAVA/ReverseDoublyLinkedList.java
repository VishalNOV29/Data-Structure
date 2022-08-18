public class ReverseDoublyLinkedList {
    class Node{
        int data;
        Node next;
        Node prev;
        Node(int num){
            data=num;
            next=null;
            prev=null;
        }

    }
    Node head;
    ReverseDoublyLinkedList(){
        head=null;
    }
    void insertNode(int data){
        Node newNode=new Node(data);
        if (head==null){
            head=newNode;
        }
        else{
            Node temp=head;
            while (temp.next!=null){
                temp=temp.next;

            }
            temp.next=newNode;
            newNode.prev=temp;
        }
    }
    void display(){
        Node temp=head;
        while (temp!=null){
            System.out.print(temp.data+"<->");
            temp=temp.next;
        }
        System.out.println("null");
    }
    void reverseList(){
        Node current=head;
        while (current.next!=null){
            System.out.println("current = "+current.data);
            Node temp=current.next;
            current.next=current.prev;
            current.prev=temp;
            // System.out.println("current.next = "+current.next.data);
            // System.out.println("current.prev = "+current.prev.data);
            current=temp;
           
        }
        current.next=current.prev;
        current.prev=null;

        head=current;
    }
    // This mehtod is more easy to understand than the previous one.
    void reverseList1(){
        Node current=head;
        Node prevNode=current.prev;
        while (current!=null){
            prevNode=current.prev;
            current.prev=current.next;
            current.next=prevNode;
            prevNode=current;
            current=current.prev;

        }
        head=prevNode;
    }
    public static void main(String[] args){
        ReverseDoublyLinkedList obj=new ReverseDoublyLinkedList();
        obj.insertNode(1);
        obj.insertNode(2);
        obj.insertNode(3);
        obj.insertNode(4);
        obj.insertNode(5);
        obj.insertNode(6);
        obj.insertNode(7);
        obj.insertNode(8);
        obj.insertNode(9);
        obj.display();
        obj.reverseList1();
        obj.display();
        
    }
    
}
