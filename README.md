It is (as far as I know) not possible to resize, blur, or do any other arithmetic on images in OpenCV.
This repoitiry provides the missing code needed: transformations from sRGB to linear and back. This
takes the gamma into account.

For an explanation and a lot more information about the problem, see
  * [What every coder should know about gamma](http://blog.johnnovak.net/2016/09/21/what-every-coder-should-know-about-gamma/)
  * [Gamma error in picture scaling](http://web.archive.org/web/20160301042052/http://www.4p8.com/eric.brasseur/gamma.html)

Code is available in C++ and Python.
