library(rmutil)

# dN/dt = r * N * (1 - ( N / K) ) * exp(TA/Tref - TA/T)
# *********************************************************************
# PARAMETRI
# *********************************************************************

Tref<- 293.15 # Referentna temp 
TA<- 8000 # Arrhenius temp 
N0<- 1  # Inicialna konc. 
r<- 0.1 # Brzina rasta (log CFU/mL/h)  
K<- 4 # Carrying capacity (log CFU/mL)  

# *********************************************************************
# IZRAČUN
# *********************************************************************
#pdf(file="Vibrio_N_solutions.pdf", pointsize = 15)

T=288.15 # dnevna temperatura
dNdt<-function(N, t) (r * N * (1 - ( N / K) ) * exp(TA/Tref - TA/T))
N <- runge.kutta(dNdt, N0, seq(1,24,by=1/128))
xl<-length(N)

plot(seq(1,24,by=1/128), N, type="l", ylim = c(0,4), 
     axes=F, xlab="t / h", ylab="N", lty=1, col=1)
axis(1, at=c(-10,6,12,18,24), pos=0, outer=T)
axis(2, at=c(-10,0, 1,2,3,4), pos=0, outer=T)

br=2
for(temp in c(293.15, 298.15, 303.15, 308.15, 313.15)){
     T<-temp
     dNdt<-function(N, t) (r * N * (1 - ( N / K) ) * exp(TA/Tref - TA/T))
     N <- runge.kutta(dNdt, N0, seq(1,24,by=1/128))
     xl<-length(N)
     lines(seq(1,24,by=1/128), N, type="l", lty=br, col=br)
     br=br+1
}

legend(18,3, legend=c("15°C","20°C","25°C","30°C","35°C","40°C"),
       lty=1:6, bty="n", col=1:6, cex=0.85)
#dev.off()
