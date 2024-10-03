def fib(n):
	if n <=1:
		return 1
	else:
		return fib(n-1) + fib(n-2)
	#endif
#end function

def fibonacci2(n):
	fib2 = 1
	fib1 = 1
	while n > 2:
		fibnew = fib1 + fib2
		fib2 = fib1
		fib1 = fibnew
		n = n-1
	#endwhile
	return fib1
#endfunction
#get