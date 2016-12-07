function out = describesValidTriangle(x)
out = 1;
if x(1) + x(2) <= x(3) 
    out = 0;
elseif x(2) + x(3) <= x(1) 
    out = 0;
elseif x(1) + x(3) <= x(2)
    out = 0;
end
    