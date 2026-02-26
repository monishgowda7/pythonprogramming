products_list={
    
    "laptop"   :150000,
    "mobile"   :120000,
    "earphone" :12500,
    "keyboard" :1999,
    "headphone":20000
    
}
print("--------PRODUCTS MENU------------")
for product,price in products_list.items():
    print(product     ,':',   price)    
print("---------------------------------")
print("Enter the option")
print("1.I WANT TO BUY PRODUCTS")
print("2.exit")
print("---------------------------------")
a=int(input("Enter the option:"))   


def billing_cart():
    cart={}
    m=input("Enter a product to buy:").lower()
    if m in products_list:
        n=int(input(f"enter the quantity of {m}:"))   
        if n>0:
            if m in cart:
                cart[m]=+n
            
            else:
                cart[m]=n 
        else:
            print("invalid quantity")  
                     
        print("Our cart:",cart)
        print("---------------------------------")
        print("            BILLING              ")
        print("---------------------------------")
        print("Product Name :",m)
        print("Quantity     :",n)
        
        price=products_list[m]*n
        
        if price>100000:
            dis1=price-(price/10)
            e=price/10
            print("Cart billing :",price)
            print("10% Discount :-",e)
            print("SUBTOTAL     :",dis1)
            Q=dis1*0.18
            print("GST 18%      :+",Q)
            print("FINAL BILLING:",dis1+Q)
            
            
            
        elif price>50000:
            dis2=price-(price/20)
            u=price/20
            print("Cart billing :",price)
            print("5% Discount  :-",u)
            print("SUBTOTAL     :",dis2)
            p=dis2*0.18
            print("GST 18%      :+",p)
            print("FINAL BILLING:",dis2+p)
              
            
        else:
            print("Cart billing :",price)  
            i=price*0.18
            print("GST 18%      :+",i)
            print("FINAL BILLING:",price+i)  
        print("---------------------------------")    
        print("Thank you,Visit again")    
        print("---------------------------------")  
           
    else:
        print("product is not available in our shop")     
          
    
match(a):
    case 1:
        billing_cart()
        
    case 2:
        print("Sucessfully exited")    
        
    case _:
        print("invalid option")    