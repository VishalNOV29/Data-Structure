// // import java.rmi.RemoteException;

// public class RemoveDuplicate {
//     class Node {
//         int data;
//         Node next;

//         public Node(int key) {
//             this.data = key;
//             this.next = null;
//         }
//     }

//     Node head;

//     public RemoveDuplicate() {
//         head = null;
//     }

//     public void insertNode(int val) {
//         Node newNode = new Node(val);
//         System.out.println(newNode.data);
//         if (head == null) {
//             head = newNode;
//         } else {
//             Node current = head;
//             while (current.next != null) {
//                 current = current.next;
//             }
//             current.next = newNode;
//         }
//     }

//     public void display() {
//         Node current = head;
//         while (current != null) {
//             System.out.print(current.data + "->");
//             current = current.next;
//         }
//         System.out.println();
//     }

//     public void removeDuplicate() {
        

//     }

//     public static void main(String[] args) {
//         RemoveDuplicate obj = new RemoveDuplicate();
//         obj.insertNode(1);
//         obj.insertNode(2);
//         // obj.insertNode(2);
//         // obj.insertNode(2);
//         // obj.insertNode(2);
//         obj.insertNode(2);
//         obj.insertNode(3);
//         // obj.insertNode(3);
//         // obj.insertNode(3);
//         // obj.insertNode(3);
//         // obj.insertNode(3);
//         // obj.insertNode(4);
//         obj.insertNode(4);
//         // obj.insertNode(4);
//         // obj.insertNode(4);
//         // obj.insertNode(4);
//         obj.insertNode(5);
//         obj.insertNode(5);
//         obj.display();
//         obj.removeDuplicate();
//         obj.display();
//     }
// }
