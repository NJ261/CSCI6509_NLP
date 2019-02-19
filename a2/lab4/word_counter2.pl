#!/usr/bin/perl

my %words=();

while (my $line = <>)
{
    foreach my $word (split /\s+/, $line)
    {
        $words{lc($word)}++; 
    }
}

sub count_frequency{
   my $input_word = shift;
   my $word_ref = shift;

   if( exists($$word_ref{$input_word} ) ) {
     print "$word_ref->{$input_word}\n";
   }
   else {
      print "0\n";
   }	
}

count_frequency('sawyer', \%words);

