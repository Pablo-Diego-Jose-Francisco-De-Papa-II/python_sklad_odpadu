public class Davitov_vadny_login_register_pindik {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        String regexPattern = "\\w+([.-]?\\w+)*@\\w+([.-]?\\w+)*(\\.\\w{2,3})+";
        Pattern pattern = Pattern.compile(regexPattern);
        HashMap<String, String> user_data = new HashMap<String, String>();



        while(true) {
            System.out.print("login or register? ");
            String start = input.next();



            switch (start.toLowerCase()) {
                case "login":
                    System.out.print("Enter your email: ");                      //input name
                    String log_mail = input.next();


                    if (user_data.containsKey(log_mail)) {      //user found
                        System.out.print("Enter your password: ");                  //input pass
                        String log_pass = input.next();

                        String pass = user_data.get(log_mail);

                        if (pass.equals(log_pass)) {
                            System.out.println("You successfully logged in!");
                            return;

                        } else {
                            System.out.println("Incorrect password! :(");
                        }

                    } else {                                    //user not found
                        System.out.println("User with this email was not found...");//error
                    }
                    break;



                case "register":
                    System.out.print("Enter a new email address: ");                     //input name
                    String reg_mail = input.next();
                    Matcher matcher = pattern.matcher(reg_mail);


                    if (!matcher.matches()) {
                        System.out.println("Invalid email address.");
                        break;
                    }

                    if (user_data.containsKey(reg_mail)) {
                        System.out.println("Email already in use...");
                        break;
                    }

                    System.out.print("Enter a password: ");                         //input pass
                    String reg_password = input.next();


                    user_data.put(reg_mail, reg_password);
                    break;



                default:
                    System.out.println("DUMBASS");                                   //error

            }
        }
    }
}
