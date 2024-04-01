def bisection(a, b, TOL, N0, f):
    # Step 1
    i=1
    FA=f(a)
    while i <= N0: # Step 2
        # Step 3
        p = a+(b-a)/2
        FP = f(p)
        # Step 4
        if FP == 0 or (b-a)/2 < TOL:
            return p
        # Step 5
        i=i+1
        # Step 6
        if FA * FP > 0:
            a=p
            FA=FP
        else:
            b=p
    print('Method failed after N0 iterations, N0 = {}'.format(N0))
    return p
