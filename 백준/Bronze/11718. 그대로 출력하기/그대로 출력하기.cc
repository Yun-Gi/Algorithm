#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    string s;
    int cont = 0;
    while(cont<100){
        getline(cin,s);
        cout<<s<<endl;
        cont++;
    }
    return 0;
}