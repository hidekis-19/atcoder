import time


if __name__ == '__main__':
    start = time.time()
    S = [1,2,3,4,5]
    T = 1
    ans = 1
    for _ in range(10*100000):
        # if S[2] == T:
        #     ans = 1
        # else:
        #     ans = 0
        if S[2] != T:
            ans = 1
        else:
            ans = 0


    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
