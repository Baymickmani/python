import matplotlib.pyplot as plt
def linear(x,y,input_value):
    diff_x=[]
    diff_y=[]
    sum_x=0
    sum_y=0
    num=0
    deno=0
    for item in x:
        sum_x=sum_x+item
    for item in y:
        sum_y=sum_y+item
    mean_x=sum_x/len(x)
    mean_y=sum_y/len(y)
    for item in x:
        diff_x.append(item-mean_x)
    for item in y:
        diff_y.append(item-mean_y)
    for i in range(0,len(x)):
        num=num+ diff_x[i]*diff_y[i]
        deno=deno+ diff_x[i]**2
    alpha=num/deno
    beta=mean_y-(alpha*mean_x)
    print(alpha)
    print(beta)
    return(alpha*input_value+beta)
x=[72,50,81,74,94,86,59,83,65,33,88,81]
y=[84,63,71,78,90,75,49,79,77,52,74,90]
input_value=int(input("Enter the value for which it has to be predicted"))
print(linear(x,y,input_value))
plt.scatter(x,y)
plt.show()

        
