import java.util.Scanner;

public class InsertionCwh {
    static void myMethod(int arr[], int ind, int ele, int siz) {
        for (int i = siz; i >= ind; i--) {
            arr[i] = arr[i - 1];
        }
        arr[ind - 1] = ele;
        for (int i = 0; i < siz + 1; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int myArr[] = new int[20];
        System.out.println("Enter elements less than 20 separated by space.");
        String input = sc.nextLine();
        String numbers[] = input.split(" ");
        for (int i = 0; i < numbers.length; i++) {
            myArr[i] = Integer.parseInt(numbers[i]);
        }
        System.out.println("Enter the element you want to insert: ");
        int ele = sc.nextInt();
        System.out.println("Enter the position at which you want to insert element: ");
        int ind = sc.nextInt();
        int siz = numbers.length;
        System.out.println("Now I am going to implement myMethod.");
        myMethod(myArr, ind, ele, siz);
        sc.close();

    }
}