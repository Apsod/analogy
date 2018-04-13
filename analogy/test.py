from enum import Enum
from analogy.util import chunk


class Result(Enum):
    Incorrect = 0
    Correct = 1
    NA = 2


def run(examples, model, chunksize=200):
    ret = []
    ans = []
    mask = [all(model.members(example)) for example in examples]

    valid_examples = [example for flag, example in zip(mask, examples) if flag]

    for batch in chunk(chunksize, valid_examples):
        (aa, bb, xx, _) = zip(*batch)
        abx = zip(aa, bb, xx)
        ans += model.analogies(abx)

    j = 0
    for i in range(len(examples)):
        if mask[i]:
            ret.append(ans[j])
            j += 1
        else:
            ret.append(None)
    return ret


def run_all(eval_set, model, normalize):
    ret = {}
    for category, examples in eval_set.items():
        pred = run(examples, model)
        for p, a, b, x, y in zip(pred, *zip(*examples)):
            ret[category].append({
                'query': [a, b, x],
                'correct': y,
                'prediction': p})
    return ret


def evaluate(examples, model, normalize, chunksize=200):
    """
    Evaluate the model on all analogy examples given.
    :param examples: Analogy examples: [A:B::X:Y]
    :param model: Distributional semantic model with __contains__ and analogy defined
    :param normalize: Normalize query words and return words (i.e. lowercase, or ICU-normalize)
    :return: Aggregate of incorrect, correct, and N/A judgements.
    """

    pred = run(examples, model, chunksize)

    ret = {k.name: 0 for k in Result}

    for p, a, b, x, y in zip(pred, *zip(*examples)):
        if p is None:
            ret[Result.NA.name] += 1
        else:
            ret[Result(y == normalize(p)).name] += 1

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
