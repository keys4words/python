def area_of_circle(radius):
    return 3.14*radius**2


def area_of_disc(outer, inner):
    '''
    Return area of disk
    :param outer: outer radius
    :param inner: inner radius
    :return: area
    '''
    return area_of_circle(outer)-area_of_circle(inner)