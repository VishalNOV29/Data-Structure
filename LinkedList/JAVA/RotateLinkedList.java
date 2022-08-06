// public class RotateLinkedList {
//     class Node {
//         int data;
//         Node next;

//         public Node(int val) {
//             data = val;

//         }
//     }

//     Node head;

//     public RotateLinkedList() {
//         head = null;
//     }

//     public void addElement(int data) {
//         Node newNode = new Node(data);
//         if (head == null) {
//             head = newNode;
//         } else {
//             Node temp = head;
//             while (temp.next != null) {
//                 temp = temp.next;
//             }
//             temp.next = newNode;
//         }
//     }

//     public void display(Node head) {
//         Node temp = head;
//         while (temp != null) {
//             System.out.print(temp.data + "->");
//             temp = temp.next;
//         }
//         System.out.println("null");
//     }

//     public Node rotateList(Node head, int k) {
//         Node temp = head;
//         if (head == null || head.next == null) {
//             return head;
//         }
//         int length = 1;
//         while (temp.next != null) {

//             length++;

//             temp = temp.next;
//         }
//         k = k % length;
//         k = length - k;
//         temp.next = head;
//         System.out.println("temp.next ="+temp.next.data);
//         for (int j = k; j > 0; j--) {
//             temp = temp.next;
//         }
//         System.out.println("temp.next ="+temp.next.data);
//         head = temp.next;
//         System.out.println("newHead ="+head.data);
//         temp.next = null;
//         return head;

//     }

//     public static void main(String[] args) {
//         RotateLinkedList obj = new RotateLinkedList();
//         obj.addElement(1);
//         obj.addElement(2);
//         obj.addElement(3);
//         obj.addElement(4);
//         obj.addElement(5);
//         obj.display(obj.head);
//         Node newHead = obj.rotateList(obj.head, 2);
//         obj.display(newHead);
//     }
// }
