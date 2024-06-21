matris_correlacao <- function(dados.ok){
  
  # Pacotes nescessários
  library(ggplot2)
  library(ggcorrplot)
  
  
  # Determinando a matrix de correlacao e truncando os valores             
  cor.data <- round(cor(na.omit(dados.ok)),1)
  
  
  # Plotando e salvando os dados
  suppressWarnings({ #Apenas para não emitir os avisos
    
    ggcorrplot(cor.data, #Definindo os dados 
               hc.order = TRUE, #Organiza os dados usando agrupamento 
               type = "lower", #Mostra apenas a diagonal inferior da matriz
               legend.title = "Coeficiente de \n Correlação", #Título da legenda
               lab = TRUE, #Adiciona o coeficiente de correlação no gráfico
               lab_size = 3,#Definindo o tamanho dos rótulos 
               method="circle", #Definindo o tipo de pontos 
               colors = c("#FF2000", "white", "#00B3D4"), #Definindo as cores 
               title="Correlação entre Variáveis", #Definindo o título principal
               ggtheme=theme_bw) #Definindo o tema
  })
  
}