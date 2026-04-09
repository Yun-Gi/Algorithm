#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main(){
    string str;
    cin>>str;
    int count = str.size();
    for(int i = 0;i<str.size();i++){
        if(str[i]=='c'){
            if(str[i+1] == '='||str[i+1] == '-'){
                i++;
                count--;
            }
        }
        if(str[i]=='d'){
            if(str[i+1] == '-'){
                i++;
                count--;
            }
            else if(str[i+1]=='z'){
                if(str[i+2]=='='){
                    i++;
                    i++;
                    count -= 2;
                }
            }
        }
        if(str[i]=='l'||str[i]=='n'){
            if(str[i+1] == 'j'){
                i++;
                count--;
            }
        }
        if(str[i]=='s'||str[i]=='z'){
            if(str[i+1] == '='){
                i++;
                count--;
            }
        }
    }
    cout<<count;
    return 0;
}