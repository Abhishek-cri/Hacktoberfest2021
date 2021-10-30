 #include<bits/stdc++.h>

using namespace std;

int main ()

{

	int n;

	cin>>n;

	int arr[n];

	

	

	for(int i=0;i<n;i++)

	cin>>arr[i];

	cout<<"\n\t";

	

	

	int k,sum=0;

	cin>>k;

	cout<<"\n\t";

	

	for(int i=0;i<k;i++)

	sum+=arr[i];

	

	

	if(sum%3==0)

	{

		for(int i=0;i<k;i++)

		cout<<arr[i]<<" ";

		cout<<endl;

		

	}

	

	

	int st=0;

	for(int i=k;i<n;i++)

	{

		sum=sum-arr[st]+arr[i];

		st++;

	    if(sum%3==0)

	{

		for(int j=st;j<=i;j++)

		cout<<arr[j]<<" ";

		cout<<endl;

		

	}

		

		

	}

	

	

}
