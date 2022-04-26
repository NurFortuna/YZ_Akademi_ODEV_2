
def inputs():
    
    hour=int(input("hour of the day: "))
    #print(hour)
    if (hour>24 or hour<0):
        raise Exception("ınputs not in the specified range")
    
    minute=input("minutes: ")
    minute=int(minute)
    if (minute>60 or minute<0):
        raise Exception("ınputs not in the specified range")
    

    return hour,minute

def timeInWord(h,m):
    
    # h:the hour of the day
    # m:  the minutes after the hour

    time=""
   
    #input h is int
    #input m is string(convert to int before use it)
    m=int(m)
    
    
    minutes={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",
             8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"Thirteen",14:"Fourteen",
           16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Eighteen",20:"Twenty",21:"Twenty-one",22:"Twenty-two",
           23:"Twenty-three",24:"Twenty-four",25:"Twenty-five",26:"Twenty-six",27:"Twenty-seven",
           28:"Twenty-eight",29:"Twenty-nine"}
    
  
    hours={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",
           8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve"}
    
    #24 hour time to 12 hour time convert
    if(h>12 and h<24):
        h=h%12
        if(h==0):
            h=12
        #print(h)
      
    #At minutes = 0, => “o'clock”
    if(m==0):
       time=hours[h]+" o'clock"
    
    #For 1≤ minutes≤ 30 => “past”
    elif(m<=30 and m>=0):
        if(m==15):
            time="Quarter past "+hours[h]
        elif(m==30):
            time="Half past "+hours[h]
        else:
            time=minutes[m]+" minutes past "+hours[h]
        
    # for 30< minutes => “to”.
    elif(m>30 and m<60):
        if(m==45):
            time="Quarter to "+hours[h+1]
        else:
            m=60-m
            time=minutes[m]+" minutes to "+hours[h+1]
        
        
    return time


h,m=inputs()
print("------------------------------------------------")
print(timeInWord(h,m))


