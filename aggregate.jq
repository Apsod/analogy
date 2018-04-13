def aggregate_all: .[] | map(.) | reduce .[] as $item ({NA:0, Correct:0, Incorrect:0}; .NA += $item.NA | .Correct += $item.Correct | .Incorrect += $item.Incorrect);

def coverage: (.Correct + .Incorrect) / (.NA + .Correct + .Incorrect);

def accuracy: .Correct / (.Correct + .Incorrect);

def metrics: . | {coverage: . | coverage, accuracy: . | accuracy};

{
  aggregate: aggregate_all | metrics,
  total: .[] | map_values(metrics)
}
