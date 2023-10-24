import java.util.Scanner;

public class FKnapsack_DP 
{
    static float[] p,wt, pw;
    static int C, n;

    static void fractionalKnapsack()
    {
        float[] x=new float[n+1];  // x is the solution vector
        float tp=0;    // tp=total profit
        int i,j,w;
        w=C;        // w is the remaining capacity of the knapsack
        for(i=1;i<=n;i++)
            x[i]=0;
        
        for(i=1;i<=n;i++)
        {
            if(w<wt[i])
                break;
            else
            {
                x[i]=1;
                tp=tp+p[i];   
                w=w-(int)wt[i];  
            }
        }
        if(i<=n)
            x[i]=w/wt[i];
        
        tp=tp+(x[i]*p[i]);  
        System.out.println("The solution vector is: ");
        for(i=1;i<=n;i++)
            System.out.print(x[i]+" ");
        
        System.out.println("\nMaximum Profit: "+tp);

    }
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of items");
        n=sc.nextInt();  // n is the number of items

        System.out.println("Enter the items Profit: ");
        p=new float[n+1];
        for(int i=1;i<=n;i++)
            p[i]=sc.nextFloat();  // p is the profit array
        
        System.out.println("Enter the items Weight: ");
        wt=new float[n+1];
        for(int i=1;i<=n;i++)
            wt[i]=sc.nextFloat();  // wt is the weight array
        
        for(int i=1;i<=n;i++)
            pw[i]=p[i]/wt[i];   // pw is the profit/weight array
        
        System.out.println("Enter the capacity of the knapsack: ");
        C=sc.nextInt();  // C is the capacity of the knapsack

        System.out.println("The Fractional Knapsack Problem Using Dynamic Programming: ");
        fractionalKnapsack();
    }
}