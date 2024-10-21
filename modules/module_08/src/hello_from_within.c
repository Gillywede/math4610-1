#include <stdio.h>
#include <math.h>

int main()
{
  //
  // this is an OpenMP directive for the compiler
  //
  #pragma omp parallel
  {
    printf("Hello World!\n");
  }
}
