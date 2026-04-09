#include <iostream>
using namespace std;

int main(){
	int a,b;
	cin>>a;
	cin>>b;
	int b1 = b%10; int b2 = (b % 100)/10; int b3 = b/100;
	cout<<a*b1<<endl;
	cout<<a*b2<<endl;
	cout<<a*b3<<endl;
	cout<<a*b;
	cout<<endl;return 0;
}