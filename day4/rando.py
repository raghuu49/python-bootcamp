import random
i,head_count,tail_count=0,0,0

while(i<10000000):
    random_number=random.random()
    if random_number<=0.5:
        # print('Head')
        head_count+=1
    else:
        # print('Tail')
        tail_count+=1
    i+=1
print(f'head count is {head_count/10000000 * 100}, tail count is {tail_count/10000000 * 100}')