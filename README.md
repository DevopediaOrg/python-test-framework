# Overview

This is an example project showing the use of Python's `unittest` module. Although the module is meant for unit testing, it can also be used as the building block of a system-level testing framework.

In this example we will control and monitor a Wi-Fi-enabled Raspberry Pi hardware, which is on the same WLAN as the host (laptop) that runs this framework. Raspberry Pi will have SNMP installed and enabled. To interact with the Raspberry Pi over SNMP, we will make use of [PySnmp](http://pysnmp.sourceforge.net/) Python module on the host. For logging and graphing on the host, we will make use of [RRDTool](http://oss.oetiker.ch/rrdtool/).

We have used the following for the project:

* Host: Dell Inspiron N5050 with 4GB RAM, running Ubuntu 14.04 LTS.
* Host: Python 3.4.3. Any later version should also work fine.
* RPI: Raspberry Pi 2 with [TP-Link TL-WN725N 150Mbps Wireless N Nano USB Adapter](http://www.tp-link.com.au/products/details/TL-WN725N.html).

# Getting Started

## Installation

The instructions below are documented for Ubuntu Linux. Do the following on the host:

* Install RRDTool: `sudo apt-get install librrds-perl rrdtool`
* Install PySNMP: `sudo pip3 install pysnmp`

Do the following on Raspberry Pi:

* Install snmp: `sudo apt-get install snmpd snmp`

## Code Organization


## Usage

