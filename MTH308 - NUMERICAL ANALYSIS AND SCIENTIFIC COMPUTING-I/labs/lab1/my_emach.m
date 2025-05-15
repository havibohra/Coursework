clc;
clear;
i=0;
x=2;
while x>1
    i=i+1;
    d= 2^(-i);
    x=1+d;
end
fprintf('Emach: is 2^(-%d), mantissa bits: %d\n', i-1,i-1);