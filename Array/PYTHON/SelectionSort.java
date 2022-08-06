import java.util.ArrayList;
import java.util.Arrays;

// import java.util.Arrays;

// class Selection {
// static int[]selectionSort(int arr[]){for(int i=0;i<arr.length-1;i++){int ele=arr[i];for(int j=i;j<arr.length;j++){if(arr[j]<ele){arr[i]=arr[j];arr[j]=ele;ele=arr[i];}}

// }return arr;}

//     public static void main(String[] args) {
//         int arr[] = { 5, 4, 3, 2, 1 };
//         System.out.println(Arrays.toString(arr));
//         int[] res = selectionSort(arr);

//         System.out.println(Arrays.toString(res));
//     }
// }

// import java.util.*;
// class Main {
//     static int[] orderList(int arr[]) {
//         for (int i = 0; i < arr.length - 1; i++) {
//             int ele = arr[i];
//             for (int j = i; j < arr.length; j++) {
//                 if (arr[j] < ele) {
//                     arr[i] = arr[j];
//                     arr[j] = ele;
//                     ele = arr[i];
//                 }
//             }

//         }
//         return arr;
//     }

//     static int lastIndex(int[] arr, int target) {
//         int lb = 0;
//         int ub = arr.length - 1;
//         int index = -1;
//         while (lb <= ub) {
//             int mid = (lb + ub) / 2;
//             if (arr[mid] == target) {
//                 index = mid;
//                 lb = mid + 1;
//             } else if (arr[mid] > target) {
//                 ub = mid - 1;
//             } else {
//                 lb = mid + 1;
//             }
//         }
//         return index;
//     }

//     public static void main(String[] args) {

//         Scanner sc = new Scanner(System.in);

//         System.out.print("Enter list size: ");
//         int ele = sc.nextInt();

//         System.out.println("Enter elements separated by space ");
//         sc.nextLine();

//         String numbers = sc.nextLine();
//         String str_arr[] = numbers.split(" ");

//         int arr[] = new int[ele];
//         for (int i = 0; i < ele; i++) {
//             arr[i] = Integer.parseInt(str_arr[i]);
//         }

//         System.out.print("Enter rarget value: ");
//         int target = sc.nextInt();
//         sc.close();

//         System.out.println("Entered Array : " + Arrays.toString(arr));
//         System.out.println("Sorted Array : " + Arrays.toString(orderList(arr)));

//         // Binary search is only applicable to sorted array.
//         System.out.println("Index of target : " + lastIndex(arr, target));

//     }
// }

// num=12
// print(1<<4)

// class Solution {
//     public int[] singleNumber(int[] arr) {
//         int result[]=new int[2];
//         int res=0;
//         for (int ele:arr){
//             res=res^ele;
//         }
//         int mask=1;
//         while (true){
//             if ((mask&res)!=0){
//                 break;
//             }
//             mask=mask<<1;
//         }
//         ArrayList<Integer> arr1=new ArrayList<Integer>();
//         for (int ele:arr){
//             if ((mask&ele)==0){
//                 arr1.add(ele);
//             }
//         }
//         int new_res=res;
//         for (int ele:arr1){
//             res=res^ele;
//         }
//         result[0]=res;
//         new_res=res^new_res;
//         result[1]=new_res;
//         return result;
//     }
// }
// number="1111"
// num=int(number,2)

// // print(int("1111",10))