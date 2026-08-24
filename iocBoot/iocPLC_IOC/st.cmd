#!../../bin/linux-x86_64/PLC_IOC

#- SPDX-FileCopyrightText: 2003 Argonne National Laboratory
#-
#- SPDX-License-Identifier: EPICS

#- You may have to change PLC_IOC to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/PLC_IOC.dbd"
PLC_IOC_registerRecordDeviceDriver pdbbase


epicsEnvSet("ASYN_PORT",             "ADS_1")
epicsEnvSet("PLC_IP",                "192.168.88.63")
epicsEnvSet("PLC_AMS_NET_ID",        "$(PLC_IP).1.1")
epicsEnvSet("ADS_DEFAULT_PORT",      "851")
epicsEnvSet("PARAM_TABLE_SIZE",      "1000")
epicsEnvSet("PRIORITY",              "0")
epicsEnvSet("DISABLE_AUTOCONNECT",   "0")
epicsEnvSet("DEFAULT_SAMPLETIME_MS", "50")
epicsEnvSet("MAX_DELAY_TIME_MS",     "100")
epicsEnvSet("ADS_TIMEOUT_MS",        "5000")
epicsEnvSet("DEFAULT_TIME_SRC",      "0")

adsAsynPortDriverConfigure(${ASYN_PORT},${PLC_IP},${PLC_AMS_NET_ID},${ADS_DEFAULT_PORT},${PARAM_TABLE_SIZE},${PRIORITY},${DISABLE_AUTOCONNECT},${DEFAULT_SAMPLETIME_MS},${MAX_DELAY_TIME_MS},${ADS_TIMEOUT_MS},${DEFAULT_TIME_SRC})

asynOctetSetOutputEos(${ASYN_PORT}, -1, "\n")
asynOctetSetInputEos(${ASYN_PORT}, -1, "\n")
asynSetTraceMask(${ASYN_PORT}, -1, 0x41)

## Load record instances
dbLoadRecords("db/adsTestAsyn.db","P=Chopper,PORT=${ASYN_PORT},ADSPORT=${ADS_DEFAULT_PORT}", "user=epicsstudent")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=epicsstudent"
