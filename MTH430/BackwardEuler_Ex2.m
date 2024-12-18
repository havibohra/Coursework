N = input(' ');
T = input(' ');
a1 = input(' ');
b1 = input(' ');
a2 = input(' ');
b2 = input(' ');
y10 = input(' ');
y20 = input(' ');
F = input(' ');
y = BackwardEuler_Ex2( N, T, a1, a2, b1, b2, y10, y20, F);
fprintf('y1(%.2f) = %.4f; y2(%.2f) = %.4f;', T, y(1,N+1), T, y(2,N+1));

function [ y ] = BackwardEuler_Ex2(N, T, a1, a2, b1, b2, y10, y20, F)

%The input N specifies the grid size, the input T specifies the final time,
%the inputs, a1, a2, b1, b2 correspond to ODE parameters \alpha_1, \alpha_2,
%\beta_1, \beta_2 respectively and the inputs y10, y20 specify the initial
%conditions y_1(0), $y_2(0) respectively. The input F specifies the number
%of fixed point iterations for solving the non-linear system at each step
%of the backward Euler method.

    % Time step size
    h = T / N;
    
    y = zeros(2,N+1);           % for storing the numerical solution

% Set initial conditions
    y(1, 1) = y10;  % Initial prey population
    y(2, 1) = y20;  % Initial predator population

    % Euler's method to get initial guess for y at first step
    for n = 1:N
        % Current values
        y1_curr = y(1, n);
        y2_curr = y(2, n);

        % Euler method update (forward step)
        y1_next = y1_curr + h * y1_curr * (a1 - b1 * y2_curr);
        y2_next = y2_curr + h * y2_curr * (-a2 + b2 * y1_curr);

        y(:, n+1) = [y1_next; y2_next];
    end

    % Backward Euler method with fixed-point iterations
    for n = 1:N
        % Current values
        y1_curr = y(1, n);
        y2_curr = y(2, n);

        % Start with Euler's method guess for fixed-point iteration
        y1_guess = y(1, n+1);
        y2_guess = y(2, n+1);

        % Fixed-point iteration
        for k = 1:F
            y1_new = y1_curr + h * y1_guess * (a1 - b1 * y2_guess);
            y2_new = y2_curr + h * y2_guess * (-a2 + b2 * y1_guess);

            y1_guess = y1_new;
            y2_guess = y2_new;
        end

        % Store the result after fixed-point iteration
        y(1, n+1) = y1_guess;
        y(2, n+1) = y2_guess;
    end
% complete the implementation of the Euler's method for numerical solution 
% of this problem

end
