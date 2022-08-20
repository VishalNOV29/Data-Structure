class DoublyLinedList {
    Node head;

    class Node {
        int data;
        Node next;
        Node prev;

        Node(int num) {
            data = num;
            next = prev = null;

        }
    }

    DoublyLinedList() {
        head = null;
    }

    void insertData(int num) {
        Node newNode = new Node(num);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
            newNode.prev=current;
        }
    }

    void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + "<->");
            current=current.next;
        }
        System.out.println("null");
    }
    // There will be three cases of insertion. 1. The data will be inserted at the begining of the linked list. 2. The data will be inserted at the end of the list. 
    // 3. The data will be inserted any where in the middle of the linked list.

    // Here we will have to handle any two cases. Because if we start comparing the number with the current node data then we have two option
    // 1. Insert new node after the current node. and 2. insert new node previous of the current node.

    // Here the data will be iserted previous to the current node.
    void insertSorted(int num){
        Node newNode=new Node(num);
        // System.out.println(newNode.next);
        // System.out.println(newNode.prev);

        // In this case there is no any element in the linked list.
        if (head==null){
            System.out.println("There is no any element in the list.");
            head=newNode;
            return;
        }
        // This is the case where data will be inserted at the begining of the list.
        if (num<head.data){
            System.out.println("Node will be inserted at the begining of the list.");
            newNode.next=head;
            head.prev=newNode;
            head=newNode;
            return;
        }
        Node current=head;
        while (current.data<num && current.next!=null){
            current=current.next;
        }
        if (current.next==null && current.data<num){
            System.out.println("Node will be inserted at the end of the list.");
            current.next=newNode;
            newNode.prev=current;
            return;
        }
        current.prev.next=newNode;
        newNode.next=current;
        newNode.prev=current.prev;
        current.prev=newNode;

        System.out.println(current.data);

    }

    public static void main(String[] args) {
        System.out.println("Code is running correctly.");
        DoublyLinedList obj=new DoublyLinedList();
        obj.insertData(1);
        obj.insertData(2);
        obj.insertData(10);
        obj.display();
        obj.insertSorted(5);
        obj.display();

        obj.insertSorted(11);
        obj.display();
        obj.insertSorted(0);
        obj.display();

        obj.insertSorted(8);
        obj.display();

        obj.insertSorted(8);
        obj.display();
    }
}