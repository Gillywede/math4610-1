#include <stdio.h>
#include <math.h>
#ifdef _OPENMP
  #include <omp.h>
#else
  #define omp_get_thread_num() 1
#endif

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
