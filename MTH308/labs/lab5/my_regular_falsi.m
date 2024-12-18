clc;
clear;
f=@(x) sqrt(x)-cos(x);
fprintf("\n The given equation is: sqrt(x) - cos(x)=0. \n");

a=input('\n enter a:');
b=input('\n enter b: ');

if f(a)==0
    fprintf('\n root is %f',a);
elseif f(b)==0
    fprintf('\n root is %f',b);
elseif f(a)*f(b)>0
    fprintf('\n method not valid for these inputs');
else 
    n=input('\n enter n:');
    it=1;
    while it<=n
        x= (a*f(b)-b*f(a))/(f(b)-f(a));
        disp(cell2mat(compose('%14.9f',[it a b x f(x)])));

        if f(x)==0
            fprintf('a root is %10.6f',x);
        elseif f(x)*f(a)>0
            a=x;
        else
            b=x;
        end
        it=it+1;
    end
    if(it==n+1)
        fprintf('max iter reached');
    end
end


