def valid(email):
    if len(email)>=254:
        return 0
    num='1234567890'
    sym='~`!@#$%^&*()-+={]}[:;",<.>/?'
    for i in num:
        if email.startswith(i) or email.endswith(i):
            return 0
    for i in sym:
        if email.startswith(i) or email.endswith(i):
            return 0    
    if '@' in email:
        if email.count('@')>1:
            s1,s2=email.split('@',1)
            if s1.endswith("'") and s2.startswith("'"):
                loc,domain=s2.split('@')
                local=s1+'@'+loc
                lstatus=Validlocal(local)
                dstatus=Validdomain(domain)
                if lstatus and dstatus:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            local,domain=email.split('@')
            lstatus=Validlocal(local)
            dstatus=Validdomain(domain)
            if lstatus and dstatus:
                return 1
            else:
                return 0 
    else:
        return 0
    

def Validlocal(local):
    if len(local)>64:
        return 0
    set='~`!#$%^&@*()-=+]}[{;:"/.,<>?}]'
    num='1234567890'
    for i in set:
        if local.startswith(i) or local.endswith(i):
            return 0  
    i=0     
    for i in range(len(num)):
        if local[0]==num[i]:
            return 0
    if ' ' in local:
        l1,l2=local.split(' ')
        if l1.endswith("'") and l2.startswith("'"):
            status=1
        else:
            return 0
    for i in set:
        if i in local:
            if local.count(i)>1:
                return 0
            else:
                l3,l4=local.split(i)
                if l3.endswith("'") and l4.startswith("'"):
                    return 1
                else:
                    return 0
    return 1        


def Validdomain(domain):
    if len(domain)<7:
        return 0
    if domain.startswith('-') or domain.endswith('-'):
        return 0
    if '.' in domain:
        if domain.count('.')>1:
            return 0  
        else:
           dset='!@#$%^&*(_}={][;:,<>/?'
           for i in dset:
                if i in domain:
                    return 0
    else:
        return 0            
    d1,d2=domain.split('.')
    if d2=='com' or d2=='org' or d2=='edu':
        return 1
    else:
        return 0
    

def Interactive():                 
    email=str(input("Enter your email :"))
    if valid(email):
        print(email,' is Valid')
    else:
        print(email,' is Invalid')           

print("This is the Interactive Mode of Email Validation \n")
option='y' or 'y'
while(option=='y' or option=='Y'):
    Interactive()
    option=str(input("Do you Wish to check another email (y/n) :"))
print("You are Done With this Session :) ")