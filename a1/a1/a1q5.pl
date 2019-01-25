#!/usr/bin/perl

print "Enter a positive integer: ";
$input_number = <>;
chomp($input_number);

$char_X = "X";
$blank_char = " ";

if ($input_number >= 1 ){
	print $char_X x $input_number, "\n";
	if ($input_number >= 2){
		$temp_number = $input_number - 2;
		for my $i (0..$temp_number - 1) {
		  print $char_X, $blank_char x $temp_number , $char_X,"\n";}
		print $char_X x $input_number, , "\n";}
}
else{
	print "Please enter valid positive integer from 1\n";}
