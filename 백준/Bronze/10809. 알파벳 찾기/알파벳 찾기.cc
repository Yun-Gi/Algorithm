#include <iostream>
#include <string>
using namespace std;

int main(){
    string s;
    string alpha = "abcdefghijklmnopqrstuvwxyz";
    int lo[26]; 
    for(int k = 0; k<26;k++){
        lo[k] = -1;
    }
    cin>>s;
    for(int i =s.size();i>=0;i--){
        for(int j=0;j<26;j++){
            if(s[i] == alpha[j]){
                lo[j] = i;
            }
        }
    }
    for(int k = 0; k<26;k++){
        cout<<lo[k]<<" ";
    }
    return 0;
}