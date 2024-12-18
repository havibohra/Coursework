clc;
clear;

f= @(x) x^3*exp(x);
fprintf('\n given function is f(x)=x^3*exp(x):');

a=input('\n enter a: ');
b=input('\n enter b: ');
h=input('\n enter h: ');
n= (b-a)/h;

T= (f(a)+f(b))/2;
for i=1:n-1
    T=T+f(a+i*h);
end
T=T*h;
fprintf('\n the value of integral is: %10.6f\n',T);
