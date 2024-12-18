clc;
clear;

% Defining the function
f1=@ (x1, x2) 4*x1^2-20*x1+ (1/4)*x2^2+8;
f2=@ (x1, x2) (1/2)*x1*x2^2+2*x1-5*x2+8;

% Defining the Jacobian of function
df_11=@ (x1, x2) 8*x1-20;
df_12=@ (x1, x2) (1/2)*x2;
df_21=@ (x1, x2) (1/2)*x2^2+2;
df_22=@ (x1, x2) x1*x2-5;

fprintf("\n First equation of the given system is:4x_1^2-20x_1+ (1/4)x_2^2+8=0. \n");
fprintf("\n Second equation of the given system is: (1/2)x_1x_2^2+2x_1-5x_2+8=0. \n");

x= input('\n enter initial approxmn as row vector: \n');
fx= [f1(x(1),x(2)); f2(x(1),x(2)) ];
Jf = [df_11(x(1),x(2)), df_12(x(1),x(2)); df_21(x(1),x(2)), df_22(x(1),x(2))];

if fx(1)==0 && fx(2)==0
    fprintf('A root is \n');
    disp(x);
elseif det(Jf)==0
    fprintf('Newton method cannot help you with these inputs\n');
else
    n=input('enter max iteratons: ');
    tol=input('enter tolerance: ');
    X=x;
    k=1;
    while k<=n
        k=k+1;
        temp=x;
        y= Jf\fx;
        x=x-y;
        
        X=[X,x];

        fx= [f1(x(1),x(2)); f2(x(1),x(2)) ];
        Jf = [df_11(x(1),x(2)), df_12(x(1),x(2)); df_21(x(1),x(2)), df_22(x(1),x(2))];

        if fx(1)==0 && fx(2)==0
            fprintf('A root is \n');
            disp(x);
            break;
        elseif det(Jf)==0
            fprintf('Newton method cannot help you with these inputs\n');
        elseif norm(y,Inf)<=tol
            fprintf('An approx root is with tolerance(%f)\n',tol);
            disp(x);
            break;
        end
        
    end
    if k==n+1
        fprintf('\nmax %d iter reached\n',n);
    end
    disp(cell2mat(compose('%10d',1:k)));
    fprintf('\n');
    disp(cell2mat(compose('%10.6f',X)));
end

