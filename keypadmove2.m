function out = keypadmove2(num, dirn)
% KEYPADMOVE2 determines the next key in the sequence given num and dirn
% The actual keypad looks like: 
%     1
%   2 3 4
% 5 6 7 8 9 
%   A B C 
%     D

out = 0;
switch dirn
    case 'U'
        switch num
            case 1
                out = 1;
            case 2
                out = 2;
            case 3
                out = 1;
            case 4
                out = 4;
            case 5
                out = 5;
            case 6
                out = 2;
            case 7 
                out = 3;
            case 8
                out = 4;
            case 9
                out = 9;
            case 'A'
                out = 6;
            case 'B'
                out = 7;
            case 'C'
                out = 8;
            case 'D'
                out = 'B';
        end
    case 'R'
        switch num
            case 1
                out = 1;
            case 2
                out = 3;
            case 3
                out = 4;
            case 4
                out = 4;
            case 5
                out = 6;
            case 6
                out = 7;
            case 7 
                out = 8;
            case 8
                out = 9;
            case 9
                out = 9;
            case 'A'
                out = 'B';
            case 'B'
                out = 'C';
            case 'C'
                out = 'C';
            case 'D'
                out = 'D';
        end
        
    case 'D'
        switch num
            case 1
                out = 3;
            case 2
                out = 6;
            case 3
                out = 7;
            case 4
                out = 8;
            case 5
                out = 5;
            case 6
                out = 'A';
            case 7 
                out = 'B';
            case 8
                out = 'C';
            case 9
                out = 9;
            case 'A'
                out = 'A';
            case 'B'
                out = 'D';
            case 'C'
                out = 'C';
            case 'D'
                out = 'D';
        end
        
    case 'L'
        switch num
            case 1
                out = 1;
            case 2
                out = 2;
            case 3
                out = 2;
            case 4
                out = 3;
            case 5
                out = 5;
            case 6
                out = 5;
            case 7 
                out = 6;
            case 8
                out = 7;
            case 9
                out = 8;
            case 'A'
                out = 'A';
            case 'B'
                out = 'A';
            case 'C'
                out = 'B';
            case 'D'
                out = 'D';
        end
        
end