#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float smaceps()
{
  float one = 1.0;
  float eps = 1.0;
  float appone = one + eps;

  float error = fabs(appone-one);
  printf("%g", error);
  while(error > 0.0)
  {
    eps = eps / 2.0;
    appone = one + eps;
    error = fabs( appone - one );
  }
}

int main()
{
  printf("error = %g\n", smaceps());
}