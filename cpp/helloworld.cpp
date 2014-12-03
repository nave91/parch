#include<iostream>
#include<string>
using namespace std;

int main(){
  int i;
  string name;
  cout << "give your name";
  getline(cin,name);
  cout << "hello" << name << "!!";
  return 0;
}
