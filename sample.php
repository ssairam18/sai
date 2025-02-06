<?php
// Simple PHP example

// Variables
$greeting = "Hello, World!";
$name = "PHP User";
$count = 3;

// Output basic greeting
echo "<h1>" . $greeting . "</h1>";

// Display personalized message
echo "<p>Welcome to PHP programming, " . $name . "!</p>";

// Simple loop example
echo "<p>Counting to " . $count . ":</p>";
for ($i = 1; $i <= $count; $i++) {
    echo "<p>" . $i . "</p>";
}

// Closing PHP tag is optional when file contains only PHP code
?>
