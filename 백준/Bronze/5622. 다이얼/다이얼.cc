#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    string s;
    cin >> s;
    int time = 0;
    for(int i = 0;i<s.size();i++){
        if(s[i]=='Z'){
            time += 10;
        }
        else{
            if(s[i]<'S'){
                int b=s[i] - 'A';
                b = b/3 + 3;
                time += b;
            }
            else if(s[i]=='S'){
                time += 8;
            }
            else{
                int b=s[i] - ('A'+1);
                b = b/3 + 3;
                time += b;
            }
        }
    }
    cout << time;
    return 0;
}