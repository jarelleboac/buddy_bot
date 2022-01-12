# Buddy Bot ʕ•́ᴥ•̀ʔっ♡
Fun side project inspired by a bot within Bloomberg L.P's data engineering team. This is a bot which creates random pairs for members of Rutgers WiCS to meet. The goal of this bot is to increase the sense of community within WiCS especially in this remote environment by promoting small group meetups with new people. 

## version 1.0
Created random pairs from a csv file, accounting for odd number of participants. Automated emails sent out on a weekly basis and accounts for different partner pairs (dynamic). 

## Improvements
Keep track of previous weeks' pairs (testing...in a trio, will it be able to see that two people in that group have already met?), create new pair if email bounces back.

## Quickstart
### Running the bot

To do a manual run, navigate to the directory and simply execute the following command:
```
python NAME_OF_PROGRAM.py
```
To do scheduled runs of your email bot, install `hickory`, which is a simple command line tool for scheduling Python scripts:
```
pip install hickory
```

Via command line, navigate to the directory and call hickory schedule with YOUR_PROGRAM_NAME.py as the script argument:
```
hickory schedule src.py --every=10th@9:00am
```
### `--every` Examples

| Repeat                                                  |                          |
| ------------------------------------------------------- | ------------------------ |
| Every ten minutes                                       | `--every=10minutes`      |
| Every day at 10:10 AM                                   | `--every=@10:10`         |
| Every Monday at 10:10 AM                                | `--every=monday@10:10am` |
| Every 10th day of the month at 10:10 AM                 | `--every=10th@10:10am`   |
| Every last day of the month at 10:10 AM                 | `--every=eom@10:10am`    |
| Every 10th and last day of the month at 10 AM and 10 PM | `--every=10,eom@10,10pm` |



### `--every` Table

| Interval         |                                               |
| ---------------- | --------------------------------------------- |
| 10 seconds       | `10`, `10s`, `10sec`, `10secs`, `10seconds`   |
| 10 minutes       | `10m`, `10min`, `10mins`, `10minutes`         |
| 10 hours         | `10h`, `10hr`, `10hrs`, `10hours`             |
| **Time**         |                                               |
| 10:00 AM         | `@10`, `@10am`                                |
| 10:00 PM         | `@22`, `@10pm`                                |
| 10:10 AM         | `@10:10`, `@10:10am`                          |
| 10:10 PM         | `@22:10`, `@10:10pm`                          |
| **Weekday**      |                                               |
| Monday           | `m@`, `mon@`, `monday@`                       |
| Tuesday          | `t@`, `tue@`, `tues@`, `tuesday@`             |
| Wednesday        | `w@`, `wed@`, `weds@`, `wednesday@`           |
| Thursday         | `th@`, `thu@`, `thur@`, `thurs@`, `thursday@` |
| Friday           | `f@`, `fri@`, `friday@`                       |
| Saturday         | `s@`, `sat@`, `saturday@`                     |
| Sunday           | `su@`, `sun@`, `sunday@`                      |
| **Calendar Day** |                                               |
| 1st              | `1@`, `1st@`                                  |
| 2nd              | `2@`, `2nd@`                                  |
| 3rd              | `3@`, `3rd@`                                  |
| 4th              | `4@`, `4th@`                                  |
| 15th             | `15@`, `15th@`                                |
| 31st             | `31@`, `31st@`                                |
| **Other Day**    |                                               |
| Every Day        | `day@`                                        |
| Every Weekday    | `weekday@`                                    |
| End of Month     | `eom@`                                        |

## Helpful Links
https://dev.to/maxhumber/how-to-send-and-schedule-emails-with-python-dnb <br>
https://towardsdatascience.com/how-to-send-beautiful-emails-with-python-the-essential-guide-a01d00c80cd0

