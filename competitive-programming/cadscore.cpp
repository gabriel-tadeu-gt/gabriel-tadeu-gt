#include <iostream>
using namespace std;

int main(){
    int pontuacao, n, variacao;

    cin >> pontuacao >> n;

    for (int i = 0; i < n; i++){
        cin >> variacao;
        pontuacao += variacao;

        if (pontuacao > 100){
            pontuacao = 100;
        } else if(pontuacao < 0){
            pontuacao = 0;
        }
    }
    cout << pontuacao << endl;
}
