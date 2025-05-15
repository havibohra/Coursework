clc;
clear;

f= @(x) x^2*log(x^2+1); 
fprintf('\n given function is f(x)=x^2*log(x^2+1):');
a=input('\n enter a: ');
b=input('\n enter b: ');
h=input('\n enter h: ');
n= (b-a)/(2*h);

T=f(a)+f(b);
for i=1:n-1
    T=T + 2*f(a+2*i*h) + 4*f(a+2*i*h +h);
end
T=T+4*f(a+h);
T=T*h/3;
fprintf('\n the value of integral is: %10.6f\n',T);
