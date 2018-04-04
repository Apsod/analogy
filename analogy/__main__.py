import argparse
import json
from importlib import import_module
from analogy.test import evaluate_all, run_all
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
    parser = argparse.ArgumentParser(description='Evaluate a language model against google analogy tasks')

    parser.add_argument(
        '--lower',
        action='store_true',
        help='If present, test words are lowercased before being sent to the model',
    )

    parser.add_argument(
        '--run',
        action='store_true',
        help='If present, output all predictions and queries, not just aggregate results',
    )

    parser.add_argument(
        '--test',
        type=read_test,
        required=True,
        help='Path to analogy test set. Should take the form: ": category <newline> A B X Y <newline> ... "'
        )

    parser.add_argument(
        '--wrapper',
        type=read_wrapper,
        required=True,
        help='Python import path to the wrapper class, should implement the functions "load", "members", and "analogies"'
        )

    parser.add_argument(
        '--model',
        type=str,
        required=True,
        help='Model path'
        )

    parser.add_argument(
        '--out',
        type=argparse.FileType('w'),
        default=argparse.FileType('w')('-'),
        help='Output path, default: stdout'
        )

    args = parser.parse_args()

    if args.lower:
        def normalize(w):
            return w.lower()
    else:
        def normalize(w):
            return w

    test = args.test(normalize)
    model = args.wrapper.load(args.model)
    if args.run:
        result = run_all(test, model, normalize)
    else: 
        result = evaluate_all(test, model, normalize)
    json.dump(result, args.out)

