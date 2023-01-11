# Urlshortner
Primary Goal: To achieve a Webapplication whose work is to short a given long url and also make custom short url from the given url so that they can be easily managed by user.

Solution: We have taken refernece of bitly.com who also done the same work like converting the long url into the short one and also providing the service like making custom short url.

At first we have made the UI whose main aim to take the long url from the user.

![Screenshot (30)](https://user-images.githubusercontent.com/87935713/211783062-1b0e12b0-885b-4613-ab4b-5883911eeeff.png)

This is the UI which takes url from the user.

Then after getting the url from the user, we pass that url from html to python.

In Python we use flask framework which mainly used for building microservice webapplication.

With the help of flask we get that url in our backend. After getting the url we use python logic to get a string of random 6 characters which are mainly used for converting the url with the help of rarndom module in python.

After making of this string we save this string into our database for future so that we not allot same string for more than one user.

When the saving of string to database completed then we send this shorten url to the UI for the user. 

When user click on this link then in flask automatically dynamicUrl function will run whose working is to redirect this short url to the long url given by the user.
So mainly this function is connecting our short url with long url.


![Screenshot (31)](https://user-images.githubusercontent.com/87935713/211783164-e3200840-50b8-4e15-8dc0-7c182797f735.png)

In this web applicaction login and sign up facility can also be used by user.
When a user login to our site then after login he or she can access the table of all the url which were shorted by him.

![Screenshot (32)](https://user-images.githubusercontent.com/87935713/211783181-3737f9b9-fca8-4064-bc24-e3e3d9376286.png)

User can also edit the urls and delete the urls according to its need.

So at the end we have completed an end to end webapllication whose main aim is to convert a long url to short url.
