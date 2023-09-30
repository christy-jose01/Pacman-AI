"""
Analysis question.
Change these default values to obtain the specified policies through value iteration.
If any question is not possible, return just the constant NOT_POSSIBLE:
```
return NOT_POSSIBLE
```
"""

NOT_POSSIBLE = None


def question2():
    """
    [Enter a description of what you did here.]
    I periodically reduced the noise until the agent crossed the bridge
    """

    answerDiscount = 0.9
    answerNoise = 0.01

    return answerDiscount, answerNoise


def question3a():
    """
    [Enter a description of what you did here.
    I reduced the noise even lower to increase the risk]
    """

    answerDiscount = 0.09
    answerNoise = 0.001
    answerLivingReward = 0.0

    return answerDiscount, answerNoise, answerLivingReward


def question3b():
    """
    [Enter a description of what you did here.
    I reduced the noise and discount]
    """

    answerDiscount = 0.09
    answerNoise = 0.01
    answerLivingReward = 0.0

    return answerDiscount, answerNoise, answerLivingReward


def question3c():
    """
    [Enter a description of what you did here.
    I just significantly reduced one actor and noticed that it did this]
    """

    answerDiscount = 0.9
    answerNoise = 0.01
    answerLivingReward = 0.0

    return answerDiscount, answerNoise, answerLivingReward


def question3d():
    """
    [Enter a description of what you did here.
    Leaving it as default values answered this question]
    """

    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0.0

    return answerDiscount, answerNoise, answerLivingReward


def question3e():
    """
    [Enter a description of what you did here.
    I increased the living reward so that it avoids the exits]
    """

    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 1.0

    return answerDiscount, answerNoise, answerLivingReward


def question6():
    """
    [Enter a description of what you did here. I tried everything and it didn't work]
    """

    # answerEpsilon = None
    # answerLearningRate = None

    return NOT_POSSIBLE

    # return answerEpsilon, answerLearningRate


if __name__ == "__main__":
    questions = [
        question2,
        question3a,
        question3b,
        question3c,
        question3d,
        question3e,
        question6,
    ]

    print("Answers to analysis questions:")
    for question in questions:
        response = question()
        print("    Question %-10s:\t%s" % (question.__name__, str(response)))
