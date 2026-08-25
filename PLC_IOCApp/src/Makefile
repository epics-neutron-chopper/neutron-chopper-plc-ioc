# SPDX-FileCopyrightText: 2003 Argonne National Laboratory
#
# SPDX-License-Identifier: EPICS

TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = PLC_IOC
# PLC_IOC.dbd will be created and installed
DBD += PLC_IOC.dbd
# PLC_IOC.dbd will be made up from these files:

PLC_IOC_DBD += base.dbd
PLC_IOC_DBD += asyn.dbd
PLC_IOC_DBD += drvAsynIPPort.dbd
PLC_IOC_DBD += asynRecord.dbd
PLC_IOC_DBD += devAsynRecord.dbd
PLC_IOC_DBD += devAsynFloat64.dbd
PLC_IOC_DBD += devAsynOctet.dbd
PLC_IOC_DBD += devAsynOctetLs.dbd
PLC_IOC_DBD += ads.dbd
PLC_IOC_DBD += qsrv.dbd PVAServerRegister.dbd




# Include dbd files from all support applications:
#PLC_IOC_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
PLC_IOC_LIBS += asyn ads qsrv $(EPICS_BASE_PVA_CORE_LIBS)

# PLC_IOC_registerRecordDeviceDriver.cpp derives from PLC_IOC.dbd
PLC_IOC_SRCS += PLC_IOC_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
PLC_IOC_SRCS_DEFAULT += PLC_IOCMain.cpp
PLC_IOC_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#PLC_IOC_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
PLC_IOC_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

