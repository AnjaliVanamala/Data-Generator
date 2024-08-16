# Data-Generator
This project is used to generate taxa quickly for an evaluation of current longitudinal packages for the microbiome. 

## Inputs
Inputs are found in the following lines of code:
`file = "file" #input("file")
sub, sam, types1, slope1, types2, slope2, varc1, vars1, varc2, vars2, td, noise = [int(x) for x in input("inputs\n").split(" ")]
tm, psm1, pz1 = [float(x) for x in input("inputs\n").split(" ")]`

The "file" input should be changed to the name of the output file you are expecting. 

Other variable names and their meanings are: <br>
sub = number of subjects <br>
sam = number of times a sample is taken from each subject 
types1 = type of curve for treatment 1 (0 indicates a horizontal line, 1 is linear, 2 is exponential, and 3 is logarithmic.) 
