# *********************************************************************
# Prikaz dinamike vibria s promjenjivim K za temperature 13 - 30 5°C
# *********************************************************************
rm(list=ls())
graphics.off()
library(rmutil)
library(readr)

# *********************************************************************
# DATA INPUT
# *********************************************************************
# temp_45 <- read_csv("temperature_dummy_rcp45.csv")
# temp_85 <- read_csv("temperature_dummy_rcp85.csv")
# temp_45<-temp_45$temp
# temp_85<-temp_85$temp
temperature <- read_csv("data/timeseries_past_future/farm_638_past_future.csv")
N_365_221<-N365_45<-N365_85<-numeric(365)
brh<-24
N_365_221<-temperature$temp_2021
N_45<-temperature$temp_2030_rcp45
N_85<-temperature$temp_2030_rcp85

# dN/dt = r * N * (1 - ( N / K) ) * exp(TA/Tref - TA/T)
# *********************************************************************
# PARAMETRI PROMJENE BRZINE RASTA
# *********************************************************************
Tref<-293.15 # Referentna temp 
TA<-8000 # Arrhenius temp 
# N0<-1  # Inicialna konc. 
r<-0.1 # Brzina rasta (log CFU/mL/h)  
K<-4 # Carrying capacity (log CFU/mL)  

# varijabilni K
b_f<-40 # slope
c_f<-1 # minimum
d_f<-4 # maksimum
e_f<-18 # temperatura infleksije

Calc1<-function(T, N0){
  Kr<-(1-((c_f+(d_f-c_f)/(1+exp(b_f*(log10(T-273.15)-log10(e_f)))))))+4
  if(Kr<1) Kr<-1
  dNdt<-function(N, t) (r * N * (1 - ( N / Kr) ) * exp(TA/Tref - TA/T))
  N <- runge.kutta(dNdt, N0, seq(1,brh,by=1/128))
  xl<-length(N)
  dayN<-N[xl] 
  nod<-length(N[N>=2])
  return(dayN)
}

Calc0<-function(T){
  Kr<-(1-((c_f+(d_f-c_f)/(1+exp(b_f*(log10(T-273.15)-log10(e_f)))))))+4
  if(Kr<1) Kr<-1
  dNdt<-function(N, t) (r * N * (1 - ( N / Kr) ) * exp(TA/Tref - TA/T))
  N <- runge.kutta(dNdt, 1, seq(1,brh,by=1/128))
  xl<-length(N)
  dayN<-N[xl] 
  nod<-length(N[N>=2])
  return(dayN)
}




# *********************************************************************
# IZRAČUN
# *********************************************************************
# Scenarij 4.5.
N365_45[1]<-Calc0(temp_45[1]+273.15)

for(dan in 2:365){
N0<-N365_45[dan-1]
T=temp_45[dan]+273.15 # dnevna temperatura u K
dayN<-Calc1(T, N0)
N365_45[dan]<-N365_45[dan-1]+(dayN-N0)
}


# Scenarij 8.5.
N365_85[1]<-Calc0(temp_85[1]+273.15)

for(dan in 2:365){
  N0<-N365_85[dan-1]
  T=temp_85[dan]+273.15 # dnevna temperatura u K
  dayN<-Calc1(T, N0)
  N365_85[dan]<-N365_85[dan-1]+(dayN-N0)
}
plot(1:365, N365_45, type="l", col="darkred", ylab="log(N)", xlab = "Days")
lines(1:365, N365_85, col="red")
length(N365_45[N365_45>=2])
length(N365_85[N365_85>=2])


