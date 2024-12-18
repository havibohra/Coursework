clc;
clear;
%% input
n= input('enter n: ');
a=input('enter matrix: ');
b= input('enter rhs vector: ');
%% SOR
% x=input('enter initial guess: ');
% t= input('enter no. of iterations: ');
% w=input('enter relaxation parameter: ');
% 
% r=zeros(n,t+1);
% r(:,1)=x;
% for k=1:t
%     for i=1:n
%         z=b(i);
%         for j=1:n
%             if(j<i)
%                 z=z-a(i,j)*x(j,k+1);
%             elseif(j>i)
%                 z=z-a(i,j)*x(j,k);
%             end
%         end
%         z= w*z/a(i,i);
%         z= z+(1-w)*x(i,k);
%         x(i,k+1)=z;
%     end
% end
% disp(cell2mat(compose('%10.6f',x)));
%% LU-DECOMPOSN (doliitle,crout)
% l= diag(ones(n,1));
% u= zeros(n);
% flag=1;
% 
% for i=1:n
%     u(i,i)= a(i,i);
%     for k=1:i-1
%         u(i,i)= u(i,i)- l(i,k)*u(k,i);
%     end
%     if(u(i,i)==0)
%         flag=0;
%         break;
%     end
% 
%     for j=i+1:n
%         u(i,j)=a(i,j);
%         l(j,i)=a(j,i);
%         for k=1:i-1
%             u(i,j)= u(i,j)- l(i,k)*u(k,j);
%             l(j,i)= l(j,i)- l(j,k)*u(k,i);
%         end
%         u(i,j)= u(i,j)/l(i,i);
%         l(j,i)= l(j,i)/u(i,i);
%     end
% end
% 
% if(flag==0)
%     fprintf("Factorization Impossible!\n");
% else
%     fprintf("L:\n");
%     disp(l);
%     fprintf("U:\n");
%     disp(u);
% end
%% Cholesky Decomposn
% l=zeros(n);
% flag=1;
% for i=1:n
%     l(i,i)=a(i,i);
%     for k= 1:i-1
%         l(i,i)= l(i,i)-l(i,k)^2;
%     end
%     if(l(i,i)==0)
%         flag=0;
%         break;
%     end
% 
%     l(i,i)=sqrt(l(i,i));
% 
%     for j=i+1:n
%         l(j,i) = a(i,j);
%         for k=1:i-1
%             l(j,i) = l(j,i) - l(j,k)*l(i,k);
%         end
%         l(j,i)= l(j,i)/l(i,i);
%     end
% end
% 
% if(flag==0)
%     fprintf("Cholesky Decompostion Impossible!");
% else
%     fprintf("A=LL^T, where L=\n");
%     disp(l);
% end
%%
disp(a);
disp(b);
disp([a transpose(b)]);