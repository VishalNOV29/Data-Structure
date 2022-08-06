// public class DoubleLikedList {
//     Node head;

//     class Node {
//         int data;
//         Node next;
//         Node prev;

//         public Node(int key) {
//             data = key;
//             this.next = null;
//             this.prev = null;

//         }
//     }

//     public DoubleLikedList() {
//         head = null;
//     }

//     public void insertFirst(int data) {
//         Node newNode = new Node(data);
//         if (head == null) {
//             // It means there is no any element in the linked llsit.
//             head = newNode;
//         } else {
//             newNode.next = head;
//             head.prev = newNode;
//             head = newNode;
//         }
//     }

//     public void insertLast(int data) {
//         Node newNode = new Node(data);
//         if (head == null) {
//             head = newNode;
//         } else {
//             Node temp = head;
//             while (temp.next != null) {
//                 temp = temp.next;
//             }
//             temp.next = newNode;
//             newNode.prev = temp;
//         }
//     }

//     public void show() {
//         Node temp = head;
//         while (temp != null) {
//             System.out.print(temp.data + "<->");
//             temp = temp.next;
//         }
//         System.out.println("null");

//     }

//     public void showRev() {
//         Node temp = head;
//         while (temp.next != null) {
//             temp = temp.next;
//         }
//         while (temp != null) {
//             System.out.print(temp.data + "<->");
//             temp = temp.prev;

//         }
//         System.out.println("null");
//     }

//     public void rev() {
//         Node temp = null;
//         Node current = head;
//         while (current != null) {
//             temp = current.prev;
//             current.prev = current.next;
//             current.next = temp;
//             current = current.prev;
//         }
//         if (temp != null) {
//             head = temp.prev;
//         }
//         // System.out.println(head.data);
//     }

//     public void rotate(int num) {
//         System.out.println("This method is being called.");
//         for (int i = 0; i < num; i++) {
//             System.out.println("Entering the loop "+i);
//             Node currentNode = head;
//             System.out.println("currentNode = "+currentNode.data);
//             head = head.next;
//             System.out.println("head = "+head.data);
//             Node temp = head;
//             while (temp.next != null) {
//                 temp = temp.next;
//             }
//             System.out.println("temp = "+temp.data);
//             temp.next=currentNode;
//             currentNode.prev=temp;
//             currentNode.next=null;
//             System.out.println("One rotation is completed.");
//             DoubleLikedList obj1=new DoubleLikedList();
//             obj1.show();

//         }
//         System.out.println("Process completed.");
//     }

//     public boolean isEmpty(Node head){
//         if (head==null){
//             return true;
//         }
//         return false;

//     }
//     public static void main(String[] args) {
//         DoubleLikedList obj = new DoubleLikedList();
//         boolean result = obj.isEmpty(obj.head);
//         System.out.println(result);
//         obj.insertFirst(10);
//         obj.insertFirst(20);
//         obj.insertFirst(30);
//         obj.insertFirst(40);
//         obj.insertLast(50);
//         obj.insertLast(60);
//         obj.insertLast(70);
//         obj.insertLast(80);

//     }

// }

// class DoubleLikedList {
//     Node head;

//     class Node {
//         int data;
//         Node next;
//         Node prev;

//         public Node(int key) {
//             data = key;
//             this.next = null;
//             this.prev = null;

//         }
//     }

//     public DoubleLikedList() {
//         head = null;
//     }

//     public void insertFirst(int data) {
//         Node newNode = new Node(data);
//         if (head == null) {
//             head = newNode;
//         } else {
//             newNode.next = head;
//             head.prev = newNode;
//             head = newNode;
//         }
//     }

//     public boolean isEmpty(Node head) {
//         if (head == null) {
//             return true;
//         }
//         return false;
//     }

//     public static void main(String[] args) {
//         DoubleLikedList obj = new DoubleLikedList();

//         System.out.println("Before inserting any node.");
//         System.out.println(obj.isEmpty(obj.head));

//         obj.insertFirst(20); // Inserting a node.
       
//         System.out.println("After inserting a node.");
//         System.out.println(obj.isEmpty(obj.head));
//     }
// }