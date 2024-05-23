import random

# Number of subjects
# Number of samples
# Zero-inflation percent 
# Variability curve
# Variability coef
# Timepoint curve
# Timepoint coef 
# Type of Curve 
# Coefficient for slope 
# Does treatment have an effect?
# How large is the effect?
# What percentage is the higher effect?
# Noise?

# all inputs 
random.seed(123)
file = input("file")
sub, sam, zero, varc, varcoef, timec, timecoef, curve, coef, treatc, treatcoef, perc, noise = [int(x) for x in input("inputs\n").split(" ")]
f = open(f"{file}.txt", "w")
f.write("Sample\tDay\tTreatment")
# Check if we want noise
if (noise == 1):
    num = int(input("how many noise?"))
    for i in range(num):
        f.write(f"\tNoiseTaxa{i}")
    f.write("\n")
    for i in range(sub):
        Day = 0
        for j in range(sam):
            f.write(f"T{i}.1\t{Day}\t1")
            for k in range(num):
                val = random.randrange(0, 5000)
                f.write(f"\t{val}")
            f.write("\n")
    for i in range(sub):
        Day = 0
        for j in range(sam):
            f.write(f"T{i}.2\t{Day}\t2")
            for k in range(num):
                val = random.randrange(0, 5000)
                f.write(f"\t{val}")
            f.write("\n")

else:
    f.write("Sample\tDay\tTreatment\tTaxa\n")
    
    
    
f.close()

