clear all;
close all;

tol = 1.e-8;
M = input(' ');

alpha = 1/(exp(1)+exp(-1));

for m = 1:M
    N = 2^m;
    h = 2/(N+1);
    t = [-1+h:h:1-h].';
    
    % Starting u for the Newton interations
    u = ones(N,1)/(exp(1)+exp(-1));
    
    % A = zeros(N,N);
    % for i=1:N
    %   A(i,i) = -2;
    %   if(i > 1)    A(i,i-1) = 1;
    %   if(i < N)    A(i,i+1) = 1;
    % end
    A = diag(-2*ones(N,1)) + diag(ones(N-1,1),1) + diag(ones(N-1,1),-1);
     
    g = zeros(N,1);
    g(1) = -alpha/h^2;
    g(N) = -alpha/h^2;
    
    converged = false;
    while (converged == false)
        
        F = calF(u,alpha,N,h);
        Fp = calFp(u,alpha,N,h);
        
        mat1 = (1/h^2)*A - Fp;
        mat2 = (1/h^2)*A*u - F - g;
        
        res = mat1\mat2;
        u = u - res;
        
        % check for convergence
        % if (norm(A*u-calF(u,alpha,N,h)-g,inf)<tol)
        %     converged = true;
        % end
        
        converged = (norm(res, inf) < tol);
    end
    % The error
    E(m) = max(abs(u-1./(exp(t)+exp(-t))));
end
fprintf('\n');
fprintf('E(m): ');
for m = 1:M
    fprintf('%.2g ', E(m));
end
fprintf('\n');
fprintf('E(m)/E(m+1): ');
for m = 1:M-1
    fprintf('%.2f ', E(m)/E(m+1));
end
fprintf('\n');

----------------------------------------------------
function [f] = calf(u,up)
   f =  -u + 2*up^2/u;
end

function [F] = calF(u,alpha,N,h)
    F = zeros(N,1);
    for i = 1:N
        if i == 1
            F(i) = calf(u(i), (u(i+1)-alpha)/(2*h));
        elseif i == N
            F(i) = calf(u(i), (alpha-u(i-1))/(2*h));
        else
            F(i) = calf(u(i), (u(i+1) - u(i-1))/(2*h));
        end
    end
end

function [Fp] = calFp(u,alpha,N,h)
    Fp = zeros(N,N);
    for i = 1:N
        if i == 1
            temp = (u(2) - alpha) / (2*h*u(1));
        elseif i == N
            temp = (alpha - u(N-1)) / (2*h*u(N));
        else
            temp = (u(i+1) - u(i-1)) / (2*h*u(i));
        end
        Fp(i,i) = -1 - 2*temp^2;
        if i > 1
            Fp(i,i-1) = -(1/(2*h)) * 4 * temp;
        end
        if i < N
            Fp(i,i+1) = (1/(2*h)) * 4 * temp;
        end
    end
end