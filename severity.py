import random
polarity=random.choice("gbn")
severity=random.choice("lmh")
if polarity=="g":
    polarity=1
elif polarity=="b":
    polarity=0
elif polarity=="n":
    polarity=2
else:
    polarity="smth went wrong"
if severity=="m":
    severity=1
elif severity=="l":
    severity=0
elif severity=="h":
    severity=2
else:
    polarity="smth went wrong"
