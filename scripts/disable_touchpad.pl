#!/usr/bin/perl
use warnings;
use strict;


my @xil = split( /\n/, `xinput list`);
my $cnt=0;

foreach my $line (@xil) {
	if ($line =~ m/TouchPad\s+id=(\d+)/) {
		print "$cnt\t$1\t$line\n";
		system(qq{xinput set-prop $1 "Device Enabled" 0});
	}
	$cnt++;
}

