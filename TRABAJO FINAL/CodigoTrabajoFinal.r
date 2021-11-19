options(max.print=9999)
SIR.model <- function(t, b, g, n, c){
  require(deSolve) # Librería deSolve para resolver Sistemas de Ecuaciones Diferenciales
  init <- c(S=1-(10/n),I=10/n,R=0)
  parameters <- c(beta=b,gamma=g) #Parámetros
  time <- seq(0,t,by=1) #Se calculan los valores por cada día.
  eqn <- function(time,state,parameters){ #Ecuaciones del Sistema
    with(as.list(c(state,parameters)),{
      dS <- -beta*S*I #cambio en la proporción de los susceptibles(dS/dt)
      dI <- beta*S*I-gamma*I #cambio en la proporción de los infectados (dI/dt)
      dR <- gamma*I #cambio en la proporción de los recuperados (dR/dt)
      return(list(c(dS,dI,dR)))}) #lista con los resultados.
  }
  out<-ode(y=init,times=time,eqn,parms=parameters, method = "euler") #solución del sistema usando ode() de deSolve con el método euler.
  out.df<-as.data.frame(out) #crea un dataframe del output de la función anterior.
  
  print(out.df)
  
  require(ggplot2)
  theme_set(theme_minimal())
  title <- bquote("365 dias de Epidemia: Propagacion COVID-19 Santa Marta")
  subtit<-bquote(list("Marzo 20/2020-Marzo 20/2021", beta==.(parameters[1]),~gamma==.(parameters[2]), n==.(n), c==.(c))) #subtítulo con los parámetros usados.
  res<-ggplot(out.df,aes(x=time))+ #Plot con los resultados proporción vs días.
    ggtitle(bquote(atop(bold(.(title)),atop(bold(.(subtit))))))+ #poner título y subtítulo.
    geom_line(aes(y=S,colour="Susceptibles"))+ #línea del plot con los valores de S.
    geom_line(aes(y=I,colour="Infectados"))+ #línea del plot con los valores de I.
    geom_line(aes(y=R,colour="Recuperados"))+ #línea del plot con los valores de R.
    ylab(label="Cantidad")+ #label del eje Y
    xlab(label="Dias")+ #label del eje X
    
    scale_colour_manual("Líneas",
                        breaks=c("Susceptibles","Infectados","Recuperados"),
                        values=c("mediumblue","red","magenta1"))
  
  

  #Punto 2. Impresion del Plot generado anteriormente.Grafica de la epidemia.
  print(res)
  
  #Punto 3. Fecha con la mayor cantidad de recuperados.
  cat("\nLa cantidad maxima aproximada de infectados es: ", max(out.df$I), " (aproximadamente unas ", as.integer(max(out.df$I)*n)," personas) se espera entonces que esto suceda el dia: ", (which.max(out.df$I)-1), " (aproximadamente 11 de Noviembre del 2020)." )
  
  #Punto 4. Calculos de los porcentajes respectivos de poblacion estimada a infectarse y poblacion recuperada.
  cat("\n\nEl porcentaje estimado de población estimado que llegaria a infectarse: ", (max(out.df$I))*100, "% y el porcentaje estimado de personas recuperadas es: ", (max(out.df$R))*100, "%.")
  
  #Punto 5. Estimacion de la fecha en la que la epidemia estará controlada.
  indiceControl = g/(b*c)
  c <- which(out.df[['S']]<indiceControl)-1
  cat("\n\nA partir de la fecha", c[1] ,"de epidemia (la cual aproximadamente seria en Diciembre 6 del 2020) basado en estimacion, se dice entonces que la epidemia se encontrara controlada.")
}
SIR.model(365,0.06,0.021,45000,1.5)