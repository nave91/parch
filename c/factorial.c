#include<stdio.h>

int factorial(int n){
  if(n==1) return 1;
  return n * factorial(n-1);
}
void main(){
  int n = 3;
  int fact = factorial(n);
  printf("%d",fact);
}
