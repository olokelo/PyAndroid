# Made for pyandroid <= 1.1
def code(data):
    
    code = 0
    final = ''
    while code < len(data):
        ch = data[code:code+1] 
        if True:
            if ch == 'a':
                final += '&10 '
            elif ch == 'A':
                final += '&11 '
            elif ch == 'b':
                final += '&20 '
            elif ch == 'B':
                final += '&21 '
            elif ch == 'c':
                final += '&30 '
            elif ch == 'C':
                final += '&31 '
            elif ch == 'd':
                final += '&40 '
            elif ch == 'D':
                final += '&41 '
            elif ch == 'e':
                final += '&50 '
            elif ch == 'E':
                final += '&51 '
            elif ch == 'f':
                final += '&60 '
            elif ch == 'F':
                final += '&61 '
            elif ch == 'g':
                final += '&70 '
            elif ch == 'G':
                final += '&71 '
            elif ch == 'h':
                final += '&80 '
            elif ch == 'H':
                final += '&81 '
            elif ch == 'i':
                final += '&90 '
            elif ch == 'I':
                final += '&91 '
            elif ch == 'j':
                final += '$10 '
            elif ch == 'J':
                final += '$11 '
            elif ch == 'k':
                final += '$20 '
            elif ch == 'K':
                final += '$21 '
            elif ch == 'l':
                final += '$30 '
            elif ch == 'L':
                final += '$31 '
            elif ch == 'm':
                final += '$40 '
            elif ch == 'M':
                final += '$41 '
            elif ch == 'n':
                final += '$50 '
            elif ch == 'N':
                final += '$51 '
            elif ch == 'o':
                final += '$60 '
            elif ch == 'O':
                final += '$61 '
            elif ch == 'p':
                final += '$70 '
            elif ch == 'P':
                final += '$71 '
            elif ch == 'q':
                final += '$80 '
            elif ch == 'Q':
                final += '$81 '
            elif ch == 'r':
                final += '$90 '
            elif ch == 'R':
                final += '$91 '
            elif ch == 's':
                final += '#10 '
            elif ch == 'S':
                final += '#11 '
            elif ch == 't':
                final += '#20 '
            elif ch == 'T':
                final += '#21 '
            elif ch == 'u':
                final += '#30 '
            elif ch == 'U':
                final += '#31 '
            elif ch == 'v':
                final += '#40 '
            elif ch == 'V':
                final += '#41 '
            elif ch == 'w':
                final += '#50 '
            elif ch == 'W':
                final += '#51 '
            elif ch == 'x':
                final += '#60 '
            elif ch == 'X':
                final += '#61 '
            elif ch == 'y':
                final += '#70 '
            elif ch == 'Y':
                final += '#71 '
            elif ch == 'z':
                final += '#80 '
            elif ch == 'Z':
                final += '#81 ' 
            elif ch == '.':
                final += '#90 '
            elif ch == ',':
                final += '#91 '
            elif ch == ':':
                final += '#92 '
            elif ch == '"':
                final += '#93 ' 
            elif ch == "'":
                final += '#94 '
            elif ch == ';':
                final += '#95 '
            elif ch == '(':
                final += '#96 '
            elif ch == ')':
                final += '#97 ' 
            elif ch == ' ':
                final += '#98 '
            elif ch == '/':
                final += '#99 '
            elif ch == '0':
                final += '@10 '
            elif ch == '1':
                final += '@11 ' 
            elif ch == '2':
                final += '@12 '
            elif ch == '3':
                final += '@13 ' 
            elif ch == '4':
                final += '@14 '
            elif ch == '5':
                final += '@15 ' 
            elif ch == '6':
                final += '@16 '
            elif ch == '7':
                final += '@17 ' 
            elif ch == '8':
                final += '@18 '
            elif ch == '9':
                final += '@19 ' 
            elif ch == '+':
                final += '@20 '
            elif ch == '=':
                final += '@21 ' 
            elif ch == '-':
                final += '@22 '
            elif ch == '%':
                final += '@23 ' 
            elif ch == '_':
                final += '@24 '
            elif ch == '|':
                final += '@25 ' 
            elif ch == '\\':
                final += '@26 '
            elif ch == '*':
                final += '@27 ' 
            elif ch == '?':
                final += '@28 '
            elif ch == '!':
                final += '@29 '
            elif ch == '[':
                final += '@30 ' 
            elif ch == ']':
                final += '@31 '
            elif ch == '{':
                final += '@32 ' 
            elif ch == '}':
                final += '@33 '
            elif ch == '<':
                final += '@34 '
            elif ch == '>':
                final += '@35 '
            elif ch == '\n':
                final += '@36 '
            else:
                final += '&00 '
            code += 1
    return final

