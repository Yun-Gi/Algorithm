#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    string str;
    string rstr;
    
    cin>>str;
    rstr = str;
    reverse(str.begin(), str.end());
    if(rstr == str){
        cout<<"1";
    }
    else{
        cout<<"0";
    }
    return 0;
}