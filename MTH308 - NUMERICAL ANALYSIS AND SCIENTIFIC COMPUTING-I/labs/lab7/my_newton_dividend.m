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

