# timelogging
a lighweight library to make a simple timestamp for your logging needs. Because time stamp should not take more than one line of code.

If you don't provide a format it uses [year][month][day]_[hour][minute]. 

If you want your own format, you can either use the datetime library format or you can use one of the following options :
- year2second
- month2second
- month2minute
- year2minute
- year2day
- month2day

for a compact representation of (%Y)%m%d_%H%M(%S). 

It's always better to go in this order since it can be sorted directly by date.