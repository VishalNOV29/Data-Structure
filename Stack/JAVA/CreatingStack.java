// class MyStack{
//     int a[];
//     int top;
//     int capacity;
//     public MyStack(int capacity){
//         this.capacity=capacity;
//         top=-1;
//         a=new int[capacity];
//     }
//     void push(int data){
//         if (top==capacity-1){
//             System.out.println("Stack is full.");
//         }
//         top++;
//         a[top]=data;
//     }
//     int pop(){
//         if (top==-1){
//             System.out.println("Stack is empty.");
//             return -1;
//         }
//         int res=a[top];
//         top--;
//         return res;
//     }
//     int peak(){
//         if (top==-1){
//             System.out.println("Stack is empty.");
//             return -1;
//         }
//         return a[top];
//     }
//     boolean isEmpty(){
//        return top==-1;
//     }
// }
// class Test{
//     public static void main(String[] args){
//         // MyStack obj=new MyStack(5);
//         // obj.push(20);
//         // System.out.println(obj.peak());
//         // obj.push(100);
//         // System.out.println(obj.peak());
//         // obj.push(30);
//         // // obj.pop();
//         // // obj.peak();
//         // System.out.println(obj.peak());

//     }
// }

// class Stack{
//     String stack[];
//     int capacity;
//     int top=-1;
//     Stack(int capacity){
//         this.capacity=capacity;
//         stack=new String[this.capacity];
//     }
//     void insert(String key){
//         top+=1;
//         stack[top]=key;
//     }
//     String pop(){
//         String res=stack[top];
//         stack[top]=null;
//         top-=1;
//         return res;
//     }
//     String top(){
//         if (top==-1){
//             return null;
//         }
//         return stack[top];
//     }
//     public static void main(String[] args){
//         Stack obj=new Stack(10);
//         obj.insert("X");
//         obj.insert("Y");
//         obj.insert("K");
//         // obj.insert(key);
//         System.out.println(obj.top());
//     }
// }