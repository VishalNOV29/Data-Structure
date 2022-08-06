// import java.util.ArrayList;

// // import java.util.ArrayList;

// class Node {
//     int data;
//     Node next;

//     public Node(int data) {
//         this.data = data;
//         next = null;
//     }
// }

// class LinkedList {
//     Node head;

//     public LinkedList() {
//         head = null;
//     }

//     void addFirst(int data) {
//         Node newNode = new Node(data);
//         if (head == null) {
//             head = newNode;
//         } else {
//             newNode.next = head;
//             head = newNode;
//         }

//     }

//     void addLast(int data) {
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

//     void display() {
//         if (head == null) {
//             System.out.println("LinkedList is empty.");
//         } else {
//             Node temp = head;
//             while (temp != null) {
//                 System.out.printf(temp.data + "-->");
//                 temp = temp.next;
//             }
//             System.out.println("null");

//         }
//     }

//     void reverse() {
//         Node current = head;
//         Node next = null;
//         Node prev = null;

//         while (current != null) {
//             next = current.next;
//             current.next = prev;
//             prev = current;
//             current = next;
//         }
//         head = prev;
//     }
//     // void delBetween(int left,int right){
//     // Node currentNode=head;
//     // int i=1;
//     // while (i!=left){
//     // i++;
//     // currentNode=currentNode.next;
//     // }
//     // System.out.println("currnetNode ="+currentNode.data);
//     // Node lastNode=currentNode;
//     // int j=i;
//     // while (j!=right){
//     // lastNode=lastNode.next;
//     // j++;
//     // }
//     // System.out.println("lastNode = "+lastNode.data);
//     // lastNode=lastNode.next;
//     // Node nextNode=currentNode.next;
//     // head.next=lastNode;
//     // while (currentNode!=null && nextNode!=null){
//     // Node temp=nextNode.next;
//     // nextNode.next=currentNode;
//     // currentNode=nextNode;
//     // nextNode=temp;
//     // }

//     // }

//     void midDelete() {
//         Node temp = head;
//         int countNode = 0;
//         while (temp != null) {
//             countNode++;
//             temp = temp.next;
//         }
//         System.out.println(countNode);
//         int pos = Math.floorDiv(countNode, 2);
//         System.out.println("Positon to be deleted = " + pos);
//         int i = 0;
//         Node current = head;
//         while (i != pos) {
//             current = current.next;
//             i++;
//         }
//         System.out.println("Node to be deleted =" + current.data);
//         if (current.next == null) {
//             current = null;
//         } else {
//             current.data = current.next.data;
//             current.next = current.next.next;
//         }
//     }

//     Node removeDuplicate() {
//         Node temp = head;
//         while (temp != null) {
//             Node check = temp.next;
//             while (check.data == temp.data) {
//                 check = check.next;
//                 if (check == null) {
//                     break;
//                 }
//             }
//             temp.next = check;
//             temp = temp.next;
//         }
//         return head;
//     }
// }

// public class Main {
//     public static void main(String[] args) {
//         LinkedList obj = new LinkedList();
//         obj.addLast(1);
//         obj.addLast(1);
//         obj.addLast(1);
//         obj.addLast(2);
//         obj.addLast(2);
//         obj.addLast(2);
//         obj.addLast(3);
//         obj.addLast(3);
//         obj.addLast(4);
//         obj.addLast(4);
//         obj.addLast(5);
//         obj.addLast(5);
//         obj.addLast(6);
//         obj.addLast(6);
//         obj.addLast(7);
//         obj.addLast(7);
//         obj.addLast(7);
//         obj.addLast(7);
//         obj.addLast(8);
//         obj.addLast(8);
//         obj.addLast(9);
//         obj.addLast(9);
//         obj.addLast(10);
//         obj.addLast(10);
//         obj.addLast(10);
//         obj.display();
//         // obj.reverse();
//         // obj.display();
//         // obj.midDelete();
//         // obj.display();
//         // obj.delBetween(2, 5);
//         // obj.display();
//         obj.removeDuplicate();
//         obj.display();
//     }
// }

