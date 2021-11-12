#include <iostream>
using namespace std;

int main(){
    int n, m[100][100], x;

    cin >> n;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            m[i][j] = 0;
        }
    }


    for (int k = 0; k < n; k++){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++){
                cin >> x;
                m[i][j] += x;
                x = 0;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++){
            cout << m[i][j] << " ";
        }
        cout << endl;
    }


}

