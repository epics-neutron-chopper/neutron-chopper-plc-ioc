from epics import caget, caput, cainfo, PV
import time
import threading
set_frq = PV("Chopper:SetFrequency.VAL")
curr_frq  = PV("Chopper:GetCurrentFrequency.VAL")
start_frequency = PV("Chopper:AskStartFrequency.VAL")
final_frequency = PV("Chopper:AskEndFrequency.VAL")
nsteps = PV("Chopper:AskNumberOfSteps.VAL")
scan_time = PV("Chopper:AskScanTimeAtEachStep.VAL")
stability_status = PV("Chopper:StabilityAlarm.VAL")
is_scan_enabled = PV("Chopper:EnableSweepProgram.VAL")
scanning_status = PV("Chopper:ScanningStatus.VAL")
run_sweep = PV("Chopper:RunSweepProgram.VAL")

def scanning_function():

    step_size = (final_frequency.get() - start_frequency.get())/nsteps.get()
    set_frq.put(start_frequency.get())
    while stability_status.get() != 0:
        if run_sweep.get() == 0:
            scanning_status.put(0)
            return None
        pass

    scanning_status.put(1)
    for i in range(int(nsteps.get()) + 1):
        if run_sweep.get() == 0:
            scanning_status.put(0)
            return None
        new_setpoint = start_frequency.get() + i * float(step_size)
        set_frq.put(new_setpoint)
        while stability_status.get() != 0:
            if run_sweep.get() == 0:
                scanning_status.put(0)
                return None
            pass

        time.sleep(scan_time.get())

    scanning_status.put(0)
    run_sweep.put(0)



while True:
    if run_sweep.get() == 1:
        scanning_function()
        



        
    

