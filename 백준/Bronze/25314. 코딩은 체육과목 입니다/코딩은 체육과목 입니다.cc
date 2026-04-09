#include <iostream>
using namespace std;

int main(){
   int n,m;
   cin>>n;
   m = n/4;
   string s="";
   for(int i = 0; i < m; i++){
      s += "long ";
   } 
   cout<<s<<"int";
}