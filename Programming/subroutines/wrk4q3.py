def getPword(attempt):
    if attempt == 1:
        print("enter password")
    elif attempt == 2:
        print("re-enter password")
    #endif
    pword = str(input())
    if len(pword) < 6 or len(pword)> 8:
        print("error password must be between 6 and 8 characters!")
    else:
        return(pword)
    #endif
#endfunction

attempt = 1
getPword(attempt)