ebhq = {'R4'; 'R3'; 'L3'; 'L2'; 'L1'; 'R1'; 'L1'; 'R2'; 'R3'; 'L5'; 'L5'; 'R4'; 'L4'; 'R2'; 'R4'; 'L3'; 'R3'; 'L3'; 'R3'; 'R4'; 'R2'; 'L1'; 'R2'; 'L3'; 'L2'; 'L1'; 'R3'; 'R5'; 'L1'; 'L4'; 'R2'; 'L4'; 'R3'; 'R1'; 'R2'; 'L5'; 'R2'; 'L189'; 'R5'; 'L5'; 'R52'; 'R3'; 'L1'; 'R4'; 'R5'; 'R1'; 'R4'; 'L1'; 'L3'; 'R2'; 'L2'; 'L3'; 'R4'; 'R3'; 'L2'; 'L5'; 'R4'; 'R5'; 'L2'; 'R2'; 'L1'; 'L3'; 'R3'; 'L4'; 'R4'; 'R5'; 'L1'; 'L1'; 'R3'; 'L5'; 'L2'; 'R76'; 'R2'; 'R2'; 'L1'; 'L3'; 'R189'; 'L3'; 'L4'; 'L1'; 'L3'; 'R5'; 'R4'; 'L1'; 'R1'; 'L1'; 'L1'; 'R2'; 'L4'; 'R2'; 'L5'; 'L5'; 'L5'; 'R2'; 'L4'; 'L5'; 'R4'; 'R4'; 'R5'; 'L5'; 'R3'; 'L1'; 'L3'; 'L1'; 'L1'; 'L3'; 'L4'; 'R5'; 'L3'; 'R5'; 'R3'; 'R3'; 'L5'; 'L5'; 'R3'; 'R4'; 'L3'; 'R3'; 'R1'; 'R3'; 'R2'; 'R2'; 'L1'; 'R1'; 'L3'; 'L3'; 'L3'; 'L1'; 'R2'; 'L1'; 'R4'; 'R4'; 'L1'; 'L1'; 'R3'; 'R3'; 'R4'; 'R1'; 'L5'; 'L2'; 'R2'; 'R3'; 'R2'; 'L3'; 'R4'; 'L5'; 'R1'; 'R4'; 'R5'; 'R4'; 'L4'; 'R1'; 'L3'; 'R1'; 'R3'; 'L2'; 'L3'; 'R1'; 'L2'; 'R3'; 'L3'; 'L1'; 'L3'; 'R4'; 'L4'; 'L5'; 'R3'; 'R5'; 'R4'; 'R1'; 'L2'; 'R3'; 'R5'; 'L5'; 'L4'; 'L1'; 'L1'};
%ebhq = {'R2'; 'R2'; 'R2'};

dirn = ['N', 'E', 'S', 'W'];

d = 1;
net_x = 0; 
net_y = 0;

for ctr = 1:length(ebhq)
    j = ebhq{ctr};
    if j(1) == 'R'
        d = d + 1;
        if d > 4
            d = 1;
        end
    else
        d = d - 1;
        if d < 1
            d = 4;
        end
    end
    jj = str2double(j(2:end));
    if d == 1
        net_y = net_y + jj;
    elseif d == 2
        net_x = net_x + jj;
    elseif d == 3
        net_y = net_y - jj;
    elseif d == 4
        net_x = net_x - jj;
    end
end

display(norm([net_x, net_y], 1));

% 546 is too high
% 288
% 82 is too low