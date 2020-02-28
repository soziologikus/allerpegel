library(anytime)

df_aller_pegel <- read.csv("aller_pegel.csv", header = TRUE, sep = ";")
datum <- anytime(as.factor(df_aller_pegel$datum))

jpeg("allerpegel_plot.jpg", height = 400, width = 800)
plot(datum, df_aller_pegel$allerpegel, type = "l", main = "Wasserstand der Aller beim Pegel Eitze", xlab = "Zeit", ylab = "Pegel der Aller (cm)", lwd=3, col="blue")
abline(h=c(460, 500, 560))
dev.off()

