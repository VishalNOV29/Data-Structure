// // import java.util.spi.CurrencyNameProvider;

// class RemoveNthElement {
//     class Node {
//         int data;
//         Node next;

//         public Node(int val) {
//             data = val;

//         }
//     }

//     Node head;

//     public RemoveNthElement() {
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
//     public Node removeNth(Node head,int n){
//         if (head==null){
//             return head;
//         }else{
//             Node temp=head;
//             int length=1;
//             while (temp.next!=null){
//                 length++;
//                 temp=temp.next;
//             }
//             n=length-n;
//             Node current=head;
//             int i=1;
//             while (i!=n){
//                 i++;
//                 current=current.next;
//             }
//             System.out.println("current ="+current.data);
//             // head=current.next.next;
//             current.next=current.next.next;
//             // System.out.println("current.next.next "+current.next.next.data);
//             return head;

//         }

//     }

//     public static void main(String[] args) {
//         RemoveNthElement obj = new RemoveNthElement();
//         obj.addElement(1);
//         obj.addElement(2);
//         // obj.addElement(3);
//         // obj.addElement(4);
//         // obj.addElement(5);

//         obj.display(obj.head);
//         // Node newHead = obj.rotateList(obj.head, 2);
//         // obj.display(newHead);
//         Node newHead=obj.removeNth(obj.head, 1);
//         obj.display(newHead);
//     }
// }
