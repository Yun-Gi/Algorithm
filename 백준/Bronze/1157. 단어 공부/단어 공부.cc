#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main(){
    string str;
    cin>>str;
    for(auto& c : str){
        c= toupper(c);
    }
    int count[26] = {};
    for(auto& c : str){
        count[c-'A']++;
    }
    int maxval = -1;
    int ind =-1;
    for(int i=0;i<26;i++){
         if(maxval<count[i]){
            maxval = count[i];
            ind = i;
         }
    }
    for(int i=0;i<26;i++){
         if(count[i] == maxval && i!=ind){
            cout<<"?";
            return 0;
         }
    }
    
    char result = 'A' + ind;
    cout<<result;

    return 0;
}