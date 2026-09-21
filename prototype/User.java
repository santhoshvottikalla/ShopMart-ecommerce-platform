
public class User {
    private String username;
    private String password;
    private final String role = "user";
    
    public User(String username, String password)
     {
        this.username = username;
        this.password = password;
    }
    
    // Getters and setters
    public String getUsername() 
    { return username;
     }
    public String getPassword() 
    { 
        return password; 
    }
    public String getRole() 
    {
         return role;
    }
    
    public void setUsername(String username)
     {
         this.username = username;
     }
    public void setPassword(String password)
     {
         this.password = password;
     }
    
    // User Services 
    
    public void viewProducts()
     {
        System.out.println("\nAvailable Products:");
        for(Product p : DB.getProducts()){
            System.out.println(p);
        }
    }
    
    
    public void addToCart(Cart cart, int productId, int quantity) {
        Product p = DB.findProductById(productId);
        if(p != null) {
            cart.addProduct(p, quantity);
        } 
        else {
            System.out.println("Product not found.");
        }
    }
    public void checkout(Cart cart) {
        double total = cart.getTotal();
        if(total == 0) {
            System.out.println("Your cart is empty.");
            return;
        }
        System.out.println("Your total is: $" + total);
        Payment payment = new Payment(total);
        if(payment.processPayment()){
            Transaction t = new Transaction(DB.getNextTransactionId(), this.username, total);
            DB.addTransaction(t);
            cart.clearCart();
            System.out.println("Order placed successfully.");
        }
         else {
            System.out.println("Payment failed.");
        }

    }
    
    @Override
    public String toString()
    {
        return "User: " + username;
    }
}
