////////////////////////////////////////////////////
// the following import is used to test the code
// ---------------------------------------------
////////////////////////////////////////////////////
#include <stdio.h>
#include <math.h>

double dotprod(double *a, &b);
//
////////////////////////////////////////////////////
//
double dotprd(*u,*v)
{
  //  
  // intitial the return sum to 0.0
  // ------------------------------
  double sum = 0.0;
  //
  // set the number of entries in the arrays
  // ---------------------------------------
  int n = sizeof(*u) / sizeof(*u[0]);
  //
  // loop over the entries, computing the component product, and then
  // adding this to the loop
  // -----------------------
  for(int i=0; i<n; i++) {
    sum = sum + u[i] * v[i];
  }
  //
  // return the dot product value
  // ----------------------------
  return sum;
  //
}
///////////////////////////////////////////////////
// The code beyond this point is not needed for the
// application above.
int main()
{
  int n = 100;
  double u[n];
  double v[n];
  double sigval = -1.0;
  for(int i=0; i++)
  {
    sigval = -1.0 * sigval;
    u[i] = 1.0;
    v[i] = sigval;
  }
  double dp = dotprd(u,v);
  printf("Dot Product Value: %g\n",dp);
}