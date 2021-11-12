#include <iostream>
using namespace std;

int main(){
    int n, acesso_dia, acessos_totais, contador, dias_necessarios;

    cin >> n;
    contador = 0;
    acessos_totais = 0;
    dias_necessarios = 0;

    while (contador < n) {
            cin >> acesso_dia;
            acessos_totais += acesso_dia;
            contador += 1;
            if (acessos_totais >= 1000000 && dias_necessarios == 0) {
                dias_necessarios = contador;
            }
    }
    cout << dias_necessarios << endl;
}
