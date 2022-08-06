
// // import java.security.cert.CertStoreException;
// import java.security.cert.CertPath;
// import java.util.Scanner;

// public class BinarySearchTree {
//     static Scanner sc = new Scanner(System.in);

//     class Node {
//         int data;
//         Node left, right;

//         public Node(int val) {
//             data = val;
//             this.left = null;
//             this.right = null;
//         }
//     }

//     Node root;

//     public BinarySearchTree() {
//         root = null;
//     }

//     public Node createTree() {
//         System.out.print("Enter data: ");
//         int val = sc.nextInt();
//         if (val == -1) {
//             return null;
//         }
//         root = new Node(val);
//         System.out.println("Enter data for left: ");
//         root.left = createTree();
//         System.out.println("Enter data for right: ");
//         root.right = createTree();
//         return root;
//     }
//     public static void main(String[] args){
//         BinarySearchTree obj=new BinarySearchTree();
//         Node res=obj.createTree();
//         System.out.println("root is "+res.data);
//     }

// }
