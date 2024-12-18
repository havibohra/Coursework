clc;
clear;
n=input('enter n: ');
a=input('enter matrix: ');
l=diag(ones(n,1));
u=zeros(n);
fprintf("Given matrix A:\n");
disp(a);
flag=1;

for i=1:n
    u(i,i)=a(i,i);
    for k=1:i-1
        u(i,i)= u(i,i)-l(i,k)*u(k,i);
    end
    if u(i,i)==0
        flag=0;
        break;
    end

    for j=i+1:n
        u(i,j)= a(i,j);
        l(j,i)= a(j,i);
        for k=1:i-1
            u(i,j)= u(i,j)-l(i,k)*u(k,j);
            l(j,i)= l(j,i)-l(j,k)*u(k,i);
        end
        l(j,i)=l(j,i)/u(i,i);
    end
end
if flag
    fprintf("Dolittle's LU decomposition of the givem matrix is:\n");
    fprintf("L:\n");
    disp(l);
    fprintf("U:\n");
    disp(u);
else
    fprintf("Factorization impossible!\n");
end