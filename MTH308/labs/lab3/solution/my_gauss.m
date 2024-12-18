clc;
clear;
n=input("enter n: ");
a= input('enter the matrix: ');
b= input('enter rhs vector: ');

A=[a,b];
rank=0;
fprintf("Augmented matrix corresponding to the system is given by:\n");
disp(A);
x=zeros(n,1);

%step1
for j=1:n
    p=rank+1;
    %step2(pivot-finding)
    while(p<=n && A(p,j)==0)
        p=p+1;
    end
    
    if p~=n+1
        rank= rank+1;
        %step3(swapping)
        if p~=rank
            row= A(p,:);
            A(p,:)=A(rank,:);
            A(rank,:)=row;
        end

        %step4-5-6(elimn)
        for k=rank+1:n
            if A(k,j)~=0
                m=A(k,j)/A(rank,j);
                A(k,:)= A(k,:)- m*A(rank,:);
            end
        end
    end
end

%step7
if rank<n
    flag=1;
    for k=rank+1:n
        if A(k,n+1)~=0
            flag=0;
            break;
        end
    end
    if flag 
        fprintf("No unique solution (infinite no.of solutions) exists\n");
    else
        fprintf("No solution exists\n");
    end
else
    %step8
    x(n)= A(n,n+1)/A(n,n);
    
    %step9
    for i= n-1:-1:1
       x(i)= A(i,n+1);
       for j=i+1:n
           x(i)= x(i)- A(i,j)*x(j);
       end
       x(i)=x(i)/A(i,i);
    end
    fprintf("Solution of the system is given by:\n");
    disp(x);
end