#include <iostream>
using namespace std;

int main(){
	int a,b,c;
	cin>>a>>b;
	cin>>c;
	if(b+c>=60){
		a += (b+c)/60;
		if(a>=24) a = a%24;
		b = (b+c)%60;
	}
	else{
		b = b+c;
	}
	cout<<a<<" "<<b;
	cout<<endl; return 0;
}