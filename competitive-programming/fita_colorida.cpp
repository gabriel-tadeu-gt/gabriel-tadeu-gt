#include <iostream>
using namespace std;

int main(){
    //10 cores 0 a 9
    int n, x, v[10000], d;
    cin >> n;
    d = 10;

    for(int i = 0; i < n; i++){
        cin >> x;
        v[i] = x;
    }
    for(int i = 0; i < n; i++){
        if(v[i] == -1){
            for(int j = i - 1; j >= 0; j--){
                if(v[j] == 0 && i - j > 0 && i - j <= d && i - j <= 9){
                    d = i - j;
                } else if(i - j >= 9 && d == 10){
                    d = 9;
                }
            }
            for(int j = 0; j < n; j++){
                if(v[j] == 0 && j - i > 0 && j - i <= d && j - i <= 9){
                    d = j - i;
                } else if (j - i >= 9 && d == 10){
                        d = 9;
                }
            }
        }
        else {
            d = 0;
        }
        cout << d << " ";
        d = 10;
    }
}
