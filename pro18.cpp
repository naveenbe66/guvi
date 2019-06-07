#include<bits/stdc++.h>
using namespace std;

int main(void){
    int n3, m2, temp2, max_count1=0;
    cin>>n3>>m2;

    vector<vector<int>> count(n3+1, vector<int>(m2+1));
    for(int i1=0; i1<n3; i1++){
        for(int j1=0; j1<m2; j1++){
            cin>>temp2;
            if(i1==0 || j1==0 || temp2 == 0){
                count[i1+1][j1+1] = temp2;
            } else {
                count[i1+1][j1+1] = 1 + min({count[i1][j1+1] , count[i1+1][j1], count[i1][j1]});
            }
            max_count1 = max(max_count1, count[i1+1][j1+1]);
        }
    }
    for(int i1=0; i1<max_count1; i1++){
        for(int j1=0; j1<max_count1; j1++){
            cout<<1;
            if(i1!=(max_count1-1))
            {
                cout<<" ";
            }
        }
        cout<<"\n";
    }
    return 0;
}
