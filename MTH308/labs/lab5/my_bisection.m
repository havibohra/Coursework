clc;
clear;
f=@(x) sqrt(x)-cos(x);
fprintf("\n The given equation is: sqrt(x) - cos(x)=0. \n");
a=input('enter a:');
b=input('enter b:');
y0=f(a);
y1=f(b);
if f(a)==0
    fprintf('root is %f',a);
elseif f(b)==0
    fprintf('root is %f',b);
elseif y0*y1>0
    fprintf('bisection method not applicable with this inputs');
else 
    n= input('enter max iter: ');
    eps= input('enter eps: ');
    it=1;
    while it<=n
        x=(a+b)/2;
        disp(cell2mat(compose('%10.6f',[it a b x f(x)])));
        
        if f(x)==0
            fprintf('a root is %10.6f',x);
            break;
        elseif f(x)*f(a)>0
            a=x;
        elseif f(x)*f(b)>0
            b=x;
        end
        if(b-a <= eps)
            fprintf('approx root is %f,, with tolerance eps',(a+b)/2);
        end
        it=it+1;
    end
    if(it==n+1)
        fprintf('max iter reached');
    end
end

