#include <iostream>
using namespace std;

int main(){
    int n;
    int campo[50];

    cin >> n;

    for(int i = 0; i < n; i++){
        cin >> campo[i];
    }

    for(int i = 0; i < n; i++){
        int bombas = 0;

        if (i != 0){
           bombas += campo[i - 1];
        }

        bombas += campo[i];

        if(i != n - 1){
            bombas += campo[i + 1];
        }

        cout << bombas << endl;

    }
}
