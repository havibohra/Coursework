clc;
clear;
f=@(x) x-cos(x);

df =@(x) 1+sin(x);
 fprintf("\n The given equation is: x - cos(x)=0. \n");
 x0=input('enter x0: ');
 % x1=input('enter x1"');
 if f(x0)==0
    fprintf('\n a root is: %f',x0);
 elseif df(x0)==0
     fprintf('NEWTON RAPHSON NOT VALID');
 else
     n=input('\n max iter: ');
     esp=input('\n enter eps: ');
     disp(cell2mat(compose('%10.6f',[0  x0  f(x0)])));
     it=1;
     while it<=n
         
         x= x0 - f(x0)/df(x0);
        disp(cell2mat(compose('%f',[it  x  f(x)])));
        if f(x)==0
            fprintf('\n a root is %10.6f', x);
            break;
        elseif(abs(x-x0)<=eps || abs(f(x)-f(x0)) <=eps)
            fprintf('approx root with tol %f is %f',eps,x);
            break;
        end
         x0=x;
         it=it+1;
     end
     if it==n+1
         fprintf('max iter reached');
     end
 end
