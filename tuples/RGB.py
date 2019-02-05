def yiq(RGB):
    y = 0.299 * RGB[0] + 0.587 * RGB[1] + 0.114 * RGB[2]
    i = 0.596 * RGB[0] + (-0.274) * RGB[1] + (-0.322) * RGB[2]
    q = 0.211 * RGB[0] + (-0.523) * RGB[1] + 0.312 * RGB[2]

    return y, i, q


