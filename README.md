# Yoyo Python API Test

The test is to build a Django project that provides a set of REST webservices
for a loyalty programme.

## Requirements

The project represents a shop that sells two products: a widget and a gizmo.

- For each widget bought, one loyalty stamp is earnt 
- No stamps are earnt for gizmo purchases
- Multiple products can be bought a single transaction
- If you earn ten loyalty stamps, you automatically earn a voucher for a free widget
- When you earn a voucher for a free widget, your widget loyalty stamps balance resets
- You can only use a voucher once

## The Test

Create a set of REST APIs that:

- allow a transaction to take place 
- show how many stamps a customer has
- show how many vouchers a customer has
- add stamps to a customer
- add vouchers to a customer
- mark a voucher as redeemed

## What We Expect

It is expected that you:

- create your own data models
- either stub data or create and connect to a real database (it's free on Heroku!)
- write unit tests
- commit often
- deploy on Heroku 
- provide api documentation in the project

## Afterwards

When complete, send us the urls of the Heroku application and git repository.

## Getting Started

We have provided an empty django project. Feel free to either use this or create
your own. If you are going to use this then __please do the following__:

- clone (but do not fork) this repository 
- remove the (justyoyo) git origin
- create your own repository in either GitHub or BitBucket and set that as the new origin

## Get Creative

Add some useful additional feature. Show us something we haven't seen!

Have fun!
