#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin>>n;
    int wpaper[100][100]={};
    vector<vector<int>> bpaper(n,vector<int>(2,0));

    for(int i=0;i<n;i++){
        cin>>bpaper[i][0]>>bpaper[i][1];
    }
    for(int a=0;a<n;a++){
    for(int i=bpaper[a][0];i<bpaper[a][0]+10;i++){
        for(int j = bpaper[a][1];j<bpaper[a][1]+10;j++){
            wpaper[i][j] = 1;
        }
    }
    }
    int sum=0;
    for(int i=0;i<100;i++){
        for(int j =0;j<100;j++){
            sum+=wpaper[i][j];
        }
    }
    cout<<sum;
    return 0;
}