food=read.csv("food.csv")
food
tomato=data.frame(ingredient="tomato",sweetness=6,crunchiness==4)
tomato
food1=food[,2:3]
food1
tomato1=tomato[,2:3]
tomato1
library(class)
pred=knn(food1,tomato1,food$FoodType,k=1)
pred

