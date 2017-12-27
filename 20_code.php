<?hh

$input = '20_input.txt';

$swarm = new Map(null);
$remove = array("p", "v", "a", "<", ">", "=", " ");
if ($f = fopen($input, 'r')) {
	$i = 0;
    while(!feof($f)) {
		$deleted = str_replace($remove, "", fgets($f));
		$split = explode(",", $deleted);
    	$position = Map {
    		'x' => (int)$split[0],
    		'y' => (int)$split[1],
    		'z' => (int)$split[2],
    	};
    	$velocity = Map {
    		'x' => (int)$split[3],
    		'y' => (int)$split[4],
    		'z' => (int)$split[5],
    	};
    	$acceleration = Map {
    		'x' => (int)$split[6],
    		'y' => (int)$split[7],
    		'z' => (int)$split[8],
    	};
    	$location = Map {
    		'p' => $position,
    		'v' => $velocity,
    		'a' => $acceleration,
    	};
        $swarm[$i] = ($location);
        $i++;
    }
    fclose($f);
}

function particale_swarm(Map $swarm): void {
	for ($x = 0; $x <= 1000; $x++) {
		foreach ($swarm as $particale) {
			$particale['v']['x'] += $particale['a']['x'];
			$particale['v']['y'] += $particale['a']['y'];
			$particale['v']['z'] += $particale['a']['z'];
			$particale['p']['x'] += $particale['v']['x'];
			$particale['p']['y'] += $particale['v']['y'];
			$particale['p']['z'] += $particale['v']['z'];
		}
	}
	$min_index = 0;
	$min_distance = PHP_INT_MAX;
	foreach ($swarm as $key => $particale) {
		$manhattan_distance = abs($particale['p']['x']) + abs($particale['p']['y']) + abs($particale['p']['z']);
		if ($min_distance > $manhattan_distance) {
			$min_index = $key;
			$min_distance = $manhattan_distance;
		}
	}
	echo "Part 1: " . $min_index . "\n";

}

function part_2(Map $swarm): void {
	for ($x = 0; $x <= 1000; $x++) {
		$positions = new Map(null);
		foreach ($swarm as $key => $particale) {
			$particale['v']['x'] += $particale['a']['x'];
			$particale['v']['y'] += $particale['a']['y'];
			$particale['v']['z'] += $particale['a']['z'];
			$particale['p']['x'] += $particale['v']['x'];
			$particale['p']['y'] += $particale['v']['y'];
			$particale['p']['z'] += $particale['v']['z'];

			$curr_position = $particale['p']['x'] . $particale['p']['y'] . $particale['p']['z'];
			if (!$positions->containsKey($curr_position)) {
				$positions[$curr_position] = new Vector(null);
			}
			$positions[$curr_position]->add($key);
		}

		foreach ($positions as $key => $particales) {
			if ($particales->count() > 1) {
				foreach ($particales as $key => $index) {
					$swarm->removeKey($index);
				}
			}
		}

	}
	echo "Part 2: " . $swarm->count() . "\n";

}

# particale_swarm($swarm);
# part_2($swarm);
