#!/usr/bin/perl
#replace.pl

use warnings;
use strict;

while(<>){

 $_ =~ s/[bB][oO][oO][kK]/book/;
 print $_;
}
