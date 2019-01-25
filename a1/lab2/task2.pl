#!/usr/bin/perl

sub conc {
 my ($a, $b) = @_;
 @string_conc = sort($a, $b);
 return $string_conc[0].$string_conc[1];

}

print &conc('aaa','ccc'); 
print "\n"; 
print &conc('ccc','aaa'); 
print "\n";