// class Course{
//     private String courseCode;
//     private double examMark;
//     private double courseWorkMark;
//     public static int  noOfCourse=0;
//     public Course(String name,double num1,double num2){
//         courseCode=name;
//         examMark=num1;
//         courseWorkMark=num2;
//         noOfCourse++;
//     }
//     public double finalMark(){
//         double result=examMark+courseWorkMark;
//         return result;
//     }
//     public static int getNoOfCourse(){
//         return noOfCourse;
//     }
//     public String toString(){
//         return courseCode+" "+examMark+" "+courseWorkMark;
//     }

// }
// class CourseLab extends Course{
//     double labMark;
//     public CourseLab(String name,double num1,double num2,double num3){
//         super(name,num1,num2);
//         labMark=num3;
//     }
//     @Override
//     public double finalMark(){
//         double result=super.finalMark()+labMark;
//         return result;
//     }
//     public String toString(){
//         return super.toString()+" "+labMark;

//     }
//     public static void main(String[] args){
//         Course obj=new Course("02011ABC", 100, 100);
//         Course obj1=new CourseLab("0201AACJC", 98, 99,100);
//         System.out.println(obj);
//         System.out.println(obj1);
//         System.out.println("Number of course ="+getNoOfCourse());
//     }
// }

// import java.text.Format;
// import java.text.SimpleDateFormat;
// import java.util.Date;
// import java.util.Calendar;

// class GetDayNameExample1 {
//     public static void main(String args[]) throws Exception {
//         // returns a Calendar object whose calendar fields have been initialized with
//         // the current date and time
//         Calendar cal = Calendar.getInstance();
//         // creating a constructor of the SimpleDateFormat class
//         SimpleDateFormat sdf = new SimpleDateFormat("dd-MM-yyyy");
//         // getting current date
//         System.out.println("Today's date: " + sdf.format(cal.getTime()));
//         // creating a constructor of the Format class
//         // displaying full-day name
//         Format f = new SimpleDateFormat("EEEE");
//         String str = f.format(new Date());
//         // prints day name
//         System.out.println("Day Name: " + str);
//     }
// }

// import java.time.LocalDate;
// import java.text.SimpleDateFormat;
// import java.util.Date;
// import java.util.*;

// class GetDayNameExample4 {
//     public static void main(String args[]) {
//         Scanner sc=new Scanner(System.in);
//         try {
//             SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy", java.util.Locale.ENGLISH);
//             System.out.print("Enter today date: ");
//             String myDate=sc.nextLine();
//             Date date = sdf.parse(myDate);
//             // specifies the pattern to print
//             sdf.applyPattern("EEE, d MMM yyyy");
//             String str = sdf.format(date);
//             // prints day name with date
//             System.out.println(str);
//             sc.close();
//         } catch (Exception e) {
//             e.printStackTrace();
//         }
//     }
// }

// class University{
//     public String status="O";// O stands for open.
//     int arr[]=new int[19];
//     public University(){
//         status="C";
//     }
// }
// class Electrical{
//     public Electrical(){

//     }
// }
// class Operators{
//     public static void main(String[] args){
//         int a=5,b=10,c=11;
//         // System.out.println(a<10^b==10);
//         // System.out.println(a++);
//         // System.out.println(++a);
//         // System.out.println(divisible(b,a));
//         if (divisible(b,a)| divisible(c,a)){
//             System.out.println("COndition satisfied.");
//         }

//     }
// }

// cla

// class Array {
//     void printArray(int[] array) {
//         for (int i = 0; i < array.length; i++) {
//             System.out.print(array[i] + " ");
//         }
//         System.out.println();
//     }

//     void printArray(String[] array) {
//         for (int i = 0; i < array.length; i++) {
//             System.out.print(array[i] + " ");
//         }
//         System.out.println();
//     }

//     void printArray(float[] array) {
//         for (int i = 0; i < array.length; i++) {
//             System.out.print(array[i] + " ");
//         }
//         System.out.println();
//     }

