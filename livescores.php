<?php
ob_start();
passthru('python3 livescores.py --json');
$output = ob_get_clean(); 

$output = json_decode($output);

print_r($output);
?>
