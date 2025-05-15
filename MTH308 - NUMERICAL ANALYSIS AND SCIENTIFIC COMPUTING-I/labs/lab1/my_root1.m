a=input('enter a: ');
while(a==0)
    a=input('a cannot be zero, re-enter a: ');
end

b=input('enter b: ');
c=input('enter c: ');

M=max([abs(a),abs(b),abs(c)]);
a=a/M;
b=b/M;
c=c/M;

if(a~=0 && b^2~=0)
    if((b^2-4*a*c)<0)
        x= -b/2*a;
        y=sqrt(4*a*c-b^2)/(2*a);
        fprintf('roots: %f +i %f and %f -i %f respectively.\n',x,y,x,y);
    else
        x_1 = (-b+sqrt(b^2-4*a*c))/(2*a);
        x_2 = (-b-sqrt(b^2-4*a*c))/(2*a);
        fprintf('roots: %f and %f\n',x_1,x_2);
    end
else 
    fprintf('there is an underflow error for the inputs\n');
end
