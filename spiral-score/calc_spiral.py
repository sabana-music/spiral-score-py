from math import pi, cos, sin, log2

def calc_spiral_pos(freq, f0, distance_func):
    """Calculates the corresponding 2D-coordinate of the given frequencies
    Any wave can be represented as a series of sinusoidal waves with different frequencies.
    Each component sinusoidal wave is called a `note` in a spiral score.
    A note with frequency `f` is represented as a point in a plane.
    Using polar coordinate system, its position is determined as

        r = distance_func(f)
        θ = π/2 - 2πlog_2(f/f0)
        f0 must satisfy distance_func(f0) = 1.
        A note with frequency f0 lies in the 12 o'clock direction.
        If f0 has the frequency of C1, then every C note is placed in a half line heading to 12 o'clock direction. 

    For instance, if we set up distance function as

        distance_function(f) = f0/f

    Given two notes an octave apart, the note with higher frequency is two times closer to the origin then the other. 

    Args:
        freq: Single frequency or a list of frequencies
        distance_func: A function that takes frequency value and returns the distance
        from the origin to the corresponding position of the vertex in the range of (0, 1]

    Returns:
        returns a tuple (or list of tuples) of 2D-coordinate coresponding to the given frequency.
    """

    multi_freqs = True
    if type(freq) == float or type(freq) == int:
        freq = [freq]
        multi_freqs = False

    points = []
    for f in freq:
        r = distance_func(f)
        theta = pi/2 - 2*pi*log2(f/f0)
        points.append((r*cos(theta), r*sin(theta)))

    if multi_freqs:
        return points
    else:
        return points[0]

def create_rational(f0):
    """
    Create a `rational` distance function.
    Given two notes an octave apart, the note with higher frequency is two times closer to the origin then the other.
    """
    return lambda f: f0/f

def create_linear(f0, f_end):
    """
    Create a `linear` distance function.
    Given two notes an octave apart, the distance between two notes is always the same.
    When f = f_end, the return value of this function is f0/f_end and it is same with the result of `rational(f_end)`.
    """
    return lambda f: 1 - (f-f0)/f_end

def create_rational_linear_comb(f0, f_end, lin):
    """
    Create Combination of `rational` and `linear` function
    """
    linear = create_linear(f0, f_end)
    rational = create_rational(f0)
    return lambda f: lin * linear(f) + (1 - lin) * rational(f)


if __name__ == "__main__":
    f0 = 100
    pos = calc_spiral_pos(200, f0, create_rational(f0))
    print(pos)
