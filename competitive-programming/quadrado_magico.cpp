#include <iostream>
using namespace std;
/*Código está errado*/
int main(){
    int n, m[11][11], sl, sla, sc, sca, sd1, sd2;
    cin >> n;
    sl = sc = sd2 = sla = sca = sd1 = 0;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> m[i][j];
        }
    }

    for(int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            sl += m[i][j];
        }
        if(sl != sla){
            cout << -1 << endl;
            break;
        } else {
            sl = 0;
        }
    }

    for(int i = 0; i < n; i++){
        sc = 0;
        for (int j = 0; j < n; j++){
            sc += m[j][i];
        }
        if(sc != sca){
            cout << -1 << endl;
            break;
        } else {
            sc = 0;
        }
    }

    for(int i = 0; i < n; i++){
        sd1 += m[i][i];
        sd2 += m[i][2 - i];
    }
    if(sd1 == sd2){
        cout << sd1 << endl;
    } else{
        cout << -1 << endl;
    }
}
