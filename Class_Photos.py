def classPhotos(redShirtHeights, blueShirtHeights):
    
    redShirtHeights.sort()
    blueShirtHeights.sort()
    
    if redShirtHeights[0] > blueShirtHeights[0]:
        for r, b in zip(redShirtHeights, blueShirtHeights):
            if r < b:
                return False
        return True
    elif redShirtHeights[0] < blueShirtHeights[0]:
        for r, b in zip(redShirtHeights, blueShirtHeights):
            if r > b:
                return False
    else:
        return False
    return True
