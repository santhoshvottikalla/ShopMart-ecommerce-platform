
public class Admin {
    private String username;
    private String password;
    private final String role = "admin";
    
    public Admin(String username, String password) {
        this.username = username;
        this.password = password;
    }
    
    
    public String getUsername()
     { 
        return username;
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
    
    //  Admin Services 
    
        public void viewProducts() {
        System.out.println("\nProducts:");
        for(Product p : DB.getProducts()){
            System.out.println(p);
        }
    }
    
    public void addProduct(String name, double price, int stock, int categoryId) {
        Category cat = DB.findCategoryById(categoryId);
        if(cat == null) {
            System.out.println("Category not found.");
            return;
        }
        int newId = DB.getNextProductId();
        Product p = new Product(newId, name, price, stock, cat);
        DB.addProduct(p);
        System.out.println("Product added.");
    }
    
    public void updateProductStock(int productId, int newStock) {
        Product p = DB.findProductById(productId);
        if(p != null) {
            p.setStock(newStock);
            System.out.println("Stock updated.");
        } else {
            System.out.println("Product not found.");
        }
    }
    
    public void deleteProduct(int productId) {
        if(DB.removeProduct(productId)) {
            System.out.println("Product deleted.");
        } else {
            System.out.println("Product not found.");
        }
    }
    
    // Category management
    public void viewCategories() {
        System.out.println("\nCategories:");
        for(Category c : DB.getCategories()){
            System.out.println(c);
        }
    }
    
    public void addCategory(String name, String description) {
        int newId = DB.getNextCategoryId();
        Category cat = new Category(newId, name, description);
        DB.addCategory(cat);
        System.out.println("Category added.");
    }
    
    public void updateCategory(int categoryId, String newName, String newDesc) {
        Category cat = DB.findCategoryById(categoryId);
        if(cat != null) {
            cat.setName(newName);
            cat.setDescription(newDesc);
            System.out.println("Category updated.");
        } 
        else {
            System.out.println("Category not found.");
        }
    }
    
    public void deleteCategory(int categoryId) {
        if(DB.removeCategory(categoryId)) {
            System.out.println("Category deleted.");
        } 
        else {
            System.out.println("Category not found.");
        }
    }
    
    // User management
    public void viewUsers() {
        System.out.println("\nRegistered Users:");
        for(User u : DB.getUsers()){
            System.out.println(u);
        }
    }
    
    public void deleteUser(String username) {
        if(DB.removeUser(username)) {
            System.out.println("User deleted.");
        } 
        else {
            System.out.println("User not found or cannot delete admin.");
        }
    }
    
    public void resetUserPassword(String username, String newPassword) {
        User u =DB.findUserByUsername(username);
        if(u != null) {
            u.setPassword(newPassword);
            System.out.println("Password reset.");
        }
         else {
            System.out.println("User not found.");
        }
    }
    
    // Update both username and password for a user
    public void updateUserCredentials(String oldUsername, String newUsername, String newPassword) {
        User u =DB.findUserByUsername(oldUsername);
        if(u != null) {
            if(DB.findUserByUsername(newUsername) != null) {
                System.out.println("New username already exists.");
                return;
            }
            u.setUsername(newUsername);
            u.setPassword(newPassword);
            System.out.println("User credentials updated.");
        }
         else {
            System.out.println("User not found.");
        }
    }
    
    @Override
    public String toString(){
        return "Admin: " + username;
    }
}
