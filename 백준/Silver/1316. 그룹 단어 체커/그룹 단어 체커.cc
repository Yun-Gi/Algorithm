#include <iostream>
#include <string>
#include <cctype>
#include <unordered_set>
using namespace std;
int groupchecker(string);
int main(){
    int n;
    cin>>n;
    int count = 0;
    for(int i =0;i<n;i++){
        string str;
        cin>>str;
        count += groupchecker(str);
    }
    cout<<count;
    return 0;
}

int groupchecker(string s){
    std::unordered_set<char> visited;

    for (int i = 0; i < s.length(); ++i) {
        char currentChar = s[i];

        // 이미 나온 문자인데 바로 전 문자와 다르면 그룹 단어가 아님
        if (visited.find(currentChar) != visited.end() && s[i - 1] != currentChar) {
            return 0;;
        }

        visited.insert(currentChar);
    }

    return 1;
}