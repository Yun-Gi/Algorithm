#include <iostream>
#include <string>
using namespace std;

int main(){
    string name,grade;
    float jumsu;
    float aver = 0;
    int count=0;
    for(int i=0;i<20;i++){
        cin>>name>>jumsu>>grade;
        if(grade[0] == 'P'){
        }
        else if(grade == "A+"){
            aver += jumsu*4.5;
            count += jumsu;
        }
        else if(grade == "A0"){
            aver += jumsu*4.0;
            count += jumsu;
        }
        else if(grade == "B+"){
            aver += jumsu*3.5;
            count += jumsu;
        }
        else if(grade == "B0"){
            aver += jumsu*3.0;
            count += jumsu;
        }
        else if(grade == "C+"){
            aver += jumsu*2.5;
            count += jumsu;
        }
        else if(grade == "C0"){
            aver += jumsu*2.0;
            count += jumsu;
        }
        else if(grade == "D+"){
            aver += jumsu*1.5;
            count += jumsu;
        }
        else if(grade == "D0"){
            aver += jumsu*1.0;
            count += jumsu;
        }
        else if(grade == "F"){
            count += jumsu;
        }
    }
    cout<<aver/count;
}