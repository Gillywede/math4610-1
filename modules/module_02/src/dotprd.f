      function subroutine dotprd(u, v, n)
      real*8 u

      real*8 sum

      sum = 0.0
      do 1 i=1,n
         sum = sum + u(i) * v(i)
    1 enddo

      return sum
    