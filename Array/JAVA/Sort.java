import java.util.Scanner;
import java.util.Arrays;
public class Sort {
    public static void main(String[] args){
        Scanner obj=new Scanner(System.in);
        String input=obj.nextLine();
        String[] numbers=input.split(" ");
        int[] myArr=new int[numbers.length];
        for (int i=0;i<myArr.length;i++){
            myArr[i]=Integer.parseInt(numbers[i]);
        }
        Arrays.sort(myArr);
        for(int ele:myArr){
            System.out.println(ele);
        }
        obj.close();
    }
}

