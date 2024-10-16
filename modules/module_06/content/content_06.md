# Roundoff Error in Approximations Assignment

---

## The Main Question for Math 4610 at USU

---

The following is a list of tasks to complete for this module.

* Show that the second derivative approximation
  $$
    f''(x) \approx \frac{2\ U_i - 5\ U_{i-1} + 4 U_{i-2} - U_{i-3}}{\Delta x^2}
  $$
  converges as $\Delta x\rightarrow 0$.

* For the approximation, determine the order of accuracy using Taylor
  series expansions.

* Determine where the approximation starts to fail due to
  roundoff error. This means you will need to write a code
  that implements the difference approximation. Use
  $f(x)=e^{-\pi x}$ at $x=0$ to test the result.

* The following list of ordered pairs defines the error in
  an approximation of some algorithim. Determine if the approximation converges using a least squares approach.
  It would be a good idea to plot the data to get a feel
  for the behavior of the data set. You can use Matplotlib
  for the plot.

* Use linear regression to determine the rate of
  convergence. You will need to write a code that
  computes the least squares fit to the given data.

**The data:**

  (.05,         0.72736334),
  (.025,        0.51876322),
  (.0125,       0.36998741),
  (.00625,      0.26387894),
  (.003125,     0.18820125),
  (.0015625,    0.13422712),
  (.00078125,   0.09573220),
  (.000390625,  0.06827721),
  (.0001953125, 0.04869603)

* Write a few sentances to summarize what you learned in
  this module.
