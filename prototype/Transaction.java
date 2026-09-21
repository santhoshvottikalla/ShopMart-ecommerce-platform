// Transaction.java
public class Transaction {
    private int id;
    private String username;
    private double total;
    
    public Transaction(int id, String username, double total) {
        this.id = id;
        this.username = username;
        this.total = total;
    }
    
    @Override
    public String toString() {
        return "Transaction ID: " + id + " | User: " + username + " | Total: $" + total;
    }
}

