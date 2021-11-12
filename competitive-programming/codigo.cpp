#include <iostream>
using namespace std;

int main(){
    int t, e, n_seq;
    int v[10000];
    cin >> t;
    n_seq = 0;

    for(int i = 0; i < t; i++){
        cin >> e;
        v[i] = e;
    }

    for(int i = 0; i < t; i++){
        if(v[i] == 1){
            if(i + 1 < t && v[i + 1] == 0){
                if(i + 2 < t && v[i+2] == 0){
                        n_seq++;
                }
            }
        }
    }

    cout << n_seq << endl;

}
