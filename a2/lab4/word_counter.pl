#!/usr/bin/perl

my %words=();
my $count = 0;

while (my $line = <>)
{
    foreach my $word (split /\s+/, $line)
    {
        $words{lc($word)}++;
    }
}

# creating array to get sorted values from hash
@word_array=();

for my $word (sort {$words{$b} cmp $words{$a}} keys %words) {
   push(@word_array, $word);}

# creating array for finding hapax legomena
@word_values = values % words;

foreach (@word_values){
   if ($_ == 1){
    $count ++; 
   }
}

print "10 most common words are: ", join(", ", @word_array[0..9]), "\n";
print "The number of hapax legomena is ", $count, "\n";
