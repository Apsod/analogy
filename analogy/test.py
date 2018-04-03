from enum import Enum


class Result(Enum):
    Incorrect = 0
    Correct = 1
    NA = 2


def evaluate(examples, model, normalize):
    """
    Evaluate the model on all analogy examples given.
    :param examples: Analogy examples: [A:B::X:Y]
    :param model: Distributional semantic model with __contains__ and analogy defined
    :param normalize: Normalize query words and return words (i.e. lowercase, or ICU-normalize)
    :return: Aggregate of incorrect, correct, and N/A judgements.
    """
    ret = {k.name: 0 for k in Result}
    mask = [all(model.members(example)) for example in examples]

    examples = [example for flag, example in zip(mask, examples) if flag]

    (aa, bb, xx, yy) = zip(*examples)

    abx = zip(aa, bb, xx)
    ret[Result.NA.name] += sum([not m for m in mask])
    for y, ans in zip(yy, model.analogies(abx)):
        ret[Result(y == normalize(ans)).name] += 1
    return ret


def evaluate_all(eval_set, model, normalize):
    """
    Evaluate the model on all categories of analogy examples given.
    :param eval_set: Categories of analogy examples: {Category: [A:B::X:Y]}
    :param model: Distributional semantic model with __contains__ and analogy defined
    :param normalize: Normalize query words and return words (i.e. lowercase, or ICU-normalization)
    :return: Aggregate of incorrect, correct, and N/A judgements over categories
    """
    ret = {}
    for category, examples in eval_set.items():
        ret[category] = evaluate(examples, model, normalize)
    return ret
