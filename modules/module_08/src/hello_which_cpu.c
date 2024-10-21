#include <stdio.h>
#include <math.h>
#include <omp.h>

int main()
{
  //
  // this is an OpenMP directive for the compiler
  //
  #pragma omp parallel
  {
    printf("Hello World! from CPU %d\n", omp_get_thread_num());
  }
}
