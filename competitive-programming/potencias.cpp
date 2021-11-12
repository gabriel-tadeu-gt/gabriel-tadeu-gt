#include <iostream>
#include <cmath>

using namespace std;

int main(){
    double num1, num2;

    cout.precision(4);
    cout.setf(ios::fixed);

    cin >> num1 >> num2;
    cout << pow(num1, num2);

}
