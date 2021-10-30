 #include<bits/stdc++.h>

using namespace std;

int main()

{

	int n,x;

	cin>>x>>n;

	

	int arr[n];

	for(int i=0;i<n;i++)

	{

		cin>>arr[i];

	}

	int start=0,sum=arr[0],ans=INT_MAX;

	for(int i=1;i<n;i++)

	{

		sum=sum+arr[i];

		while(sum>x)

		{

			if(sum-arr[start]<=x)

			break;

			sum-=arr[start];

			ans=min(ans,i-start);

			start++;

			

			

		}

	}

	

	cout<<"\t\t\n"<<ans;

}
