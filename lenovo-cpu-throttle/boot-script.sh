#!/bin/bash

sudo sh -c 'for i in /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor; do echo performance > $i; done'
sudo modprobe msr
sudo wrmsr 0x1FC 2
