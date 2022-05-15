from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                          + self.coefficients[1:])

        elif isinstance(other, Polynomial):
            # Work out how many coefficient places the two polynomials have in
            # common.
            common = min(self.degree(), other.degree()) + 1
            # Sum the common coefficient positions.
            coefs = tuple(a - b for a, b in zip(self.coefficients[:common],
                                                other.coefficients[:common]))

            # Append the high degree coefficients from the higher degree
            # summand.
            coefs += self.coefficients[common:] + tuple(-c for c in other.coefficients[common:])

            return Polynomial(coefs)

        else:
            return NotImplemented

    def __rsub__(self, other): 
        return other - self

    def __mul__(self, other):
        if isinstance(other, Number):
            return Polynomial(tuple(other*n for n in self.coefficients))
        
        elif isinstance(other, Polynomial):

            entries = self.degree() + other.degree() + 1

            coefs = [0 for n in range (entries)]

            for m in range (self.degree()+1):
                for n in range (other.degree()+1):
                    coefs[m+n] += self.coefficients[m]*other.coefficients[n]
        
            coefs_tuple=tuple(coefs)

            return Polynomial(coefs_tuple)
        
        else:
            return NotImplemented


    def __rmul__(self, other):
        return self*other

    def __pow__(self, other):

        if isinstance(other, Integral):
            product=1
            for n in range (other):
                product = product*self
        
            return product
        
        else:
            return NotImplemented
    

    def __call__(self, other):

        if isinstance(other, Number):
            outcome=self.coefficients[0]
            for n in range (1, self.degree()+1):
                outcome+= self.coefficients[n]*(other**n)
            
            return outcome
        
        else:
            return NotImplemented

    
    def dx(self):

        coef=[]

        if self.degree()==0:
            coef=[0]
            coef_tuple=tuple(coef)
            

        else:
            for n in range (1, self.degree()):
                coef.append ((n+1)*self.coefficients[n+1])
                coef_tuple=tuple(coef)
        
        return Polynomial(coef_tuple)

def derivative(p):
    return p.dx()
