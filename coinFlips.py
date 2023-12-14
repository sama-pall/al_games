import random

print("I'll through coin 1000 times. Try to g_uess how much time Head will appear?(Press enter if you want to start)")
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads += 1
    flips += 1

    if flips == 900:
        print('900 flips and Head appeared ' + str(heads) + ' times')
    if flips == 100:
        print('100 flips and Head appeared ' + str(heads) + ' times')
    if flips == 500:
        print('500 flips and Head appeared ' + str(heads) + ' times')

print()
print('1000 flips and Head appeared ' + str(heads) + ' times')
print('How close were you to proper answer?')


