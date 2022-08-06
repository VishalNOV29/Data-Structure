// import java.util.*;

// public class Tree {
//     static Scanner sc = null;

//     public static void main(String[] args) {
//         sc = new Scanner(System.in);
//         Tree obj=new Tree();
//         Node root=obj.createTree();
//         System.out .println("root : "+root.data);
//         System.out.println("root.left : "+root.left.data);
//         System.out.println("root.right : "+root.right.data);

//     }

//     Node createTree() {
//         Node root = null;

//         System.out.println("Enter data: ");
//         int data = sc.nextInt();
//         if (data == -1) {
//             return null;
//         }
//         root = new Node(data);
//         System.out.println("Enter left for "+data);
//         root.left=createTree();
//         System.out.println("Enter right for root "+data);
//         root.right=createTree();
//         System.out.println("Both part called."+root.data);
//         return root;
//     }
// }

// class Node {
//     int data;
//     Node left, right;

//     Node(int key) {
//         data = key;
//     }
// }
