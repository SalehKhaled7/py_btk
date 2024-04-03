# Bankamatik Uygulaması

SadikHesap = {
    'name': 'Sadık Turan',
    'accountNumber': '13245678',
    'balance': 3000,
    'adbalance': 2000
}

AliHesap = {
    'name': 'Ali Turan',
    'accountNumber': '12345678',
    'balance': 2000,
    'adbalance': 1000
}

def withdraw(account ,amount):
    print(f"Hello ,{account['name']}")
    

    if amount <= account['balance']:
        account['balance'] -= amount
        print("withdraw successfuly ! ")
        recipt(account)
    else :
        if amount <= (account['balance'] + account['adbalance']):
            reaply = input("you dont have enough balance do you want withdraw from ad Account Y/N?")
            if reaply.lower() == "y":
                
                account['adbalance'] = (account['balance'] + account['adbalance']) - amount #this changes the global !!
                account['balance'] = 0 #this changes the global !!
                #give moneya nd card
                recipt(account)
            else:
                #give card back
                print("please pick up your card")
                recipt(account)
        else:
            #give card back
            print("sorry ! you dont have enough balance !")
            recipt(account)
            

def recipt(account):
    print(f"{account['accountNumber']} have balance of :{account['balance']} and ad balance of :{account['adbalance']}")


withdraw(AliHesap,900)
withdraw(AliHesap,2000)

