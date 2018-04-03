from enum import Enum


class Result(Enum):
    Incorrect = 0
    Correct = 1
    NA = 2


def evaluate(examples, model):
    """
    Evaluate the model on all analogy examples given.
    :param examples: Analogy examples: [A:B::X:Y]
    :param model: Distributional semantic model with __contains__ and analogy defined
    :return: Aggregate of incorrect, correct, and N/A judgements.
    """
    ret = {k: 0 for k in Result}
    for example in examples:
        a, b, c, d = example
        if all(w in model for w in example):
            ret[Result(d == model.analogy(a, b, c))] += 1
        else:
            ret[Result.NA] += 1
    return ret


def evaluate_all(eval_set, model):
    """
    Evaluate the model on all categories of analogy examples given.
    :param eval_set: Categories of analogy examples: {Category: [A:B::X:Y]}
    :param model: Distributional semantic model with __contains__ and analogy defined
    :return: Aggregate of incorrect, correct, and N/A judgements over categories
    """
    ret = {}
    for category, examples in eval_set.items():
        ret[category] = evaluate(examples, model)
    return ret
