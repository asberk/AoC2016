% import day3data
importDay3
% run code by rows
numValid = 0;
for j = 1:size(day3data, 1)
    numValid = numValid + describesValidTriangle(day3data(j,:));
end
display(numValid);

% run code by columns
if mod(size(day3data, 1), 3) > 0
    display('uh oh what is going on?');
end

vecValid = zeros(1,3);

for j = 1:size(day3data, 1)/3
    x = day3data(3*j + (-2:0), 1).';
    y = day3data(3*j + (-2:0), 2).';
    z = day3data(3*j + (-2:0), 3).';
    vecValid = vecValid + [describesValidTriangle(x), describesValidTriangle(y), describesValidTriangle(z)];
end
display(sum(vecValid));