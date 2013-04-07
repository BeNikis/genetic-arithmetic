#!/usr/bin/python

from random import randint,choice

add=lambda x:lambda y:x+y
sub=lambda x:lambda y:x-y
mul=lambda x:lambda y:x*y
div=lambda x:lambda y:x/y
mod=lambda x:lambda y:x%y

ops=[[add,'+'],[sub,'-'],[mul,'*']]

def gen_expression(length,left,right):
    expr=[]
    for i in range(length):
        op=choice(ops)
        expr.append([op[0](randint(left,right)),op[1]])
    return expr

def eval_expression (x,expr):
    for i in expr:
           #print i 
           x=i[0](x)
    #print "\n"
    return x

def expression_tostring(expr):
    #expr=map(lambda x:x,expr) #making a copy
    #expr.reverse()
    expr_str=len(expr)*'('+'x '
    for i in expr :
        if i[1]=='*':
            n=i[0](1)
        else:
            n=i[0](0)
        expr_str+=i[1]+' '+str(n)+') '
    
    return expr_str

def evald_expression_tostring(expr,x):
    exprstr=expression_tostring(expr).replace('x',str(x))
    return exprstr+ ' = ' + str(eval_expression(x,expr))

def genetic_arithmetic(get,start,length,left,right):
    batch=[]
    found = False
    my_key=lambda y:abs(eval_expression(start,y)-get)
    best_key=999999999999
    for i in range(30):
        batch.append(gen_expression(length,left,right))
        
    while not found:
        #print "Sorting the batch"
        batch=sorted(batch,key=my_key)
        batch=batch[:7]
        
        
                #combine                        
        for w in range(len(batch)):
            rind=choice(range(length))
            batch.append(batch[w][:rind]+choice(batch)[rind:])
                        
            #mutate
        for w in range(len(batch)):
            rind=choice(range(length))
            op=choice(ops)
            op=[op[0](randint(left,right)),op[1]]
            #brackets around op so we don't concatenate
            batch.append(batch[w][:rind]+[op]+batch[w][rind+1:])
       # print "checking for a match"
        if (best_key>my_key(batch[0])):
            best_key=my_key(batch[0])
            print("\n"+evald_expression_tostring(batch[0],start))
    
        found=(eval_expression(start,batch[0])==get)


if __name__ == "__main__" :
    import sys
    if ((len(sys.argv)!=6)) :
        print "Usage :genetic_arithmetic [to_get] [start] [expr_length] [left] [right]"
        print "to_get is the number that we're trying to evaluate to"
        print "start is the input for the expressions"
        print "expr_length is the length of our expression"
        print "left and right are bounds of the interval which are we getting our random numbers from"
        
    else:
        try:
            genetic_arithmetic(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
        except ValueError:
            print "not all parameters are integers"
        
    
        
    
