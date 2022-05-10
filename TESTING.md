# TESTING

## HTML VERIFIER

Using w3c HTML verifier I checked all live pages deployed on heroku. There were several warnings and some errors involving stray div's and li elements. These have been removed by making use of the authenticator.
The major warning given was that the javascript at the bottom of the page doesnt require text="text/javascript". These aren't serious warnings however have been removed.

## HOMEPAGE

![HOMEHTML](readme/images/homepagehtml.jpg)

## ALLPRODUCTS

![ALLPRODUCTS](readme/images/allproductshtml.jpg)

## FULLPRODUCT

![FULLPRODUCT](readme/images/fullproducthtml.jpg)

## CATEGORY

![CATEGORY](readme/images/categoryhtml.jpg)

## BAG

![BAG](readme/images/baghtml.jpg)

## CHECKOUT

![CHECKOUT](readme/images/checkouthtml.jpg)

## CHECKOUT SUCCESS

![CHECKOUTSUCCESS](readme/images/checkoutsuccesshtml.jpg)

## CONTACT

![CONTACT](readme/images/checkoutsuccesshtml.jpg)

## PROFILE

![PROFILE](readme/images/profilehtml.jpg)

However it is worth noting when checking all HTML pages one by one as they are coded. It gives off a lot of warnings and errors. This is due to the templating language used from django.


## CSS 

The base.css file was run through the authenticator giving no errors but a couple of warnings involving use of webkit and using background colors and border colors which are them same. However after checking the elements these were on this
doesn't cause a major issue in my opinion.

![CSSCHECK](readme/images/csscheck.jpg)

## JavaScript

### STRIPE
![JSHINT](readme/images/jshintstripe.jpg)