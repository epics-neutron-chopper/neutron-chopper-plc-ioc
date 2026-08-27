from epics import caget, caput, cainfo, PV
import time

set_frq = PV("Chopper:SetFrequency.VAL")
curr_frq  = PV("Chopper:GetCurrentFrequency.VAL")
start_frequency = PV("Chopper:AskStartFrequency.VAL")
final_frequency = PV("Chopper:AskEndFrequency.VAL")
nsteps = PV("Chopper:AskNumberOfSteps.VAL")
scan_time = PV("Chopper:AskScanTimeAtEachStep.VAL")
stability_status = PV("Chopper:StabilityAlarm.VAL")
is_scan_enabled = PV("Chopper:EnableSweepProgram.VAL")
scanning_status = PV("Chopper:ScanningStatus.VAL")

def scanning_function():

    step_size = (final_frequency.get() - start_frequency.get())/nsteps.get()
    set_frq.put(start_frequency.get())
    while stability_status.get() != 0:
        pass

    scanning_status.put(1)
    for i in range(int(nsteps.get()) + 1):
        new_setpoint = start_frequency.get() + i * float(step_size)
        set_frq.put(new_setpoint)
        while stability_status.get() != 0:
            pass
        time.sleep(scan_time.get())
#print(scan_time.get())
#print()
scanning_function()
scanning_status.put(0)
#print("Scanning Done")


