clc;
clear;
x= input('enter x coordis as row vector: ');
f= input('values at x coordis as row vector: ');
n1=length(x);
n2=length(f);
while(n1~=n2)
    x= input('enter x coordis as row vector: ');
    f= input('values at x coordis as row vector: ');
    n1=length(x);
    n2=length(f);
end

fprintf("\n given data is :\n");
d=[' x ' ,' f(x) '];
disp(d);
disp(cell2mat(compose('%10.6f',[x;f]' )));
T=0;
for i=1:n1-1
    T=T+(f(i)+f(i+1))*(x(i+1)-x(i));
end
fprintf('\n the value of integral is: %10.6f\n',T/2);
