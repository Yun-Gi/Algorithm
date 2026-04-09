#include <iostream>
#include <string>
using namespace std;

int main(){
    string S,P;
    int R,T;
    cin>>T; //테스트 갯수
    for(int i=0;i<T;i++){
        cin>>R>>S; //반복횟수,  최초문자열
        P="";
        for(int j=0;j<S.size();j++){
            for(int k=0;k<R;k++){
                P+=S[j];
            }
        }
        cout<<P<<endl;
    }
    return 0;
}