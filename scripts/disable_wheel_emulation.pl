#!/usr/bin/perl
use warnings;
use strict;

# xinput query-state 11
# xinput list-props 11 

my @xil = split( /\n/, `xinput list`);
my $cnt=0;

foreach my $line (@xil) {
	if ($line =~ m/TouchPad\s+id=(\d+)/) {
		print "$cnt\t$1\t$line\n";
		system(qq{xinput set-prop $1 "Device Enabled" 1});
	}
	if ($line =~ m/TrackPoint\s+id=(\d+)/) {
		print "$cnt\t$1\t$line\n";
		system(qq{xinput set-prop $1 "Evdev Wheel Emulation" 0});
	}
	$cnt++;
}

