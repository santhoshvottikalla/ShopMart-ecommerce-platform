
import java.util.ArrayList;

public class Cart {
    private ArrayList<Product> products;
    private ArrayList<Integer> quantities;
    
    public Cart() {
        products = new ArrayList<>();
        quantities = new ArrayList<>();
    }
    
    public void addProduct(Product p, int qty) {
        if(p.getStock() < qty) {
            System.out.println("Not enough stock for " + p.getName());
            return;
        }
        int index = products.indexOf(p);
        if(index != -1) {
            int currentQty = quantities.get(index);
            quantities.set(index, currentQty + qty);
        } else {
            products.add(p);
            quantities.add(qty);
        }
        p.setStock(p.getStock() - qty);
        System.out.println("Added " + qty + " of " + p.getName() + " to cart.");
    }
    
    public void viewCart() {
        if(products.isEmpty()){
            System.out.println("Cart is empty.");
            return;
        }
        double total = 0;
        System.out.println("Cart contents:");
        for(int i = 0; i < products.size(); i++){
            Product p = products.get(i);
            int qty = quantities.get(i);
            double cost = qty * p.getPrice();
            total += cost;
            System.out.println(p.getName() + " x " + qty + " = $" + cost);
        }
        System.out.println("Total: $" + total);
    }
    
    public double getTotal() {
        double total = 0;
        for(int i = 0; i < products.size(); i++){
            total += quantities.get(i) * products.get(i).getPrice();
        }
        return total;
    }
    
    public void clearCart() {
        products.clear();
        quantities.clear();
    }
}
