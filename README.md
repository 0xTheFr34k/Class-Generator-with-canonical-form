## Simple Class Generator with orthodox canonical form

# Setup as alias :

```bash

git clode https://github.com/BleedTheFreak/Class-Generator-with-canonical-form ~/Class-Generator

```

```bash

echo "alias class='python3 ~/Class-Generator/GeneratClass.py'" >> ~/.zshrc

```

```bash

source ~/.zshrc

```

Now you can use it as command in terminal

```bash
class Fixed
```

You will got something like this

# Fixed.hpp

```c++

#ifndef FIXED_CLASS
#define FIXED_CLASS

#include <iostream>

class Fixed
{
public:
	Fixed();
	~Fixed();
	Fixed(const Fixed &f);
	Fixed & operator =(const Fixed &f);
private: 

}; 

#endif // !FIXED_CLASS 

```

# Fixed.cpp

```c++

#include "Fixed.hpp"

Fixed::Fixed(){
	std::cout << "Default constructor called" << std::endl;
} 

Fixed::~Fixed(){
	std::cout << "Destructor called" << std::endl;
} 

Fixed::Fixed(const Fixed &f){
	std::cout << "Copy constructor called" << std::endl;
	 *this = f;
} 

Fixed & Fixed::operator =(const Fixed &f){
	std::cout << "Copy assignment operator called" << std::endl;
	if(this != &f)
	{ 
	} 
	return *this;
} 

```
