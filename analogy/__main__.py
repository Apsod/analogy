import argparse
import json
from importlib import import_module
from analogy.test import evaluate_all
from analogy.parse import parse_txt


def read_test(arg):
    def inner(prep):
        txt = argparse.FileType('r')(arg).read()
        return parse_txt(txt, prep)
    return inner


def read_wrapper(arg):
    path = arg.split('.')
    mm = import_module('.'.join(path[:-1]))
    wrapper = getattr(mm, path[-1])
    return wrapper


def __main__():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--lower',
        action='store_true'
    )

    parser.add_argument(
        '--test',
        type=read_test,
        required=True)

    parser.add_argument(
        '--wrapper',
        type=read_wrapper,
        required=True)

    parser.add_argument(
        '--model',
        type=str,
        required=True)

    parser.add_argument(
        '--out',
        type=argparse.FileType('w'),
        default=argparse.FileType('w')('-'))

    args = parser.parse_args()

    def normalize(w):
        r = w
        if args.lower:
            r = r.lower()
        return r

    test = args.test(normalize)
    model = args.wrapper.load(args.model)
    result = evaluate_all(test, model, normalize)
    json.dump(result, args.out)


