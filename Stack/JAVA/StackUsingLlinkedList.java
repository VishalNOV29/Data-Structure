// Creating a node.
class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}
// Creating a stack.
class Stack {
    Node head;

    public Stack() {
        head = null;
    }

    void push(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            System.out.println("Inserted: " + newNode.data);
        } else {
            newNode.next = head;
            head = newNode;
            System.out.println("Inserted: " + newNode.data);
        }
    }
}
class Test{
    public static void main(String args[]){
        Stack obj=new Stack();
        obj.push(24);
        obj.push(25);
        obj.push(26);
        

    }
}
