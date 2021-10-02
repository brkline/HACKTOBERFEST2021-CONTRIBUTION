#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int main()
{
    long long n;
    cout << "No of terms : ";
    cin >> n;

    long long dp[n+1];

    dp[0] = 0;
    dp[1] = 1;

	if(n<0)
		cout<<"No of terms should be a positive number";
	else if(n<=0){}
	else if(n==1)
		cout<<dp[0];
	else if(n==2)
		cout<<dp[0]<<" "<<dp[1];
	else
	{
		cout<<dp[0]<<" "<<dp[1];
	    for(long long i = 2;i<n; i++)
    	{
        	dp[i] = dp[i-1] + dp[i-2];
        	cout << " " << dp[i];
    	}
	}
	cout<<"\n";
    return 0;
}
