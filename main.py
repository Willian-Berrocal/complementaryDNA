# Este programa traduce un dna de entrada (string) en su complementario A<>T, G<>C
# El tiempo de ejecucion es O(n), siendo n el size del dna

dna = 'ATTGC'
#dna = 'AAGTGGGATCGGAATCCTCCTCGTT'
#dna = 'GGAAACGAGAAACTACTATA'

dnaC = ''

for c in dna:
    if c == 'A':
        dnaC += 'T'
    elif c == 'T':
        dnaC += 'A'
    elif c == 'G':
        dnaC += 'C'
    elif c == 'C':
        dnaC += 'G'

print(dnaC)