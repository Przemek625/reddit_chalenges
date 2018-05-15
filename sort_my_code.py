INPUT_DATA1 = \
"""
  std::cout << "Hello world!" << std::endl;
}
#include <iostream>
int main () {
"""

INPUT_DATA2 = \
"""
    sum = i + sum;
  {
  }
  int sum = 0
  for (int i = 0; i <= 100; ++i)
  std::cout << sum;
  return 0;
{
}
#include <iostream>
int main()
"""

INPUT_DATA3 = \
"""
Input
        sum += f(x);
    {
    }
    return ( 1.0 / ( y * y) );
    unsigned int start = 1;
    unsigned int end = 1000;
    double sum = 0;
    for( unsigned int x = start; x <= end; ++x )
    std::cout << "Sum of f(x) from " << start << " to " << end << " is " << sum << std::endl;
    return 0;
{
{
}
}
#include <iostream>
double f(double y)
int main()
"""

if __name__ == '__main__':
    pass
