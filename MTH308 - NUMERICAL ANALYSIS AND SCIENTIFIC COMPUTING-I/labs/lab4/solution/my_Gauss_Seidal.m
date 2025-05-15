clc;
clear;
n= input('enter n: ');
a= input('enter matrix: ');
b= input('enter rhs vector: ');
x= input('enter intial guess: ');
t= input('enter no. of iterations: ');
x_2= zeros(n,t+1);
x_2(:,1)=x;

for k=1:t
    for i=1:n
        x_2(i,k+1)= b(i);
        for j=1:n
            if(j>i)
                x_2(i,k+1)= x_2(i,k+1)-a(i,j)*x(j);
            elseif(j<i)
                x_2(i,k+1)= x_2(i,k+1)-a(i,j)*x_2(j,k+1);
            end
        end
        x_2(i,k+1)=x_2(i,k+1)/a(i,i);
    end
    x=x_2(:,k+1);
end
fprintf("\n");
disp(cell2mat(compose('%10.6f',x_2)));
