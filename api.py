# Requirements:

# Users should be able to track their expense with other users.
# Users should be able to create groups and start tracking expenses.
# Multiple people can pay up in an expense. Also, amount can be split up unequally in an expense. Consider this example:
# Users involved A,B,C
# Expense amount: 2000
# A B C
# Paid amount: 1500 500 0
# Owed amount: 500 500 1000
# Here A paid 1500 and B paid 500. But A and B consumed worth 500 where as C consumed worth 1000.
# Users should be able to able to settle up their balances with minimum number of transactions using the settle up feature.


# thoughts
1. new user sign up
2 userlogin
3 create group
4 add users to group 
5. add expense to group
6. get all expenses of group
7. add expense to user 
8 expense will cotain amount, paid by, owed by , group id, description
# check again for creating expense, 

initial steps to start with:
1. create a users db table and have some mock data 
2 a api to create a group
question: should we create a group first and then add users to it or add users first and then create a group?
what is the easiest way to do this?
3. create a group and add users to it using aother api 
4. create an expense and add it to the group using aother api
5. get all expenses of the group using aother api

what about db? mysql or mongo db