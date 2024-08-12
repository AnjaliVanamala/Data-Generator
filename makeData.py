import random
import math

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
"""
Make_noise, makes n noise taxa properly formatted under treatment m
    number of samples will be determined by sub * sam. 
sub = number of subjects 
sam = number of times a sample is taken from each subject 
t = the treatment 
"""
def make_noise(sub, sam, t, day):
    for i in range(sub):
        for j in range(sam):
            f.write(f"T{i}.{t}\t{day[j]}\t{t}")
            for k in range(num):
                val = random.randrange(0, 5000)
                f.write(f"\t{val}")
            f.write("\n")

"""
find_day, finds the day values and outputs as a list given:
td = distance between time points 
tm = percentage of time points missed
sam = number of times a sample is taken from each subject 
    function logic - sam = the number of timepoints needed = number of 
    values in the list. So to start, I need (1 - tm) * number of values in 
    the list = sam. So the number of values to generate is sam/(1-tm). 
    Then a number of values - sam numbers are randomly deleted from the 
    list. 
"""
def find_day(td, tm, sam):
    nv = int(sam/(1 - tm))
    day = [x for x in range(0, nv*td, td)]
    for i in range(nv-sam):
        # start at zero as one would always get a "before" treatment sample
        de = random.randrange(1, len(day)) 
        del day[de]
    return day

"""
make_taxa, generates the taxa counts given all previous information. 
sub = # of subjects 
sam = # of samples
t = the treatment 
day = list of days 
psm1 = percentage of samples in treatment 1
z1 = list of indexes that should be zeroes 
types1 = type of curve (see types in calc_curve) for treatment 1 
types2 = type of curve for treatment 2
slope1 = "a" value of curve 1 
slope2 = "a" value of curve 2
varc1 = type of curve for variability for treatment 1
varc2 = type of curve for variability for treatment 2
vars1 = "a" value of variability curve 1
vars2 = "a" value of variability curve 2
"""
def make_taxa(sub, sam, t, day, psm1, z1, types1, types2, slope1, slope2, varc1, varc2, vars1, vars2):
    line1 = calc_curve(types1, slope1, sam)
    line2 = calc_curve(types2, slope2, sam)
    var1 = calc_var(varc1, vars1, sam)
    var2 = calc_var(varc2, vars2, sam)
    for i in range(sub*2):
        for j in range(sam):
            f.write(f"T{i}.{t[i]}\t{day[j]}\t{t[i]}")
            if(sub*2*psm1 > i):
                val = abs(line1[j] + var1[j])
            else:
                val = abs(line2[j] + var2[j])
            if (i in z1):
                val = 0
            f.write(f"\t{val}\n")

"""
calc_curve, calculates the list of values for the taxa.
types = the type of curve the taxa growth/counts follow, 0 indicates a 
    horizontal line, 1 is linear, 2 is exponential, and 3 is logarithmic. 
slope = the "a" value of the curve, for horizontal = a, linear = ax, 
    exponential = x^a, logarithmic = log base a of x. 
sam = the number of samples, the x above will go from [0, sam) with each
    x being that index in the list. 
"""
def calc_curve(types, slope, sam):
    if (not types):
        return [slope for x in list(range(sam))]
    elif types == 1:
        return [slope*x for x in list(range(sam))]
    elif types == 2:
        return [x**slope for x in list(range(sam))]
    else:
        return [math.log(x, slope) for x in list(range(sam))]

"""
calc_var, calculates what to add to each taxa count along the specified
    variation. 
types = the type of curve the taxa growth/counts follow, 0 indicates a 
    horizontal line, 1 is linear, 2 is exponential, and 3 is logarithmic. 
slope = the "a" value of the curve, for horizontal = a, linear = ax, 
    exponential = x^a, logarithmic = log base a of x. 
sam = the number of samples, the x above will go from [0, sam) with each
    x being that index in the list. 
"""
def calc_var(types, slope, sam):
    if (not types and not slope):
        return [0 for x in list(range(sam))]
    if (not types):
        return [random.randrange(-1*slope, slope) for x in list(range(sam))]
    elif types == 1:
        return [random.randrange(-1*slope*x, slope*x) for x in list(range(1, sam + 1))]
    elif types == 2:
        return [random.randrange(-1*x**slope, x**slope) for x in list(range(1, sam + 1))]
    else:
        return [random.randrange(-1*math.log(x, slope), math.log(x, slope)) for x in list(range(1, sam + 1))]
    
# all inputs 
random.seed(123)
file = "file" #input("file")
sub, sam, types1, slope1, types2, slope2, varc1, vars1, varc2, vars2, td, noise = [int(x) for x in input("inputs\n").split(" ")]
tm, psm1, pz1 = [float(x) for x in input("inputs\n").split(" ")]
f = open(f"{file}.txt", "w")
f.write("Sample\tDay\tTreatment")
# Check if we want noise
if (noise == 1):
    num = 100 #int(input("how many noise?")) # number of noise taxa
    for i in range(num):
        f.write(f"\tNoiseTaxa{i}")
    f.write("\n")
    # makes noise taxa for treatments 1 and 2 with proper formatting
    day = find_day(td, tm, sam)
    make_noise(sub, sam, 1, day)
    make_noise(sub, sam, 2, day)
    
else:
    f.write("\tTaxa\n")
    t = sorted([(x%2)+1 for x in range(sub*2)])
    z1 = list(range(int(sub*2*psm1)))
    random.shuffle(z1)
    cut = int(math.floor(sub*2*psm1*pz1))
    z1 = z1[0:cut]
    day = find_day(td, tm, sam)
    make_taxa(sub, sam, t, day, psm1, z1, types1, types2, slope1, slope2, varc1, varc2, vars1, vars2)
    
    
f.close()

