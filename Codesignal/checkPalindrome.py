def  checkPalindrome ( inputString ):
    start  =  0
    end  =  len ( inputString ) - 1
    while  start  <  end :
        if  inputString [ start ] !=  inputString [ end ]:
            return  False
        start  =  start  +  1
        end  =  end  -  1
    return  True
