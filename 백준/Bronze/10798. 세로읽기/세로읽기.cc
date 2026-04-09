#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<vector<char>> A(5);
    vector<string> B(5);
    for(int i =0;i<5;i++){
        cin>>B[i];
    }
    for(int i=0;i<5;i++){
        A[i].resize(B[i].size());
    }
    for(int i=0; i<5;i++){
        for(int j=0;j<B[i].size();j++){
            A[i][j] = B[i][j];
        }
    }

    int index = 0;
    for(int i = 0;i<5;i++){
        if(index<A[i].size()){
            index=A[i].size();
        }
    }
    for(int j=0;j<index;j++){
        for(int i=0;i<5;i++){
            if(j<A[i].size()){
                cout<<A[i][j];
            }
        }
    }
    return 0;
}