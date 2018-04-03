import argparse
import json
from analogy.test import evaluate_all
from analogy.parse import parse_txt


def read_test(arg):
    txt = argparse.FileType('r')(arg).read()
    return parse_txt(txt)


def read_wrapper(arg):
    path = arg.split('.')
    module = '.'.join(path[:-1])
    wrapper = getattr(module, path[-1])
    return wrapper


def __main__():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--test',
        type=read_test,
        default=read_test('-'))

    parser.add_argument(
        '--wrapper',
        type=read_wrapper,
        required=True)

    parser.add_argument(
        '--model',
        type=argparse.FileType('rb'),
        required=True)

    parser.add_argument(
        '--out',
        type=argparse.FileType('w'),
        default=argparse.FileType('w')('-'))

    args = parser.parse_args()
    model = args.wrapper.load(args.model)
    result = evaluate_all(args.test, model)
    json.dump(result, args.out)


