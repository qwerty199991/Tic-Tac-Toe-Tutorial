army = int(input())
if army < 1:
    print('no army')
elif army >= 1 and army <= 9:
    print('few')
elif army >= 10 and army <= 49:
    print('pack')
elif army >= 50 and army <= 499:
    print('horde')
elif army >= 500 and army <= 999:
    print('swarm')
else:
    print('legion')
