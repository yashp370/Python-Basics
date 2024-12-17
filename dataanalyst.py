{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": "the python\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "x,y,z = 5 ,6,7\nprint(x)\nprint(y)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "5\n6\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 3
    },
    {
      "cell_type": "markdown",
      "source": "#(DATATypes) (operators)\n\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": " c = 5\nprint(type(c))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "<class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 16
    },
    {
      "cell_type": "code",
      "source": "c = 5.3\nprint(c)\nprint(type(c))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "5.3\n<class 'float'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 17
    },
    {
      "cell_type": "code",
      "source": "x = 2+9j\nprint(x)\nprint(type(x))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "(2+9j)\n<class 'complex'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 18
    },
    {
      "cell_type": "code",
      "source": "a = \"the python\"\nprint(a)\nprint(type(a))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "the python\n<class 'str'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 19
    },
    {
      "cell_type": "code",
      "source": "b = [1,2,3,4,5,6,7,8,9,10]\nprint(b)\nprint(type(b))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n<class 'list'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 20
    },
    {
      "cell_type": "code",
      "source": "c = (1,2,3,4,5,6,7,8,9,10)\nprint(c)\nprint(type(c))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)\n<class 'tuple'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 21
    },
    {
      "cell_type": "code",
      "source": "%whos",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Variable   Type       Data/Info\n-------------------------------\na          str        the python\nb          list       n=10\nc          tuple      n=10\nx          complex    (2+9j)\ny          int        6\nz          int        7\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 22
    },
    {
      "cell_type": "markdown",
      "source": "operators -\n\n1=\n2=\n3=\n4=\n5=\n6=\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#1= add operations\na = 5 \nb = 9\nprint(a+b)\nprint(type(a+b))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "14\n<class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 24
    },
    {
      "cell_type": "code",
      "source": "a = 5 \nb = 9.6\nprint(a+b)\nprint(type(a+b))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "14.6\n<class 'float'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 25
    },
    {
      "cell_type": "code",
      "source": "a =  5+2j\nb = 2\nprint(a+b)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "(7+2j)\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 26
    },
    {
      "cell_type": "code",
      "source": "a = \"hello\"\nb = \" students\"\nprint(a + b)\nprint(type(a+b))\n\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "hello students\n<class 'str'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 30
    },
    {
      "cell_type": "code",
      "source": "#for space in a and b \na = \"hello\"\nb = \" students\"\nprint(a + \" \" +  b)\nprint(type(a+b))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "hello  students\n<class 'str'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 32
    },
    {
      "cell_type": "code",
      "source": "# subtraction\na = 688\nb = 99\nprint(a-b)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "589\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 33
    },
    {
      "cell_type": "code",
      "source": "a = 688\nb = 99\nprint(a-b)\nprint(type(a+b))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "589\n<class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 34
    },
    {
      "cell_type": "code",
      "source": "a = 688\nb = 99.33\nprint(a-b)\nprint(type(a+b))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "588.67\n<class 'float'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 35
    },
    {
      "cell_type": "code",
      "source": "#for complex\na = 5-1j\nb = 3\nprint(a-b)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "(2-1j)\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 36
    },
    {
      "cell_type": "code",
      "source": "# mutiplication\na = 5\nb = 9\nprint(a * b)\nprint(type(a*b))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "45\n<class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 37
    },
    {
      "cell_type": "code",
      "source": "a = 5\nb = 9.66\nprint(a * b)\nprint(type(a*b))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "48.3\n<class 'float'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 38
    },
    {
      "cell_type": "code",
      "source": "# division\na =9 \nb = 10\nprint(a/b)\nprint(type(a/b))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "0.9\n<class 'float'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 39
    },
    {
      "cell_type": "code",
      "source": "# modulous\n\na = 19\nb = 3\nprint(a % b)\nprint(type(a%b))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "1\n<class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 41
    },
    {
      "cell_type": "code",
      "source": "a = 12\nb = 4 \nprint(a % b)\nprint(type(a%b))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "0\n<class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 42
    },
    {
      "cell_type": "code",
      "source": "# Exponent , \n# it is use for the power like = 2 the power of 4 = 16\na = 41256789\nprint(a**55)\nprint(type(a))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "71162028433520217717099884851404495326786614148274137562533191244754226421072922193229393035406290047490322006127486170528820460414671897074184746917638236810663780872933871199771053029074871072046645088603300420278272474373361352870797685329285463690039885441075398107839063255747535400015566353549647882767414182717586010912021318113386679928289227315380064286145450539958069165193638416244911434618495833200180049949\n<class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 46
    },
    {
      "cell_type": "code",
      "source": "a = ((859*78) + (78.256/89) + (856**67)  +  (145698 - 78526) )\nprint(a)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "2.990489165920469e+196\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 47
    },
    {
      "cell_type": "code",
      "source": "#bolien\na =True\nb = False\nprint(a and b)\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "False\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 49
    },
    {
      "cell_type": "code",
      "source": "a =True\nb = False\nprint(a or b)\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "True\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 50
    },
    {
      "cell_type": "code",
      "source": "a =True\nb = False\nprint(not(a))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "False\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 54
    },
    {
      "cell_type": "markdown",
      "source": "types of python function",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# built in function\n# abs() function  =  (absolute)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 55
    },
    {
      "cell_type": "code",
      "source": "x = abs(-7.25)\nprint(x)\nprint(type(x))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "7.25\n<class 'float'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 57
    },
    {
      "cell_type": "code",
      "source": "x = abs(-7)\nprint(x)\nprint(type(x))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "7\n<class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 58
    },
    {
      "cell_type": "code",
      "source": "z =abs(3+5j)\nprint(z)\nprint(type(z))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "5.830951894845301\n<class 'float'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 60
    },
    {
      "cell_type": "code",
      "source": "# binary function\n\nx= bin(13)\nprint(x)\nprint(type(x))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "0b1101\n<class 'str'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 63
    },
    {
      "cell_type": "code",
      "source": "x= bin(36)\nprint(x)\nprint(type(x))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "0b100100\n<class 'str'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 62
    },
    {
      "cell_type": "code",
      "source": "z = 56\nprint(bin(z))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "0b111000\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 64
    },
    {
      "cell_type": "code",
      "source": "# bytes function\n\nx = bytes(4)\nprint(x)\nprint(type(x))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "b'\\x00\\x00\\x00\\x00'\n<class 'bytes'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 66
    },
    {
      "cell_type": "code",
      "source": "x = bytes(16)\nprint(x)\nprint(type(x))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "b'\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00'\n<class 'bytes'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 67
    },
    {
      "cell_type": "code",
      "source": "x = 4\nprint(bytes(x))\nprint(type(x))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "b'\\x00\\x00\\x00\\x00'\n<class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 68
    },
    {
      "cell_type": "code",
      "source": "# chr() function\n\nx = chr(97)\nprint(x)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "a\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 73
    },
    {
      "cell_type": "code",
      "source": "x = chr(98)\nprint(x)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "b\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 74
    },
    {
      "cell_type": "code",
      "source": "x = chr(91)\nprint(x)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "[\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 82
    },
    {
      "cell_type": "code",
      "source": "# complex() function\n\nx= complex(3,5)\nprint(x)\nprint(type(x))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "(3+5j)\n<class 'complex'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 86
    },
    {
      "cell_type": "code",
      "source": "x= complex(3,5.6)\nprint(x)\nprint(type(x))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "(3+5.6j)\n<class 'complex'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 87
    },
    {
      "cell_type": "code",
      "source": "x= 3,5\nprint(complex(3,5))\nprint(type(x))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "(3+5j)\n<class 'tuple'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 91
    },
    {
      "cell_type": "code",
      "source": "x= complex(3)\nprint(x)\nprint(type(x))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "(3+0j)\n<class 'complex'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 92
    },
    {
      "cell_type": "code",
      "source": "#float() function\n\nx = float(3)\nprint(x)\nprint(type(x))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "3.0\n<class 'float'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 93
    },
    {
      "cell_type": "code",
      "source": "x = float(3.65)\nprint(x)\nprint(type(x))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "3.65\n<class 'float'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 94
    },
    {
      "cell_type": "code",
      "source": "# int() function\nx = int(500)\nprint(x)\nprint(type(x))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "500\n<class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 99
    },
    {
      "cell_type": "code",
      "source": "x = int(500.36)\nprint(x)\nprint(type(x))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "500\n<class 'int'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 100
    },
    {
      "cell_type": "code",
      "source": "# str() function\n\na = str(2563)\nprint(a)\nprint(type(a))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "2563\n<class 'str'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 103
    },
    {
      "cell_type": "code",
      "source": "a = str(\"2563\")\nprint(a)\nprint(type(a))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "2563\n<class 'str'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 104
    },
    {
      "cell_type": "code",
      "source": "a = str(2563.3)\nprint(a)\nprint(type(a))\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "2563.3\n<class 'str'>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 105
    },
    {
      "cell_type": "code",
      "source": "#help () function",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": "help (float)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Help on class float in module builtins:\n\nclass float(object)\n |  float(x=0, /)\n |\n |  Convert a string or number to a floating point number, if possible.\n |\n |  Methods defined here:\n |\n |  __abs__(self, /)\n |      abs(self)\n |\n |  __add__(self, value, /)\n |      Return self+value.\n |\n |  __bool__(self, /)\n |      True if self else False\n |\n |  __ceil__(self, /)\n |      Return the ceiling as an Integral.\n |\n |  __divmod__(self, value, /)\n |      Return divmod(self, value).\n |\n |  __eq__(self, value, /)\n |      Return self==value.\n |\n |  __float__(self, /)\n |      float(self)\n |\n |  __floor__(self, /)\n |      Return the floor as an Integral.\n |\n |  __floordiv__(self, value, /)\n |      Return self//value.\n |\n |  __format__(self, format_spec, /)\n |      Formats the float according to format_spec.\n |\n |  __ge__(self, value, /)\n |      Return self>=value.\n |\n |  __getattribute__(self, name, /)\n |      Return getattr(self, name).\n |\n |  __getnewargs__(self, /)\n |\n |  __gt__(self, value, /)\n |      Return self>value.\n |\n |  __hash__(self, /)\n |      Return hash(self).\n |\n |  __int__(self, /)\n |      int(self)\n |\n |  __le__(self, value, /)\n |      Return self<=value.\n |\n |  __lt__(self, value, /)\n |      Return self<value.\n |\n |  __mod__(self, value, /)\n |      Return self%value.\n |\n |  __mul__(self, value, /)\n |      Return self*value.\n |\n |  __ne__(self, value, /)\n |      Return self!=value.\n |\n |  __neg__(self, /)\n |      -self\n |\n |  __pos__(self, /)\n |      +self\n |\n |  __pow__(self, value, mod=None, /)\n |      Return pow(self, value, mod).\n |\n |  __radd__(self, value, /)\n |      Return value+self.\n |\n |  __rdivmod__(self, value, /)\n |      Return divmod(value, self).\n |\n |  __repr__(self, /)\n |      Return repr(self).\n |\n |  __rfloordiv__(self, value, /)\n |      Return value//self.\n |\n |  __rmod__(self, value, /)\n |      Return value%self.\n |\n |  __rmul__(self, value, /)\n |      Return value*self.\n |\n |  __round__(self, ndigits=None, /)\n |      Return the Integral closest to x, rounding half toward even.\n |\n |      When an argument is passed, work like built-in round(x, ndigits).\n |\n |  __rpow__(self, value, mod=None, /)\n |      Return pow(value, self, mod).\n |\n |  __rsub__(self, value, /)\n |      Return value-self.\n |\n |  __rtruediv__(self, value, /)\n |      Return value/self.\n |\n |  __sub__(self, value, /)\n |      Return self-value.\n |\n |  __truediv__(self, value, /)\n |      Return self/value.\n |\n |  __trunc__(self, /)\n |      Return the Integral closest to x between 0 and x.\n |\n |  as_integer_ratio(self, /)\n |      Return a pair of integers, whose ratio is exactly equal to the original float.\n |\n |      The ratio is in lowest terms and has a positive denominator.  Raise\n |      OverflowError on infinities and a ValueError on NaNs.\n |\n |      >>> (10.0).as_integer_ratio()\n |      (10, 1)\n |      >>> (0.0).as_integer_ratio()\n |      (0, 1)\n |      >>> (-.25).as_integer_ratio()\n |      (-1, 4)\n |\n |  conjugate(self, /)\n |      Return self, the complex conjugate of any float.\n |\n |  hex(self, /)\n |      Return a hexadecimal representation of a floating-point number.\n |\n |      >>> (-0.1).hex()\n |      '-0x1.999999999999ap-4'\n |      >>> 3.14159.hex()\n |      '0x1.921f9f01b866ep+1'\n |\n |  is_integer(self, /)\n |      Return True if the float is an integer.\n |\n |  ----------------------------------------------------------------------\n |  Class methods defined here:\n |\n |  __getformat__(typestr, /) from builtins.type\n |      You probably don't want to use this function.\n |\n |        typestr\n |          Must be 'double' or 'float'.\n |\n |      It exists mainly to be used in Python's test suite.\n |\n |      This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,\n |      little-endian' best describes the format of floating point numbers used by the\n |      C type named by typestr.\n |\n |  fromhex(string, /) from builtins.type\n |      Create a floating-point number from a hexadecimal string.\n |\n |      >>> float.fromhex('0x1.ffffp10')\n |      2047.984375\n |      >>> float.fromhex('-0x1p-1074')\n |      -5e-324\n |\n |  ----------------------------------------------------------------------\n |  Static methods defined here:\n |\n |  __new__(*args, **kwargs) from builtins.type\n |      Create and return a new object.  See help(type) for accurate signature.\n |\n |  ----------------------------------------------------------------------\n |  Data descriptors defined here:\n |\n |  imag\n |      the imaginary part of a complex number\n |\n |  real\n |      the real part of a complex number\n\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 107
    },
    {
      "cell_type": "code",
      "source": "#input sunction\n\na  = input(\"enter your name\")\nprint(\"hello\",a)\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "hello <PyodideFuture pending cb=[WebLoop._decrement_in_progress()]>\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 112
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}