
import java.util.ArrayList;

public class DB {
    
    private static ArrayList<User> users = new ArrayList<>();
    private static ArrayList<Admin> admins = new ArrayList<>();
    private static ArrayList<Product> products = new ArrayList<>();
    private static ArrayList<Category> categories = new ArrayList<>();
    private static ArrayList<Transaction> transactions = new ArrayList<>();
    

    private static int productIdCounter = 1;
    private static int categoryIdCounter = 1;
    private static int transactionIdCounter = 1;
    

    public static void initialize() {
        
        admins.add(new Admin("admin", "admin123"));
        
        
        Category electronics = new Category(getNextCategoryId(), "Electronics", "Devices and gadgets");
        Category fashion = new Category(getNextCategoryId(), "Fashion", "Clothing and accessories");
        categories.add(electronics);
        categories.add(fashion);
        
        
        products.add(new Product(getNextProductId(), "Laptop", 60000, 5, electronics));
        products.add(new Product(getNextProductId(), "Smartphone", 30000, 10, electronics));
        products.add(new Product(getNextProductId(), "T-Shirt", 500, 20, fashion));
        
       
    }
    
   
    public static ArrayList<User> getUsers() { return users; }
    public static ArrayList<Admin> getAdmins() { return admins; }
    public static ArrayList<Product> getProducts() { return products; }
    public static ArrayList<Category> getCategories() { return categories; }
    public static ArrayList<Transaction> getTransactions() { return transactions; }
    
   
    public static int getNextProductId() { return productIdCounter++; }
    public static int getNextCategoryId() { return categoryIdCounter++; }
    public static int getNextTransactionId() { return transactionIdCounter++; }
    
   
    public static void addUser(User u) { users.add(u); }
    
    public static User findUserByUsername(String username) {
        for(User u : users){
            if(u.getUsername().equalsIgnoreCase(username)){
                return u;
            }
        }
        return null;
    }
    
    public static boolean removeUser(String username) {
        User u = findUserByUsername(username);
        if(u != null){
            users.remove(u);
            return true;
        }
        return false;
    }
    
    public static void addProduct(Product p) { products.add(p); }
    
    public static Product findProductById(int id) {
        for(Product p : products){
            if(p.getId() == id){
                return p;
            }
        }
        return null;
    }
    
    public static boolean removeProduct(int id) {
        Product p = findProductById(id);
        if(p != null){
            products.remove(p);
            return true;
        }
        return false;
    }
    
    public static void addCategory(Category c) { categories.add(c); }
    
    public static Category findCategoryById(int id) {
        for(Category c : categories){
            if(c.getId() == id){
                return c;
            }
        }
        return null;
    }
    
    public static boolean removeCategory(int id) {
        Category c = findCategoryById(id);
        if(c != null){
            categories.remove(c);
            return true;
        }
        return false;
    }
    
    public static void addTransaction(Transaction t) { transactions.add(t); }
    
    public static void viewTransactions() {
        System.out.println("\nTransactions:");
        if(transactions.isEmpty()){
            System.out.println("No transactions yet.");
        } else {
            for(Transaction t : transactions){
                System.out.println(t);
            }
        }
    }
}
