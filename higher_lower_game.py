from random import randint

answer=True
Q1=input('Enter the star_1 name: ')
Q1_followers_=randint(1,100000000)
while answer:
    Q2=input('Enter the star_2 name: ')
    Q2_followers_=randint(1,100000000)
    # print('Q1_followers_ = ',Q1_followers_,'Q2_followers_',Q2_followers_)

    guess=input("Enter who has more followers '1' or '2' : ")
    
    if Q1_followers_>Q2_followers_ and guess=='1':
        print('Correct!, Good Job...')
        print('Q1_followers_ = ',Q1_followers_,'Q2_followers_',Q2_followers_)
        Q1=Q2
        Q1_followers_=Q2_followers_

    elif Q1_followers_<Q2_followers_ and guess=='2':
        print('Correct!, Good Job...')
        print('Q1_followers_ = ',Q1_followers_,'Q2_followers_',Q2_followers_)

        Q1=Q2
        Q1_followers_=Q2_followers_

    else:
        print('sorry!, you loose...')
        print('Q1_followers_ = ',Q1_followers_,'Q2_followers_',Q2_followers_)

        answer=False


        



    # answer==False
