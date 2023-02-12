from luatypes import *

class Vector:
  pass
class Vector:
  def add(self, o:Vector)->Vector:
    """
    Adds two vectors together.

    :param o: The second vector to add.
    :returns: The resulting vector
    """
    pass
  def sub(self, o:Vector)->Vector:
    """
    Subtracts one vector from another.

    :param o: The vector to subtract.
    :returns: The resulting vector
    """
    pass

  def mul(self, m:number)->Vector:
    """
    Multiplies a vector by a scalar value.

    :param m: The scalar value to multiply with.
    :returns: A vector with value (x * m, y * m, z * m).
    """
    pass

  def div(self, m:number)->Vector:
    """
    Divides a vector by a scalar value.

    :param m: The scalar value to divide by.
    :returns: A vector with value (x / m, y / m, z / m).
    """
    pass

  def unm(self)->Vector:
    """
    Negate a vector

    :returns: The negated vector.
    """
    pass

  def dot(self, o:Vector)->Vector:
    """
    Compute the dot product of two vectors

    :param o: The second vector to compute the dot product of.
    :returns: The dot product of self and o.
    """
    pass

  def cross(self, o:Vector)->Vector:
    """
    Compute the cross product of two vectors

    :param o: The second vector to compute the cross product of.
    :returns: The cross product of self and o.
    """
    pass

  def length(self)->number:
    """
    Get the length (also referred to as magnitude) of this vector.

    :returns: The length of this vector.
    """
    pass

  def normalize(self)->Vector:
    """
    Divide this vector by its length, producing with the same direction, butof length 1.

    :returns: The normalised vector
    """
    pass

  def round(self, tolerance:number=1)->Vector:
    """
    Construct a vector with each dimension rounded to the nearest value.

    :param tolerance: The tolerance that we should round to, defaulting to 1. For instance, a tolerance of 0.5 will round to the nearest 0.5.
    :returns: The rounded vector.
    """
    pass

  def tostring(self)->string:
    """
    Convert this vector into a string, for pretty printing.

    :returns: This vector's  representation.
    """
    pass

  def equals(self, other:Vector)->boolean:
    """
    Check for equality between two vectors.

    :param other: The second vector to compare to.
    :returns: Whether or not the vectors are equal.
    """
    pass

class vector:
  @staticmethod
  def new(x:number, y:number, z:number)->Vector:
    """
    Construct a new Vector with the given coordinates.

    :param x: The X coordinate or direction of the vector.
    :param y: The Y coordinate or direction of the vector.
    :param z: The Z coordinate or direction of the vector.
    :returns: The constructed vector.
    """
    pass