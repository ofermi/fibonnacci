import random
import sched, time



s = sched.scheduler(time.time, time.sleep)

def fibonacci_print(sc):
 
    nterms=random.randint(3, 100)

      
    n1, n2 = 0, 1
    count = 0

    # generate fibonacci sequence
 
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

    sc.enter(60, 1, fibonacci_print, (sc,))   
   

s.enter(60, 1, fibonacci_print, (s,))
s.run()   
        