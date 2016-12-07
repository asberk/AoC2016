function out = keypadmove(num, dirn)
out = 0;
switch dirn
    case 'U'
        switch num
            case 1
                out = 1;
            case 2
                out = 2;
            case 3
                out = 3;
            case 4
                out = 1;
            case 5
                out = 2;
            case 6
                out = 3;
            case 7 
                out = 4;
            case 8
                out = 5;
            case 9
                out = 6;
        end
    case 'R'
        switch num
            case 1
                out = 2;
            case 2
                out = 3;
            case 3
                out = 3;
            case 4
                out = 5;
            case 5
                out = 6;
            case 6
                out = 6;
            case 7 
                out = 8;
            case 8
                out = 9;
            case 9
                out = 9;
        end
        
    case 'D'
        switch num
            case 1
                out = 4;
            case 2
                out = 5;
            case 3
                out = 6;
            case 4
                out = 7;
            case 5
                out = 8;
            case 6
                out = 9;
            case 7 
                out = 7;
            case 8
                out = 8;
            case 9
                out = 9;
        end
        
    case 'L'
        switch num
            case 1
                out = 1;
            case 2
                out = 1;
            case 3
                out = 2;
            case 4
                out = 4;
            case 5
                out = 4;
            case 6
                out = 5;
            case 7 
                out = 7;
            case 8
                out = 7;
            case 9
                out = 8;
        end
        
end