#include<bits/stdc++.h>
#include "testlib.h"
#define ll long long
#define ii int
using namespace std;
int a[900][900];
bool checkVar(int var, int min_val, int max_val){
    if(min_val > var || var > max_val){
        cerr << "checkVar error (val: " << var << ", min: " << min_val << ", max: " << max_val << ")" << endl;
        return false;
    }
    return true;
}
string toStringTest(int t_id, int sz){
    string ret = "";
    while(t_id){
        ret = char(t_id % 10 + '0') + ret;
        t_id /= 10;
    }
    while(ret.length() < sz){
        ret = "0" + ret;
    }
    return ret;
}
void nPrint(string str, int n){
    if(n > 0){
        cerr << str;
        nPrint(str, n - 1);
    }
}

bool solve1(string s, string k){
    int pos = 0;
    for(int i = 0; i < s.length(); i++){
        if(pos < k.length() && s[i] == k[pos]){
            pos++;
        }
    }
    if(pos == k.length())return true;
    return false;
}
bool generateTest(int t_id){
//	srand(time(NULL));
    ///////////////////////////////
    cerr << "test #" << t_id << endl << endl;;
    nPrint("-", 100);
    cerr << endl;
    string s_inf = "tests/00" + toStringTest(t_id, 2) + ".in.txt";
    string s_ans = "tests/00" + toStringTest(t_id, 2) + ".out.txt";
    ofstream inff(s_inf.c_str());
    ofstream ansf(s_ans.c_str());
	int n,m,a;
	string s,k;
	cin>>n>>m>>a;
	inff<<n<<" "<<m<<" "<<a;
	cin>>n;
	ansf<<n;
    ///////////////////////////////
	
    inff.close();
    ansf.close();
}
main(){
	
    int t = 20;
    cerr << "Tests: ";
    cin >> t;
    for(int i = 1; i <= t; i++){
        generateTest(i);
    }
}
