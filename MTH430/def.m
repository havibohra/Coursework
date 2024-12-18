% clear all;
% close all;

% tol = 1.e-8;

% %M = 10;
% M = input(' ');
% for m = 1:M
%     N = 2^m;
%     h = 2/(N+1);
%     t = [-1+h:h:1-h].';
    
%     % Starting u for the Newton interations
      u = ones(N,1)/(exp(1)+exp(-1));

      A= zeros(N,N);
      for i=1:N
          A(i,i)=-2;
          if i>1 
              A(i,i-1)=1;
          end
          if i<N
              A(i,i+1)=1;
          end
      end
      alpha = 1/ (exp(1)+exp(-1));
      g= zeros(N,1);
      g(1)= -alpha/h^2;
      g(N)= -alpha/h^2;


%     converged = false;
%     while (converged == false)
            
%         %%
%         %% Complete the code for Newton updates for u
%         %%
          F= calcF(u,alpha,N,h);
          Fprime= calcFprime(u,alpha,N,h);

          mat1 = (1/h^2)*A - Fprime;
          mat2 = (1/h^2)*A*u - F - g;
          u = u - mat1\mat2;
%         % check for convergence
%         if (norm(A*u-f(t,u,up)+g,inf)<tol)
%             converged = true;
%         end
%     end
%     % The error
%     E(m) = max(abs(u-1./(exp(t)+exp(-t))));
% end
% fprintf('\n');
% fprintf('E(m): ');
% for m = 1:M
%     fprintf('%.2g ', E(m));
% end
% fprintf('\n');
% fprintf('E(m)/E(m+1): ');
% for m = 1:M-1
%     fprintf('%.2f ', E(m)/E(m+1));
% end
% fprintf('\n');
% -------------------------------------------------------------------
function[f] = fcal(u,uprime)
    f= -u + 2*(uprime^2)/u;
end
function[F] = calcF(u,alpha,N,h)
    F= zeros(N,1);
    for i=1:N
        if i==1
            F(i) = fcal(u(i),(u(i+1)-alpha)/(2*h));
        elseif i==N
            F(i) = fcal(u(i),(alpha-u(i-1))/(2*h));
        else
            F(i) = fcal(u(i),(u(i+1)-u(i-1))/(2*h));
        end
    end
end
function[Fprime] = calcFprime(u,alpha,N,h)
    Fprime = zeros(N,N);
    for i=1:N
         if i==1
            up_by_u = (u(i+1)-alpha)/(2*h*u(i));
        elseif i==N
            up_by_u = (alpha-u(i-1))/(2*h*u(i));
        else
            up_by_u = (u(i+1)-u(i-1))/(2*h*u(i));
         end

         Fprime(i,i) = -1 -2*up_by_u^2;
         if i>1
             Fprime(i,i-1) = (-1/(2*h))*4*up_by_u;
         end
         if i<N
             Fprime(i,i+1) = (1/(2*h))*4*up_by_u;
         end
    end
end
