# Smart API

**Awesome API Checker.**

# Requirements

* Python (2.7, 3.4, 3.5, 3.6)

# Example

Let's take a look at a quick example of using Smart API to build a simple for accessing API's.

Initiate a class 

    from smart_api import CSPApi
    
    my_instance = CSPApi(username="ce8b19f98c2d4868b9003eeee4dfd6d0",
                         password="694E66bC9fA342159B4BB444bB083aB4"
                         )

    my_appication_token = my_instance.application_token(url='https://endpoint.example.com/token/application')

    my_customer_token = my_instance.customer_token(url='https://endpoint.example.com/token/customer')
