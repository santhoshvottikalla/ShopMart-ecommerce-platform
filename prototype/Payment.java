
import java.util.Scanner;

public class Payment {
    private double amount;
    private String paymentMethod;
    
    public Payment(double amount) {
        this.amount = amount;
    }
    
    public boolean processPayment() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Total to pay: $" + amount);
        System.out.println("Select Payment Method:");
        System.out.println("1. UPI");
        System.out.println("2. Debit Card");
        System.out.println("3. Credit Card");
        System.out.println("4. Cash on Delivery");
        System.out.print("Enter choice: ");
        int choice = scanner.nextInt();
        scanner.nextLine();
        
        switch(choice) {
            case 1:
                System.out.print("Enter UPI ID: ");
                scanner.nextLine(); 
                paymentMethod = "UPI";
                break;
            case 2:
                System.out.print("Enter Debit Card Number: ");
                scanner.nextLine();
                paymentMethod = "Debit Card";
                break;
            case 3:
                System.out.print("Enter Credit Card Number: ");
                scanner.nextLine();
                paymentMethod = "Credit Card";
                break;
            case 4:
                paymentMethod = "Cash on Delivery";
                break;
            default:
                System.out.println("Invalid choice. Payment failed.");
                return false;
        }
        System.out.println("Payment successful using " + paymentMethod);
        return true;
    }
}
