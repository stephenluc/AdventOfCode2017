<?hh

$input = '19_input.txt';

$route = new Vector(null);
if ($f = fopen($input, 'r')) {
    while(!feof($f)) {
        $route->add(fgets($f));
    }
    fclose($f);
}

function a_series_of_tubes(Vector $route): void {
	$seen_letters = new Vector(null);
	$curr_x = 1;
	$curr_y = 0;
	
	$horizontal = 0;
	$vertical = 1;

	$steps = 0;

	while (substr($route->get($curr_y), $curr_x , 1) !== " ") {

		if (substr($route->get($curr_y), $curr_x, 1) == '+') {
			if ($horizontal == 0) {
				$horizontal = (substr($route->get($curr_y), $curr_x + 1, 1) !== " " ? 1 : -1);
				$vertical = 0;
			} else {
				$vertical = (substr($route->get($curr_y + 1), $curr_x, 1) !== " " ? 1 : -1);
				$horizontal = 0;
			}
		} elseif (ctype_alpha(substr($route->get($curr_y), $curr_x , 1))) {
			$seen_letters->add(substr($route->get($curr_y), $curr_x , 1));
		}

		$curr_x += $horizontal;
		$curr_y += $vertical;
		$steps += 1;
	}

	$joined = '';
	foreach ($seen_letters as $letter) {
		$joined .= $letter;
	}
	echo "Part 1: " . $joined . "\n";
	echo "Part 2: " . $steps  . "\n";
}

a_series_of_tubes($route);