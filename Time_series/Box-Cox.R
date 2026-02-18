
library(faraway)
?butterfat
data(butterfat)
fullmodel = lm(Butterfat ~ Breed * Age, data = butterfat)
plot(fullmodel)
library(MASS)
bc = boxcox(fullmodel , lambda = seq(-3,3))
best.lam = bc$x[which(bc$y==max(bc$y))]
fullmodel.inv= lm((Butterfat)^-1  ~ Breed * Age, data = butterfat)
plot(fullmodel.inv)
