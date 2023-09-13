import java.util.Scanner;
import java.util.ArrayList;

public class Davitov_vadny_login_register_pindik {
    
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        ArrayList<String> names = new ArrayList<String>();

        System.out.println("-> type \"show\" to see registered students\n-> type \"end\" to end program");

        while(true) {
            System.out.print("Register a new student or you will be punished: ");
            String inputed_material = input.next();


            switch (inputed_material) {
                case "show":
                    for (String name : names) {
                        System.out.print(name + " ");
                    }
                    System.out.print("\n");
                    break;

                case "end":
                    System.out.print("List of students: ");
                    for (String name : names) {
                        System.out.println(name + " ");
                    }
                    return;

                default:
                    if (names.contains(inputed_material)) {
                        System.out.println("Student already in our database");
                    } else {
                        names.add(inputed_material);
                    }
            }
        }
    }
}
