#include <stdio.h>
int main(){
    char name[100];
    int old_pin, old_pin2, new_pin;
    int c,loop = 1;
    
    printf("\n");
    printf("\n");

    printf("Welcome to SBI \n");
    printf("\n");
    printf("Enter Account Holder Name : ");
    scanf("%s",name);
    printf("Enter Your Pin : ");
    scanf("%d",&old_pin);
    printf("\n");
    printf("WELCOME DEAR CUSTOMER \n");

    printf("\n");

    int choice;
    int amount=0; 
    int newamount;

    while (loop) {
        printf("Press : \n"); 
        printf("1 For Cash Deposit \n");
        printf("2 For Cash Withdrawl \n");
        printf("3 For Pin Update \n");
        printf("4 For Account info \n");
        printf("5 Exit \n");
        scanf("%d",&choice);
        
        printf("\n");
        
        if (choice == 1){    
            int new_amount;
            printf(">>>>>  Enter the Amount : ");
            scanf("%d",&newamount);
            amount=amount+newamount;
            printf("\n");
            printf(">>>>>  AMOUNT DEPOSITED \n");
        
            printf("\n");

        }else if (choice == 2){
            printf(">>>>>  Enter Amount To Withdsraw : ");
            scanf("%d",&newamount);
            if (amount<newamount){
                printf("\n");
                printf(">>>>>  Insufficient Balance \n");
            }else if (newamount == 0){
                printf("\n");
                printf(">>>>>  Amount Entered Cannot Be '0' \n");
            }else if (newamount >= 500){
                amount = amount-newamount;
                printf("\n");
                printf(">>>>>  AMOUNT WITHDRAWN \n");        
            }else{
                printf(">>>>>  Amount cannot be less than 500\n");
            }
            printf("\n");
            
        }else if (choice == 3){
            printf(">>>>>  Enter Old Pin : ");
            scanf("%d",&old_pin2);
            if (old_pin2 == old_pin){
                printf(">>>>>  Enter New Pin : ");
                scanf("%d",&new_pin);
                if (new_pin == old_pin){
                    printf(">>>>>  \nPIN CANT BE SAME, ENTER A DIFFERENT PIN \n");
                    printf("\n");
                }
                else if (old_pin = new_pin){;  
                printf("\n");
                printf(">>>>>  PIN UPDATED \n");
                printf("\n");
                }
                }else{
                    printf(">>>>>  INVALID PIN ENTERED \n");
                    printf("\n");                             
                }
        }else if (choice == 4){
            printf(">>>>>  ACCOUNT INFO :- \n");
            printf("\n");
            printf("Name : %s\n ", name);
            printf("Account Pin : %d\n",old_pin);
            printf("Balance : %d\n",amount);
        
            printf("\n");

        }else if (choice == 5){
            printf("Thank You, Visit Again !\n");
            printf("\n");
            loop = 0;
        }
    }
    
}
        
