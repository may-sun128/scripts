# Relevent Files 

**Main Files**

- `/home/mholmes/.scripts/sleepy/sleepy.sh`
- `/home/mholmes/.scripts/sleepy/insomnia.sh`
- `/etc/systemd/system/sleepy.service` 

**Symbolic Links**
- `/usr/local/bin/sleepy.sh` -> `/home/mholmes/.scripts/sleepy/sleepy.sh`
- `/home/mholmes/.scripts/sleepy/insomnia.sh` -> `/home/mholmes/.scripts/sleepy/insomnia.sh`

## sleepy.sh

This script takes time-to-sleep[^1] as a paremeter, waits that time, and then calls rtcwake to suspend and set wake time to 06:00. After, it sets volume and calls other scrips.[^2] 

It should be noted that rtcwake requires escalted privilages, hence `make-rtc0-executable.sh` and `sleepy.service`. 

## insomnia.sh

This script sets rtcwake at 06:00 without suspending. It's intended purpose is be run on startup, as opposed to `sleepy.sh`, which is intended to be used anytime during the session.  

## sleepy.service

A systemd unit which changes ownsership of `/dev/rtc0`.
The contents of `sleepy.service` are:

	[Unit]
	Description=changes ownership of /dev/rtc0
	After=multi-user.target

	[Service]
	Type=onceshot
	ExecStart=/usr/bin/chown mholmes:mholmes /dev/rtc0

	[Install] 
	WantedBy=graphical.target

# `visudo` Configuration

The line `mholmes ALL=(ALL) NOPASSWD: /usr/sbin/rtcwake` was added using `visudo` to make `/usr/sbin/rtcwake` callable without `sudo`. This is not enough however, in that reading from `dev/rtc0` needs to have non-privilaged permissions as well. 

Also added /sys/power/state to visudo which, on its own, does not solve the problem of not being able to run `rtcwake` without `su`.

# Permissions w/ `chmod`
`chmod ugo+w /sys/power/state` was run in addition to the visudo alterations. See above. As of right now I'm not sure if this is redundant or if the changes will persist after restart.

# Footnotes

[^1] Not a named parameter, 'time-to-sleep' used for illustrative purposes.
[^2] Subject to change. See *Calls from sleepy.sh and insomnia.sh*.

/usr/sbin/