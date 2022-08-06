// class Node {
//     int data;
//     Node next;

//     public Node(int val) {
//         data = val;
//         next = null;
//     }
// }

// class LinkedList {
//     Node head;

//     public LinkedList() {
//         head = null;
//     }
//     void insertNode(int val){
//         Node newNode=new Node(val);
//         if (head==null){
//             head=newNode;
//         }else{
//             Node current=head;
//             while (current.next!=null){
//                 current=current.next;
//             }
//             current.next=newNode;
//         }
//     }
//     void displayNode(Node head){
//         Node current=head;
//         while (current!=null){
//             System.out.print(current.data+"->");
//             current=current.next;

//         }
//         System.out.println("null");
//     }
//     Node reverseList(Node head){
//         Node current=null;
//         Node nextNode=head;
//         while (nextNode.next!=null){
//             Node temp=nextNode.next;
//             nextNode.next=current;
//             current=nextNode;
//             nextNode=temp;

//         }
//         nextNode.next=current;
//         head=nextNode;
//         return head;
//     }
//     Node reverseBetweenIndex(Node head,int left,int right){
//         if (head==null || head.next==null){
//             return head;
//         }
//         Node current=null;
//         Node nextNode=head;
//         int count=1;
//         while (count<left){
//             current=nextNode;
//             nextNode=nextNode.next;
//             count+=1;
//         }
//         Node temp1=current;
//         Node temp2=nextNode;
//         current=nextNode;
//         nextNode=nextNode.next;
//         count+=1;
//         while (count<=right){
//             Node temp=nextNode.next;
//             nextNode.next=current;
//             current=nextNode;
//             nextNode=temp;
//             count+=1;
//         }
//         Node temp3=current;
//         temp2.next=nextNode;

//         if (temp1!=null){
//             System.out.println("temp1 ="+temp1.data);
//             temp1.next=temp3;
//         }
//         if (temp1==null){
//             head=temp3;
//         }
        
//         return head;
//     }
//     public static void main(String[] args){
//         LinkedList obj=new LinkedList();
//         System.out.println(obj.head);
//         obj.insertNode(1);
//         obj.insertNode(2);
//         obj.insertNode(3);
//         obj.insertNode(4);
//         obj.insertNode(5);
//         // obj.insertNode(6);
//         // obj.insertNode(7);
//         // obj.insertNode(8);
//         // obj.insertNode(9);
//         // obj.insertNode(10);
//         obj.displayNode(obj.head);
//         // Node res=obj.reverseList(obj.head);
//         // obj.displayNode(res);
//         Node res1=obj.reverseBetweenIndex(obj.head, 2, 4);
//         obj.displayNode(res1);
//     }
// }