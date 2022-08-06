// public class Recursion {
//     void showStr(String str){
//         if (str.length()==0 || str==null){
//             return ;
//         }

//     }

// }

// import java.util.*;

// class Recursion {
//     /* Function to print reverse of the passed string */
//     void reverse(String str) {
//         if ((str == null) || (str.length() <= 1))
//             System.out.println(str);
//         else {
//             System.out.print(str.charAt(str.length() - 1));
//             reverse(str.substring(0, str.length() - 1));
//         }
//     }

//     // Function to print string.
//     void show(String str) {
//         if (str == null || str.length() <= 1) {
//             System.out.print(str);
//         } else {
//             System.out.print(str.charAt(0));
//             show(str.substring(1, str.length()));
//         }
//     }

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter a line of text: ");
//         String str = sc.nextLine();
//         sc.close();
//         Recursion obj = new Recursion();
//         System.out.print("You entered : ");
//         obj.show(str);
//         System.out.println();
//         System.out.print("Reverse of text : ");
//         obj.reverse(str);

//     }
// }

// class InventoryNode {
//     private String item;
//     private int numberOfItems;
//     private InventoryNode nextNodeRef;

//     public InventoryNode() {
//         item = "";
//         numberOfItems = 0;
//         nextNodeRef = null;
//         InventoryNode head=null;
//     }

//     public InventoryNode(String itemInit, int numberOfItemsInit) {
//         this.item = itemInit;
//         this.numberOfItems = numberOfItemsInit;
//         this.nextNodeRef = null;
//     }

//     public InventoryNode(String itemInit, int numberOfItemsInit, InventoryNode nextLoc) {
//         this.item = itemInit;
//         this.numberOfItems = numberOfItemsInit;
//         this.nextNodeRef = nextLoc;
//     }

//     public InventoryNode getNext() {
//         return this.nextNodeRef;
//     }

//     public void printNodeData() {
//         System.out.println(this.numberOfItems + " " + this.item);
//     }

//     public void insertAtFront(){
//         InventoryNode newNode=new InventoryNode();
//         InventoryNode temp=head;

//     }

// }

// import numpy as

// class MyThread1 extends Thread {
//     long value1=0;
//     @Override
//     public void run() {
//         for (long i=250000000;i<=500000000;i++){
//             value1+=i;
//         }
//         System.out.println(value1);
        
//     }
//     public long getValue(){
//         return value1;
//     }
// }

// class MyThread2 extends Thread {
//     long value2=0;
//     @Override
//     public void run() {
//         for (long i=0;i<250000000;i++){
//             value2+=i;
//         }
//     }
//     public long getValue(){
//         return value2;
//     }
// }
// class Main{
//     public static void main(String args[]){
//         MyThread1 t1=new MyThread1();
//         MyThread2 t2=new MyThread2();
//         t1.start();
//         t2.start();
//         System.out.println("value 1 ="+t1.value1);
//         System.out.println(t2.value2);
//         long res=t1.getValue()+t2.getValue();
//         System.out.println("Result = "+res);
//     }
// }

// class MyThread1 extends Thread{
//     long value1=0;
//     @Override
//     public void run(){
//         System.out.println("Thread2 is called.");
//         for (int i=0;i<250000000;i++){
//             value1+=i;
//         }
//         System.out.println("value1 = "+value1);
//     }
//     public long getValue(){
//         System.out.println("This method is called"+value1);
//         return value1;
//     }
// }
// class MyThread2 extends Thread{
//     long value2=0;
//     @Override
//     public void run(){
//         System.out.println("Thread2 is called.");
//         for (int i=250000000;i<=500000000;i++){
//             value2+=i;
//         }
//         System.out.println("value2 = "+value2);
//     }
//     public long getValue(){
//         System.out.println("This method is called."+value2);
//         return value2;
//     }
// }
// class Main{
//     public static void main(String[] args){
//         MyThread1 t1=new MyThread1();
//         MyThread2 t2=new MyThread2();
//         t1.start();
//         t2.start();

//         System.out.println("HEllo");
//         long res=t1.value1+t2.value2;
//         System.out.println(res);

//     }
// }