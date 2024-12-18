fprintf("\t k \t\t\t h \t\t f'_h \t f'(1) \t Abs.Error\n");
format long
x=zeros(1,18);
y=zeros(1,18);
for k = 1:18
    h= 10^(-k);
    f_h= (sin(1+h)-sin(1))/h;
    AE= abs(cos(1)-f_h);
    disp([k, h, f_h, cos(1), AE]);
    x(k)=h;
    y(k)=AE;
end

loglog(x,y,'--ro');
xlabel('h');
ylabel('AE_{1,sin}(h)');
