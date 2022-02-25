## Relationship between PEarson correlation coefficient and p-val/n samples

## The p-value for Pearson correlation in the cor.test/stat_cor packages are computed based on a t-statistic using r and n:
## tstat= (r*sqrt(n-2))/sqrt((1-r^2))
## Want to know how different r and n's effect the significance. 

## If you have large n, the correlation coefficient becomes less important for determining p-value
## Put another way, you will have a low p-value (<0.01) if your distribution has r~0.5 and N>30 samples or so


## Compute t-stat/p-value based on: 
#a) different n
#b) different r

df<-data.frame(r=NULL,n=NULL,p=NULL)
for(r in seq(0,1,by=0.01)){
  for(n in c(3,10,20,30,40,50)){
    (tstat<-(r*sqrt(n-2))/sqrt((1-r^2)))
    (pval<-2*pt(tstat,df = n-2, lower.tail = F))
    df<-rbind(df,data.frame(r=r,n=n,p=pval))
  }
}
head(df)

ggplot(df,aes(x=r,y=p,col=as.factor(n)))+
  geom_point()+
  geom_hline(yintercept = c(0.01),lty=2,col='red')+
  theme_bw()+
  theme(legend.position = "bottom")+
  ylab("p-value")+
  xlab("Pearson correlation stat")+
  ggtitle("Relationship between p-value as a function of Pearson cor and number of samples")

## Conclusion: be careful with Pearson-based p-values as it doesn't take much to be <0.01 (either large n and/or mid-range Pearson correlation)


# and example of cor_stat in practice
x <- c(44.4, 45.9, 41.9, 53.3, 44.7, 44.1, 50.7, 45.2, 60.1)
y <- c( 2.6,  3.1,  2.5,  5.0,  3.6,  4.0,  5.2,  2.8,  3.8)
df2<-data.frame(x=x,y=y)
ggplot(df2,aes(x=x,y=y))+
  geom_point() +
  stat_cor(output.type = "text",alternative="two.sided",method="pearson")

# stat_cor uses cor.test to compute R and p-value, so as a check:
cor.test(x, y, method = "pearson", alternative = "two.sided")

(n<-length(x))

# R=0,57, as confirmed here:
(r<-cor(x,y))

# t-stat is 1.84, as confirmed here:
(tstat<-(r*sqrt(n-2))/sqrt((1-r^2)))

# and finally, p-value is 0.11 as confirmed here:
(pval<-2*pt(tstat,df = n-2, lower.tail = F))