//     int[] rArrayA(int[] array) {
//         int[] newArr = new int[array.length];
//         for (int i = 0; i < array.length; i++) {
//             newArr[array.length - 1 - i] = array[i];
//         }
//         return newArr;
//     }

//     float[] rArrayB(float[] array) {
//         float[] newArr = new float[array.length];
//         for (int i = 0; i < array.length; i++) {
//             newArr[array.length - 1 - i] = array[i];
//         }
//         return newArr;
//     }

//     String[] rArrayC(String[] array) {
//         String[] newArr = new String[array.length];
//         for (int i = 0; i < array.length; i++) {
//             newArr[array.length - 1 - i] = array[i];
//         }
//         return newArr;
//     }

//     public static void main(String[] args) {
//         Array obj = new Array();
//         int arr1[] = { 1, 2, 3, 4, 5 };
//         float arr2[] = { 1.2f, 3.4f, 5.6f, 7.8f };
//         String arr3[] = { "hello", "world", "this", "is" };

//         obj.printArray(arr1);
//         obj.printArray(arr2);
//         obj.printArray(arr3);
//         System.out.println();
//         int res1[] = obj.rArrayA(arr1);
//         float res2[] = obj.rArrayB(arr2);
//         String res3[] = obj.rArrayC(arr3);
//         System.out.println("After Reversing:");
//         obj.printArray(res1);
//         obj.printArray(res2);
//         obj.printArray(res3);

//     }

// }

// class NumberProperties {
//     private int number;

//     public NumberProperties(int n) {
//         number = n;
//     }

//     public boolean isPrime() {
//         for (int i = 2; i < number; i++) {
//             if (number % i == 0) {
//                 return false;
//             }
//         }
//         return true;
//     }

//     public boolean relativePrime(int anotherNumber) {
//         ArrayList<Integer> arr1 = new ArrayList<Integer>();
//         for (int i = 2; i < number; i++) {
//             if (number % i == 0) {
//                 arr1.add(i);
//             }
//         }
//         for (int i = 0; i < arr1.size(); i++) {
//             if (anotherNumber % arr1.get(i) == 0) {
//                 return false;
//             }
//         }
//         return true;

//     }

//     public int getNumber() {
//         return number;
//     }

//     public void setNumber(int n) {
//         number = n;
//     }

//     public static void main(String[] args) {
//         NumberProperties obj = new NumberProperties(4);
//         boolean res = obj.isPrime();
//         System.out.println("Is Prime : "+res);
//         boolean res1 = obj.relativePrime(9);
//         System.out.println("Relative Prime : "+res1);
//         System.out.println("Number before calling method : " + obj.getNumber());
//         obj.setNumber(50);
//         System.out.println("Number after calling method : " + obj.getNumber());

//     }

// }

class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        next = null;
    }
}

class LinkedList {
    Node head;

    public LinkedList() {
        head = null;
    }

    void addLast(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }

    void display() {
        if (head == null) {
            System.out.println("LinkedList is empty.");
        } else {
            Node temp = head;
            while (temp != null) {
                System.out.printf(temp.data + "-->");
                temp = temp.next;
            }
            System.out.println("null");

        }
    }

    void myFun(Node head, Node temp) {
        
        Node firstNode = temp;
        Node secondNode = temp;
        if (temp.next == null || temp.next.next == null) {
            System.out.println("Method is returning.");
            return;
        }
        while (secondNode.next.next != null) {
            secondNode = secondNode.next;
        }
        temp=temp.next;
      
        

        Node firstNext=secondNode.next;
       
        firstNode.next=firstNext;
       
        firstNode.next.next=temp;
        secondNode.next=null;
        myFun(head, temp);


    }

}

public class Main {
    public static void main(String[] args) {
        LinkedList obj = new LinkedList();
        obj.addLast(1);
        // obj.addLast(2);
        // obj.addLast(3);
        // obj.addLast(4);
        // obj.addLast(5);
        // obj.addLast(50);
        obj.display();
        obj.myFun(obj.head, obj.head);
        obj.display();
    }
}
