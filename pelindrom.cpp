 #include<bits/stdc++.h>

using namespace std;

bool fun(int arr[],int st,int end)

{

	string s="",t="";

	int g,k;

	for(int i=st;i<=end;i++)

	{

		k=arr[i];

		while(k)

		{

			g=k%10;

			t+=g;

			k=k/10;

		}

			t=string(t.rbegin(),t.rend());

			s+=t;

			t="";

	}

		t=string(s.rbegin(),s.rend());

		if(s==t)

		return true;

		else

		return false;

}

int main()

{



    int n;

    cin>>n;

    cout<<endl;

    int arr[n];

    for(int i=0;i<n;i++)

    {

    	cin>>arr[i];

	}

	cout<<endl;

     

     int k;

     cin>>k;

     cout<<endl;

     

     if(fun(arr,0,k-1))

     

     	for(int i=0;i<k;i++)

     	cout<<arr[i]<<" ";

	     cout<<endl;

	     

    for(int i=k;i<n;i++)

    {

    	if(fun(arr,i-(k-1),i))

     	for(int j=i-(k-1);j<=i;j++)

     	cout<<arr[j]<<" ";

	     cout<<endl;

	}





}
