# analogy
Lightweight google analogy test evaluation

Standard usage: 

```
> eval-analogy agg --test path/to/test --wrapper import.path.to.wrapper --model path/to/model
```

Which results in json output like the following: 

```
{
  "city-in-state": {
    "Incorrect": 157,
    "NA": 12,
    "Correct": 6
  },
  "capital-common-countries": {
    "Incorrect": 258,
    "NA": 234,
    "Correct": 14
  },
  "family": {
    "Incorrect": 128,
    "NA": 32,
    "Correct": 112
  }
}
```

The test data should be a text file of the following form:
```
# Comment
: Category 1
Stockholm Sweden Paris London
...
```

The wrapper class needs to implement a static load function, batched analogy answering, and batched word membership.

To aggregate the results in one coverage/accuracy-score, use the supplied aggregate.jq script like so: 
```
jq -sf aggregate.jq agg
```
