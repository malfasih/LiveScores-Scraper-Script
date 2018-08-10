<?php
ob_start();
passthru('python3 livescores.py --json');
$output = ob_get_clean(); 

$output = json_decode($output);

$matches = array();

foreach($output as $match)
{
	$scores = explode('-', str_replace(" ", "", $match->result));

	$time = str_replace(" ", "", trim($match->hours));

	$home_score = trim($scores[0]);
	$away_score = trim($scores[1]);

	$matches[] = array('time' => $time, 'home' => trim($match->team1), 'away' => trim($match->team2), 'home_score' => $home_score, 'away_score' => $away_score);
}

print_r($matches);
?>
