from django.urls import path





from .views import index, signup, login, productdetail, products, cartoperations, buynow, checkout, logout, cart, account,termsandconditions,customerservice
from .views import wishlist, search, updateprofile, changepassword, postreview, contact, about, cancelproduct,tickets

urlpatterns = [
    path("", index.index, name="ShopHome"),
    path("signup/", signup.Signup.as_view(), name="SignUp"),
    path("login/", login.Login.as_view(), name="LogIn"),
    path("products/", products.products, name="Products"),
    path("search/", search.search, name="Search"),
    path("productdetail/<int:prid>", productdetail.productdetail, name="ProductDetail"),
    path("addtocart/<int:prid>", cartoperations.addtocart, name="AddtoCart"),
    path("buynow/<int:prid>", buynow.buynow, name="BuyNow"),
    path("postreview/<int:prid>", postreview.postreview, name="PostReview"),
    path("deletefromcart/<int:prid>", cartoperations.deletefromcart, name="DeletefromCart"),
    path("deleteallfromcart/<int:prid>", cartoperations.deleteallfromcart, name="DeleteAllfromCart"),
    path("addtowishlist/<int:prid>", wishlist.addtowishlist, name="AddfromWishlist"),
    path("removefromwishlist/<int:prid>", wishlist.removefromwishlist, name="RemovefromWishlist"),
    path("cart/", cart.cart, name="Cart"),
    path("clearcart/", cartoperations.clearcart, name="ClearCart"),
    path("checkout/", checkout.checkout, name="CheckOut"),
    path("cancelproduct/<int:orid>/<int:prid>", cancelproduct.cancelProduct, name="CancelProduct"),
    path("contactus/", contact.contact, name="ContactUs"),
    path("about/", about.about, name="AboutUs"),
    path("account/", account.account, name="Account"),
    path("account/updateprofile/", updateprofile.updateprofile, name="UpdateProfile"),
    path("account/changepassword/", changepassword.changepassword, name="ChangePassword"),
    path("logout/", logout.logout_view, name="Logout"),
    path("termsandconditions/",termsandconditions.termsandconditions, name="TermsAndConditions" ),
    path("customerservice/", customerservice.customer_service, name="CustomerService"),
    path("customerservice/account/changepassword/", changepassword.changepassword, name="Changepassword"),
    path("customerservice/account/updateprofile/", updateprofile.updateprofile, name="UpdateProfile"),
    path("ticket/", tickets.tickets, name="ticket"),
    
   
   


]

