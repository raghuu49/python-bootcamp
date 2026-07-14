scores=[11,11,11]

print(max(scores[0:2]))
maxi,sec_maxi=0,0

for score in scores:
    if score>maxi:
        maxi=score
    if(score!=maxi):
        if score>sec_maxi:
            sec_maxi=score

print(f"the max is {maxi} and second max is {sec_maxi}")

sum=0
for numbers in range(1,101):
    sum+=numbers

print(sum)

