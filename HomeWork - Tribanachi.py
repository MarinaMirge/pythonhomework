N_tribonachi = [0,0,1]

i = 0
for i in range (0, len(N_tribonachi)):
    while len(N_tribonachi) <= 34:
        x = N_tribonachi[i] + N_tribonachi[i+1] + N_tribonachi[i+2]
        N_tribonachi.append(x)
        i += 1
print (N_tribonachi)

