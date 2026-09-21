import java.io.Console;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        DB.initialize();
        Scanner scanner = new Scanner(System.in);
        Console console = System.console();

        while (true) {
            System.out.println("\n--- Welcome to E-Commerce ---");
            System.out.println("Select your role:");
            System.out.println("1. Admin");
            System.out.println("2. User");
            System.out.print("Enter your choice: ");
            int roleChoice = scanner.nextInt();
            scanner.nextLine();

            if (roleChoice == 1) {
                System.out.println("\n--- Admin Login ---");
                System.out.print("Username: ");
                String uname = scanner.nextLine();
                String pass = readPassword(console, scanner, "Password: ");

                boolean adminFound = false;
                for (Admin a : DB.getAdmins()) {
                    if (a.getUsername().equals(uname) && a.getPassword().equals(pass)) {
                        adminFound = true;
                        adminMenu(scanner, a, console);
                        break;
                    }
                }
                if (!adminFound) {
                    System.out.println("Invalid admin credentials.");
                }

            } else if (roleChoice == 2) {
                System.out.println("\n1. Login");
                System.out.println("2. Sign Up");
                System.out.print("Enter your choice: ");
                int userChoice = scanner.nextInt();
                scanner.nextLine();

                if (userChoice == 1) {
                    System.out.print("Username: ");
                    String uname = scanner.nextLine();
                    String pass = readPassword(console, scanner, "Password: ");
                    User u = DB.findUserByUsername(uname);
                    if (u != null && u.getPassword().equals(pass)) {
                        userMenu(scanner, u);
                    } else {
                        System.out.println("Invalid user credentials.");
                    }
                } else if (userChoice == 2) {
                    System.out.print("Choose a username: ");
                    String newUname = scanner.nextLine();
                    if (DB.findUserByUsername(newUname) != null) {
                        System.out.println("Username already exists. Please try logging in.");
                    } else {
                        String newPass = readPassword(console, scanner, "Choose a password: ");
                        User newUser = new User(newUname, newPass);
                        DB.addUser(newUser);
                        System.out.println("Registration successful. Please login.");
                    }
                } else {
                    System.out.println("Invalid choice.");
                }
            } else {
                System.out.println("Invalid role selection.");
            }
        }
    }

    
    public static String readPassword(Console console, Scanner scanner, String prompt) {
        if (console != null) {
            char[] passChars = console.readPassword(prompt);
            return new String(passChars);
        } else {
            System.out.print(prompt);
            return scanner.nextLine(); 
        }
    }

    // --- Admin Menu ---
    public static void adminMenu(Scanner scanner, Admin admin, Console console) {
        while (true) {
            System.out.println("\n--- Admin Dashboard ---");
            System.out.println("1. Manage Products");
            System.out.println("2. Manage Categories");
            System.out.println("3. Manage Users");
            System.out.println("4. Change Admin Credentials");
            System.out.println("5. View Transactions");
            System.out.println("6. Logout");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    manageProducts(scanner, admin);
                    break;
                case 2:
                    manageCategories(scanner, admin);
                    break;
                case 3:
                    manageUsers(scanner, admin, console);
                    break;
                case 4:
                    changeAdminCredentials(scanner, admin, console);
                    break;
                case 5:
                    DB.viewTransactions();
                    break;
                case 6:
                    System.out.println("Logging out...");
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }

    public static void manageProducts(Scanner scanner, Admin admin) {
        while (true) {
            System.out.println("\n--- Manage Products ---");
            System.out.println("1. View Products");
            System.out.println("2. Add Product");
            System.out.println("3. Update Product Stock");
            System.out.println("4. Delete Product");
            System.out.println("5. Back");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine();
            switch (choice) {
                case 1:
                    admin.viewProducts();
                    break;
                case 2:
                    System.out.print("Enter product name: ");
                    String pname = scanner.nextLine();
                    System.out.print("Enter price: ");
                    double price = scanner.nextDouble();
                    System.out.print("Enter stock: ");
                    int stock = scanner.nextInt();
                    System.out.print("Enter category ID: ");
                    int catId = scanner.nextInt();
                    scanner.nextLine();
                    admin.addProduct(pname, price, stock, catId);
                    break;
                case 3:
                    System.out.print("Enter product ID to update: ");
                    int pid = scanner.nextInt();
                    System.out.print("Enter new stock: ");
                    int newStock = scanner.nextInt();
                    scanner.nextLine();
                    admin.updateProductStock(pid, newStock);
                    break;
                case 4:
                    System.out.print("Enter product ID to delete: ");
                    int delPid = scanner.nextInt();
                    scanner.nextLine();
                    admin.deleteProduct(delPid);
                    break;
                case 5:
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }

    public static void manageCategories(Scanner scanner, Admin admin) {
        while (true) {
            System.out.println("\n--- Manage Categories ---");
            System.out.println("1. View Categories");
            System.out.println("2. Add Category");
            System.out.println("3. Update Category");
            System.out.println("4. Delete Category");
            System.out.println("5. Back");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine();
            switch (choice) {
                case 1:
                    admin.viewCategories();
                    break;
                case 2:
                    System.out.print("Enter category name: ");
                    String cname = scanner.nextLine();
                    System.out.print("Enter description: ");
                    String desc = scanner.nextLine();
                    admin.addCategory(cname, desc);
                    break;
                case 3:
                    System.out.print("Enter category ID to update: ");
                    int cid = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Enter new name: ");
                    String newName = scanner.nextLine();
                    System.out.print("Enter new description: ");
                    String newDesc = scanner.nextLine();
                    admin.updateCategory(cid, newName, newDesc);
                    break;
                case 4:
                    System.out.print("Enter category ID to delete: ");
                    int delCid = scanner.nextInt();
                    scanner.nextLine();
                    admin.deleteCategory(delCid);
                    break;
                case 5:
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }

    public static void manageUsers(Scanner scanner, Admin admin, Console console) {
        while (true) {
            System.out.println("\n--- Manage Users ---");
            System.out.println("1. View Users");
            System.out.println("2. Delete User");
            System.out.println("3. Reset User Password");
            System.out.println("4. Update User Credentials");
            System.out.println("5. Back");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine();
            switch (choice) {
                case 1:
                    admin.viewUsers();
                    break;
                case 2:
                    System.out.print("Enter username to delete: ");
                    String delUser = scanner.nextLine();
                    admin.deleteUser(delUser);
                    break;
                case 3:
                    System.out.print("Enter username to reset password: ");
                    String uname = scanner.nextLine();
                    String newPass = readPassword(console, scanner, "Enter new password: ");
                    admin.resetUserPassword(uname, newPass);
                    break;
                case 4:
                    System.out.print("Enter current username: ");
                    String oldUname = scanner.nextLine();
                    System.out.print("Enter new username: ");
                    String newUname = scanner.nextLine();
                    String newUserPass = readPassword(console, scanner, "Enter new password: ");
                    admin.updateUserCredentials(oldUname, newUname, newUserPass);
                    break;
                case 5:
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }

    public static void changeAdminCredentials(Scanner scanner, Admin admin, Console console) {
        System.out.print("Enter new admin username: ");
        String newAdminUname = scanner.nextLine();
        String newAdminPass = readPassword(console, scanner, "Enter new admin password: ");
        admin.setUsername(newAdminUname);
        admin.setPassword(newAdminPass);
        System.out.println("Admin credentials updated.");
    }

    // --- User Menu ---
    public static void userMenu(Scanner scanner, User user) {
        Cart cart = new Cart();
        while (true) {
            System.out.println("\n--- User Dashboard (" + user.getUsername() + ") ---");
            System.out.println("1. View Products");
            System.out.println("2. Add Product to Cart");
            System.out.println("3. View Cart");
            System.out.println("4. Checkout");
            System.out.println("5. Logout");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine();
            switch (choice) {
                case 1:
                    user.viewProducts();
                    break;
                case 2:
                    System.out.print("Enter product ID: ");
                    int pid = scanner.nextInt();
                    System.out.print("Enter quantity: ");
                    int qty = scanner.nextInt();
                    scanner.nextLine();
                    user.addToCart(cart, pid, qty);
                    break;
                case 3:
                    cart.viewCart();
                    break;
                case 4:
                    user.checkout(cart);
                    break;
                case 5:
                    System.out.println("Logging out...");
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }
}