def decode(data):
    code = 0
    final = ''
    while code < len(data):
        ch = data[code:code+4]
        if True:
            if ch == '&10 ':
                final += 'a'
            elif ch == '&11 ':
                final += 'A'
            elif ch == '&20 ':
                final += 'b'
            elif ch == '&21 ':
                final += 'B'
            elif ch == '&30 ':
                final += 'c'
            elif ch == '&31 ':
                final += 'C'
            elif ch == '&40 ':
                final += 'd'
            elif ch == '&41 ':
                final += 'D'
            elif ch == '&50 ':
                final += 'e'
            elif ch == '&51 ':
                final += 'E'
            elif ch == '&60 ':
                final += 'f'
            elif ch == '&61 ':
                final += 'F'
            elif ch == '&70 ':
                final += 'g'
            elif ch == '&71 ':
                final += 'G'
            elif ch == '&80 ':
                final += 'h'
            elif ch == '&81 ':
                final += 'H'
            elif ch == '&90 ':
                final += 'i'
            elif ch == '&91 ':
                final += 'I'
            elif ch == '$10 ':
                final += 'j'
            elif ch == '$11 ':
                final += 'J'
            elif ch == '$20 ':
                final += 'k'
            elif ch == '$21 ':
                final += 'K'
            elif ch == '$30 ':
                final += 'l'
            elif ch == '$31 ':
                final += 'L'
            elif ch == '$40 ':
                final += 'm'
            elif ch == '$41 ':
                final += 'M'
            elif ch == '$50 ':
                final += 'n'
            elif ch == '$51 ':
                final += 'N'
            elif ch == '$60 ':
                final += 'o'
            elif ch == '$61 ':
                final += 'O'
            elif ch == '$70 ':
                final += 'p'
            elif ch == '$71 ':
                final += 'P'
            elif ch == '$80 ':
                final += 'q'
            elif ch == '$81 ':
                final += 'Q'
            elif ch == '$90 ':
                final += 'r'
            elif ch == '$91 ':
                final += 'R'
            elif ch == '#10 ':
                final += 's'
            elif ch == '#11 ':
                final += 'S'
            elif ch == '#20 ':
                final += 't'
            elif ch == '#21 ':
                final += 'T'
            elif ch == '#30 ':
                final += 'u'
            elif ch == '#31 ':
                final += 'U'
            elif ch == '#40 ':
                final += 'v'
            elif ch == '#41 ':
                final += 'V'
            elif ch == '#50 ':
                final += 'w'
            elif ch == '#51 ':
                final += 'W'
            elif ch == '#60 ':
                final += 'x'
            elif ch == '#61 ':
                final += 'X'
            elif ch == '#70 ':
                final += 'y'
            elif ch == '#71 ':
                final += 'Y'
            elif ch == '#80 ':
                final += 'z'
            elif ch == '#81 ':
                final += 'Z'
            elif ch == '#90 ':
                final += '.'
            elif ch == '#91 ':
                final += ','
            elif ch == '#92 ':
                final += ':'
            elif ch == '#93 ':
                final += '"' 
            elif ch == '#94 ':
                final += "'"
            elif ch == '#95 ':
                final += ';'
            elif ch == '#96 ':
                final += '('
            elif ch == '#97 ':
                final += ')' 
            elif ch == '#98 ':
                final += ' '
            elif ch == '#99 ':
                final += '/'
            elif ch == '@10 ':
                final += '0'
            elif ch == '@11 ':
                final += '1' 
            elif ch == '@12 ':
                final += '2'
            elif ch == '@13 ':
                final += '3' 
            elif ch == '@14 ':
                final += '4'
            elif ch == '@15 ':
                final += '5' 
            elif ch == '@16 ':
                final += '6'
            elif ch == '@17 ':
                final += '7' 
            elif ch == '@18 ':
                final += '8'
            elif ch == '@19 ':
                final += '9' 
            elif ch == '@20 ':
                final += '+'
            elif ch == '@21 ':
                final += '=' 
            elif ch == '@22 ':
                final += '-'
            elif ch == '@23 ':
                final += '%' 
            elif ch == '@24 ':
                final += '_'
            elif ch == '@25 ':
                final += '|' 
            elif ch == '@26 ':
                final += '\\'
            elif ch == '@27 ':
                final += '*' 
            elif ch == '@28 ':
                final += '?'
            elif ch == '@29 ':
                final += '!'
            elif ch == '@30 ':
                final += '[' 
            elif ch == '@31 ':
                final += ']'
            elif ch == '@32 ':
                final += '{' 
            elif ch == '@33 ':
                final += '}'
            elif ch == '@34 ':
                final += '<'
            elif ch == '@35 ':
                final += '>'
            elif ch == '@36 ':
                final += '\n'
            else:
                final += ' '
            code += 4
    return final

#Future
def uni_code(char):
    if char == 'ä':
        final = '&12 '
    elif char == 'Ä':
        final = '&13 '
    elif char == 'ą':
        final = '&14 '
    elif char == 'Ą':
        final = '&15 '
    elif char == 'å':
        final = '&16 '
    elif char == 'Å':
        final = '&17 '
    elif char == 'ç':
        final = '&32 '
    elif char == 'ç':
        final = '&33 '
    elif char == 'ć':
        final = '&34 '
    elif char == 'Ć':
        final = '&35 '
    elif char == 'ë':
        final = '&52 '
    elif char == 'ę':
        final = '&54 '
    elif char == 'Ę':
        final = '&55 '
    elif char == 'ï':
        final = '&92 '
    elif char == 'î':
        final = '&94 '
    elif char == 'Î':
        final = '&95 '
    else:
        final = '!00 '