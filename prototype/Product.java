// Product.java
public class Product {
    private int id;
    private String name;
    private double price;
    private int stock;
    private Category category;
    
    public Product(int id, String name, double price, int stock, Category category) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.stock = stock;
        this.category = category;
    }
    
    public int getId()
     {
         return id;
     }
    public String getName()
     { 
        return name;
     }
    public double getPrice() 
    { 
        return price;
     }
    public int getStock()
     {
         return stock;
     }
    public Category getCategory() 
    { 
        return category;
     }
    
    public void setStock(int stock) 
    { 
        this.stock = stock;
     }
    
    @Override
    public String toString(){
        return id + ". " + name + " - $" + price + " (Stock: " + stock + ") | Category: " + category.getName();
    }
}
