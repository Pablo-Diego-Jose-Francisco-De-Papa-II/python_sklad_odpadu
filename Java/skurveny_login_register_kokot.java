public class simple_projects {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        HashMap<String, String> user_data = new HashMap<String, String>();



        while(true) {
            System.out.print("login or register? ");
            String start = input.next();



            switch (start.toLowerCase()) {
                case "login":
                    System.out.print("Enter your username: ");                      //input name
                    String log_mail = input.next();


                    if (user_data.containsKey(log_mail)) {      //user found
                        System.out.print("Enter your password: ");                  //input pass
                        String log_pass = input.next();

                        String pass = user_data.get(log_mail);

                        if (pass.equals(log_pass)) {
                            System.out.println("You successfully loged in!");
                            return;

                        } else {
                            System.out.println("Incorrect password! :(");
                        }

                    } else {                                    //user not found
                        System.out.println("Username not found...");                //error
                    }
                    break;



                case "register":
                    System.out.print("Enter a new username: ");                     //input name
                    String reg_mail = input.next();

                    if (user_data.containsKey(reg_mail)) {
                        System.out.println("Username already exists...");
                        break;
                    }

                    System.out.print("Enter a password: ");                         //input pass
                    String reg_password = input.next();


                    user_data.put(reg_mail, reg_password);
                    break;



                default:
                    System.out.println("dement");                                   //error
                
            }
        }
    }
}
