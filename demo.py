# new version
from PyLTSpice import RawRead

from matplotlib import pyplot as plt

#LTR = RawRead("TRAN - STEP.raw")
LTR = RawRead("/home/astra/Desktop/Draft5.raw")

print(LTR.get_trace_names())
print(LTR.get_raw_property())

#IR1 = LTR.get_trace("I(R1)")
IR1 = LTR.get_trace("V(in)")
IR2 = LTR.get_trace("V(out)")
x = LTR.get_trace('time')  # Gets the time axis
steps = LTR.get_steps()
for step in range(len(steps)):
   # print(steps[step])
   #plt.plot(x.get_time_axis(step), IR1.get_wave(step),label=steps[step])
   plt.plot(x.get_time_axis(step), IR2.get_wave(step),label=steps[step])

plt.legend()  # order a legend
plt.show()
