with open('input.txt') as file_in, open('output.txt', 'w') as file_out:
    line=file_in.readline().strip()
    i=0
    out_line=''
    letters=[]
    letter_indexes=[]
    cyfers=[]
    while i < len(line):
        if not line[i].isdigit():
            letters+=line[i]
            letter_indexes+=[i]
        i+=1
    for i in range(len(letters)):
        if i != len(letters)-1:
            cyfers+=[int(line[letter_indexes[i]+1:letter_indexes[i+1]])]
        else:
            cyfers+=[int(line[letter_indexes[i]+1:])]

    i=0
    while i<len(letters):
        out_line+=str(letters[i] * cyfers[i])
        i+=1

    file_out.write(out_line)