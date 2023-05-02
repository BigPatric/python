#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int a,b;
    for (int i = 0; i < n; i++){
        int s=0;
        cin >> a >> b;
        for(int j=a;j<=b;j++) {
            float k=sqrt(j);
            k = int(k);
            if(k==sqrt(j)) {

                s+=j;
            }




        }
    cout<< "Case "<<i+1<<": "<<s<<endl;
    }

    return 0;
}