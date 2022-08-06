import java.util.Scanner;

public class Insertion {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("How many elements you want in array.");
        int list_num = sc.nextInt();
        System.out.println("Enter elements separated with space.");
        sc.nextLine();
        String input = sc.nextLine();
        System.out.println(input);
        String[] numbers = input.split(" ");
        int[] myArray = new int[list_num];
        for (int i = 0; i < list_num; i++) {
            myArray[i] = Integer.parseInt(numbers[i]);
        }
        for (int ele : myArray) {
            System.out.println(ele);
        }
        System.out.print("Enter the position and element respectively to insert in array :");
        String index_element = sc.nextLine();
        String[] index_element_array = index_element.split(" ");
        int index = Integer.parseInt(index_element_array[0]);
        int element = Integer.parseInt(index_element_array[1]);
        int[] newArray = new int[list_num + 1];
        for (int i = 0; i <= list_num; i++) {
            if (i < index) {
                newArray[i] = myArray[i];
            }
            if (i == index) {
                newArray[i] = element;
            }

            if (i > index) {
                newArray[i] = myArray[i - 1];
            }
        }
        for (int ele : newArray) {
            System.out.println(ele);
        }
        sc.close();

    }
}