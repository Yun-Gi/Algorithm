#include <iostream>
#include <string>
using namespace std;

int main(){
    string s;
    getline(cin,s);
    int cot = 0;
    if(s.empty() || s == " " || s == "  "){
        cout<<cot;
        return 0;
    }
    for(int i=0;i<s.size();i++){
        if(s[i] == ' ' && i!=0 && i!=s.size()-1){
            cot++;
        }
    }
    
    cout << cot+1; 
    return 0;
}