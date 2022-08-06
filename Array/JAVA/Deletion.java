import java.util.Scanner;

public class Deletion {
    static int myMethod(int arr[], int ele, int capacity) {
        System.out.println("Implementing myMethod.....");
        int ind = 0;
        for (int i = 0; i < capacity; i++) {
            if (arr[i] == ele) {
                ind = i;
            }
        }
        return ind;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int myArr[] = new int[20];
        System.out.println("Enter elements separated by space: ");
        String input = sc.nextLine();
        String numbers[] = input.split(" ");
        for (int i = 0; i < numbers.length; i++) {
            myArr[i] = Integer.parseInt(numbers[i]);
        }
        System.out.println("Enter the element you want to delete: ");
        int ele = sc.nextInt();
        int capacity = numbers.length;
        int ind = myMethod(myArr, ele, capacity);
        for (int i = ind; i < capacity; i++) {
            myArr[i] = myArr[i + 1];
        }
        capacity -= 1;
        for (int i = 0; i < capacity; i++) {
            System.out.print(myArr[i] + " ");
        }
        sc.close();
    }
}
