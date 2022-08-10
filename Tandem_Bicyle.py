def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)

    return sum([max(b,r) for b,r in zip(redShirtSpeeds, blueShirtSpeeds)])
