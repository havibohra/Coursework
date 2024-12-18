% function [y,yEX,yEM] = AM2(y0,h,N)

%     y = zeros(1,N+1);       % exact solution
%     yEX = zeros(1,N+1);     % solution with exact start
%     yEM = zeros(1,N+1);     % solution started with Euler's method

%     % initial condition
%     y(1) = y0;
%     yEX(1) = y0;
%     yEM(1) = y0;

%     % choice for y_1
%     y(2) = %% complete the statement
%     yEX(2) = %% complete the statement
%     yEM(2) = %% complete the statement

%     for n = 2:N                             % time marching
%         t = n*h;                            % current time
    
%         %% complete the code to fill the arrays
%         %% y, yEX and yEM
        
%     end

% end

% T = 1.0;
% y0 = input(' ');
% M = input(' ');

% errorEX = zeros(1:M);
% errorEM = zeros(1:M);
% for m = 2:M
%     N = 2^m;
%     h = T/N;
%     [y,yEX,yEM] = AM2(y0,h,N);
%     errorEX(m) = max(abs(y-yEX));
%     errorEM(m) = max(abs(y-yEM));
% end
% fprintf('\n');
% for m = 3:M
%     fprintf('%6d \t %0.6e \t %0.2f \t %0.6e \t %0.2f\n', ...
%     2^m, errorEX(m), errorEX(m-1)/errorEX(m), ...
%     errorEM(m), errorEM(m-1)/errorEM(m));
% end

function [y,yEX,yEM] = AM2(y0,h,N)

    y = zeros(1,N+1);       % exact solution
    yEX = zeros(1,N+1);     % solution with exact start
    yEM = zeros(1,N+1);     % solution started with Euler's method

%     % initial condition
    y(1) = y0;
    yEX(1) = y0;
    yEM(1) = y0;

% %     % Exact solution for y1
% %     % y(2) = (y0 - 1) * exp(-100*h) + h*(100*h + 101); 
    y(2) = (h + 1) + (y0 - 1) * exp(-100 * h);
% %     % Euler's method for y1
    yEX(2) = (y0 - 1) * exp(-100*h) + h+1; % Exact solution for yEX(2)
    yEM(2) = y0 + h*(-100*y0 + 100*0 + 101);           % Euler's method for yEM(2)

%     for n = 2:N                             % time marching
%         t = n*h;                            % current time
        
%         % Adams-Moulton method for the exact start yEX
%         f_n = -100*yEX(n) + 100*(t-h) + 101;
%         f_n_minus_1 = -100*yEX(n-1) + 100*(t-2*h) + 101;
%         yEX(n+1) = yEX(n) + h/2 * (3*f_n - f_n_minus_1);
        
%         % Adams-Moulton method for the Euler start yEM
%         f_n = -100*yEM(n) + 100*(t-h) + 101;
%         f_n_minus_1 = -100*yEM(n-1) + 100*(t-2*h) + 101;
%         yEM(n+1) = yEM(n) + h/2 * (3*f_n - f_n_minus_1);
        
%         % Exact solution at time step t
%         % y(n+1) = (y0 - 1) * exp(-100*(n+1)*h) + ((n+1)*h)*(100*(n+1)*h + 101);
%         y(n+1) = (t + 1) + (y0 - 1) * exp(-100 * t);
%     end

% end

    m_curr = 5*h/12;
    m_prev = 8*h/12;
    m_prev_prev = -h/12;
    % initial condition
    % y(1) = y0;
    % yEX(1) = y0;
    % yEM(1) = y0;

    % % choice for y_1
    % y(2) = (y0 - 1)*exp(-100*h) + h + 1;
    % yEX(2) = (y0 - 1)*exp(-100*h) + h + 1;
    % yEM(2) = y0 + h*(-100*y0 + 101); 

    for n = 3:N+1                             % time marching
        t = (n-1)*h; % current time
        t_prev = t - h;
        t_prev_prev = t - 2*h;
        y(n) = (y0 - 1)*exp(-100*t) + t + 1;
        %% complete the code to fill the arrays
        yEX(n) = yEX(n-1) + m_curr*(100*t + 101) + m_prev*(100*t_prev + 101 - 100*yEX(n-1)) + m_prev_prev*(100*t_prev_prev + 101 - 100*yEX(n-2));
        
        yEX(n) = yEX(n)/(1 + 100*m_curr);
        
        
        yEM(n) = yEM(n-1) + m_curr*(100*t + 101) + m_prev*(100*t_prev + 101 - 100*yEM(n-1)) + m_prev_prev*(100*t_prev_prev + 101 - 100*yEM(n-2));
        
        yEM(n) = yEM(n)/(1 + 100*m_curr);

    end

end


T = 1.0;
y0 = input(' ');
M = input(' ');

errorEX = zeros(1,M);
errorEM = zeros(1,M);
for m = 2:M
    N = 2^m;
    h = T/N;
    [y,yEX,yEM] = AM2(y0,h,N);
    errorEX(m) = max(abs(y-yEX));
    errorEM(m) = max(abs(y-yEM));
end
fprintf('\n');
for m = 3:M
    fprintf('%6d \t %0.6e \t %0.2f \t %0.6e \t %0.2f\n', ...
    2^m, errorEX(m), errorEX(m-1)/errorEX(m), ...
    errorEM(m), errorEM(m-1)/errorEM(m));
end
