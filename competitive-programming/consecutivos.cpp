#include <iostream>
using namespace std;

int main(){
    int n, v, va, pts, pts_r;
    pts = pts_r = 1;

    cin >> n;
    for (int i = 0; i < n; i++){
        va = v;
        cin >> v;

        if (v == va && i != 0){
            pts += 1;
            if(pts > pts_r){
                pts_r = pts;
            }
        } else {
            pts = 1;
        }
    }


    cout << pts_r << endl;
}
