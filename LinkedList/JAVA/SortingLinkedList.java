// class Node{
//     int data;
//     Node next;
//     public Node(int key){
//         data=key;
//         next=null;
//     }
// }
// class LinkedList{
//     Node head;
//     public LinkedList(){
//         head=null;
//     }
//     public void insertEle(int data){
//         Node newNode=new Node(data);
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
//     public void display(){
//         Node current=head;
//         while (current!=null){
//             System.out.print(current.data+"->");
//             current=current.next;
//         }
//         System.out.println();
//     }
//     public void sortList(){
//         Node current=head;
//         while (current.next!=null){
//             System.out.println("current = "+current.data);
//             Node temp=current.next;
//             while (temp!=null){
//                 System.out.println("temp = "+temp.data);
//                 if (temp.data<current.data){
//                     int data=current.data;
//                     current.data=temp.data;
//                     temp.data=data;
//                 }
//                 temp=temp.next;
//             }
//             current=current.next;
//         }
//     }
//     public static void main(String[] args){
//         // System.out.println("Code is runnig correctly: ");
//         LinkedList obj=new LinkedList();
//         obj.insertEle(1);
//         obj.insertEle(2);
//         obj.insertEle(2);
//         obj.insertEle(3);
//         obj.insertEle(5);
//         obj.insertEle(4);
//         obj.display();
//         obj.sortList();
//         obj.display();
//     }
// }