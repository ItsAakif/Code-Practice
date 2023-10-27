#include <iostream>
using namespace std;

int main() {
	int n;
	cin>>n;
	for(int t=0;t<n;t++)
	{       
	        int N;
	        double SR;
	        cin>>N;
	        int A[N];
	        
	        for(int i=0;i<N;i++)
	        {
	            cin>>A[i];
	            
	        }
	        
	        double sum=0,count=0;
	        for(int i=0;i<N;i++)
	       {
	            sum=sum+A[i];
	            SR=(sum/(i+1))*100;
	           // cout<<SR<<endl;
	            if(SR==100)
	            count++;
	       }
	        cout<<count<<endl;
	}   
	
	return 0;
}
