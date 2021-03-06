from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from numpy import empty
from pymysql import NULL
from .models import CartTwo, Products, Humuus, Lalruud, Details, CartTest, CartTestTwo

# Create your views here.

def index(request):
    #    sags ruu baraa hiihed ajillaj baigaa function
    howMany = 0
    cartSync = CartTwo.objects.all()
    if request.method == "POST":
        pro_id = request.POST["pro_id"]
        count = request.POST["count"]
        # print(f"HERE THE BITCH IS:  {pro_id} ")

        
        chosenProInfo = Products.objects.get(id=pro_id)
        print(f"LOOK AT THIS availableAmount  : {chosenProInfo.detail}")
        
        cart = CartTwo()
        cart.availableAmount = chosenProInfo.availableAmount
        cart.number = pro_id
        cart.detail = chosenProInfo.detail
        cart.img = chosenProInfo.img
        cart.name = chosenProInfo.name
        cart.price = chosenProInfo.price
        cart.displayPrice = chosenProInfo.displayPrice
        cart.count = count
        
        print(f"WWWWWWWWWWWWWWWWWW price: {cart.price}")

        check_cart = CartTwo.objects.all()
        already_in_cart = NULL


        if check_cart:
            for oneItem in check_cart:
                if int(oneItem.number) == int(pro_id):
                    already_in_cart = True 
        else:
            cart.save()


        if already_in_cart == NULL:
            cart.save()
            
            
            
            #   niit dung bodoog total variable dotor hiigeed yovuulj bna
        # cartSync = CartTwo.objects.all()
        total = 0
    
        if cartSync:
            for neg in cartSync:
                howMany = howMany + 1
                total = total + int(neg.price) * int(neg.count)
                
            #   baraag songood sagsand nemeh deer darhad ajilna
            return render(request, "cart/index.html", {
                "pro_id": pro_id,
                "cart": cartSync,
                "total": total,
                "howMany": howMany
            })
        else:
            return render(request, "cart/emptyCart.html")






    #    hamgiin ehend huudas achaallahad ajilna
    products = Products.objects.all()
    cartPros = CartTwo.objects.all()
    for x in cartSync:
        howMany = howMany + 1
        
    return render(request, "home/index.html", {
        "products": products,
        "humuus": Humuus.objects.all(),
        "howMany": howMany,
        "cartPros": cartPros
    })
    
    
    
    
    
    # uzeh deer darhad ajillaj baigaa function
def pro(request, pro_id):
    product = Products.objects.get(id=pro_id)
    return render(request, "home/product.html", {
        "pro": product,
        "pro_id": pro_id
    })


