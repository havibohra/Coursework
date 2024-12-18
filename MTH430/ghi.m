clear all;

%K = 3;
K = input(' ');
for m = 1:K
    N = 2^m; 
    h = 1/N;
    u = zeros (N+1,N+1); % for saving the numerical solution

    %%
    %% Complete the code to fill u
    %%

    % Exact solution    
    ex = zeros(N+1);
    for i = 2:N
        for j = 2:N
            for k = 1:15
                for l = 1:15
                    ex(i,j) = EX(i,j) + ...
                        sin((2*k-1)*pi*x(i))*sin((2*l-1)*pi*y(j))/...
                        ((2*k-1)*(2*l-1)*((2*k-1)^2+(2*l-1)^2));
                end
            end
        ex(i,j) = 16*ex(i,j)/pi^4;
        end
    end
    
    e(m) = max(max(abs(u-ex)))/max(max(abs(ex)));
end

for m = 1:K
    fprintf('%.2g ', e(m));    
end
fprintf('\n');

for m = 2:K
    fprintf('%.2g ', e(m-1)/e(m));    
end
fprintf('\n');