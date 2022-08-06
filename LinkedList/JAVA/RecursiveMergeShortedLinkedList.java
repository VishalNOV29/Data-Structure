// class Hello1 {
//     Node head;

//     public Hello1() {
//         head = null;
//     }

//     public static void main(String[] args) {
//         // System.out.println("Hello");
//         Hello1 obj1 = new Hello1();
//         obj1.insert(10);
//         obj1.insert(20);
//         obj1.insert(30);
//         obj1.insert(40);
//         obj1.show(obj1.head);
//         Hello1 obj2 = new Hello1();
//         obj2.insert(50);
//         obj2.insert(60);
//         obj2.insert(70);
//         obj2.insert(80);
//         obj2.insert(90);
//         obj2.insert(100);
//         obj2.show(obj2.head);
//         Hello1 obj3 = new Hello1();
//         Node reuslt = obj3.recursiveMerge(obj1.head, obj2.head);
//         System.out.println("After this result will be shown.");
//         obj3.show(reuslt);

//     }

//     class Node {
//         Node next;
//         int data;

//         public Node(int key) {
//             data = key;
//             next = null;
//         }
//     }

//     public void insert(int data) {
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

//     public void show(Node head) {
//         Node temp = head;
//         while (temp != null) {
//             System.out.print(temp.data + "->");
//             temp = temp.next;
//         }
//         System.out.println("null");
//     }

//     // public Node merge(Node head1, Node head2) {
//     //     Node head = new Node(-1);
//     //     Node temp = head;
//     //     while (head1 != null && head2 != null) {
//     //         if (head1.data < head2.data) {
//     //             temp.next = head1;
//     //             head1 = head1.next;
//     //             temp = temp.next;
//     //         } else {
//     //             temp.next = head2;
//     //             head2 = head2.next;
//     //             temp = temp.next;
//     //         }
//     //     }
//     //     while (head1 != null) {
//     //         temp.next = head1;
//     //         head1 = head1.next;
//     //         temp = temp.next;
//     //     }
//     //     while (head2 != null) {
//     //         temp.next = head2;
//     //         head2 = head2.next;
//     //         temp = temp.next;
//     //     }
//     //     return head.next;

//     // }
//     public Node recursiveMerge(Node head1,Node head2){
//         Node head=new Node(-1);
//         if (head1==null){
//             return head2;
//         }
//         if (head2==null){
//             return head1;
//         }
//         Node temp=head;
//         if (head1.data<head2.data){
//             temp.next=recursiveMerge(head1.next, head2);
//         }else{
//             temp.next=recursiveMerge(head1, head2.next);
//         }
//         return head.next;
//     }
// }