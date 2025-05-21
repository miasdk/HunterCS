# CSCI 260: Computer Architecture
## Sample Final Examination

**Time: 3 hours**  
**Total Points: 100**

*This exam consists of 8 questions covering single-cycle, multi-cycle, and pipelined MIPS architectures, performance analysis, branch prediction, numeric representation, microcoding, and custom instruction implementation.*

---

## Question 1: Processor Architecture Concepts (10 points)

For each of the following statements, indicate whether it is TRUE or FALSE, and provide a brief explanation (1-2 sentences) for your answer.

a) In a single-cycle MIPS architecture, the clock period must be long enough to accommodate the slowest instruction.

b) Multi-cycle MIPS generally has a higher CPI than single-cycle MIPS, but can still provide better overall performance.

c) In a pipelined architecture, adding more pipeline stages always improves performance.

d) Structural hazards occur when an instruction depends on the result of a previous instruction still in the pipeline.

e) Branch prediction can completely eliminate the performance impact of control hazards.

---

## Question 2: Critical Path Analysis (15 points)

Consider a single-cycle MIPS processor with the following component delays:
- MUX: 3 ps
- Control Unit, ALU Control: 5 ps
- ALU: 90 ps
- Adder: 55 ps
- Registers (PC, etc.): 4 ps read, 6 ps write
- Memory (data, instruction): 75 ps read, 85 ps write
- Register File: 32 ps read, 38 ps write

a) Identify the critical path for an R-type instruction (8 points)

b) Identify the critical path for a load (lw) instruction (7 points)

For each path, list the components traversed and calculate the total delay.

---

## Question 3: Performance Comparison (15 points)

Consider three implementations of the MIPS architecture (single-cycle, multi-cycle, and pipelined) with the component delays given in Question 2. The instruction mix for a benchmark program is:
- 60% R-type
- 20% branch
- 12% load
- 5% store
- 3% jump

a) Calculate the maximum clock rate that each architecture can run at. (6 points)

b) For the multi-cycle MIPS, assume R-type instructions take 4 cycles, loads take 5 cycles, stores take 4 cycles, branches take 3 cycles, and jumps take 3 cycles. Calculate the average CPI. (3 points)

c) For the pipelined MIPS, assume a branch prediction accuracy of 90% with a 3-cycle penalty for misprediction. Calculate the effective CPI. (3 points)

d) Calculate the effective MIPS rating for each architecture when running this benchmark. (3 points)

---

## Question 4: Branch Prediction (10 points)

a) A pipelined processor uses a 2-bit saturating counter for branch prediction. Starting from the "Strongly Not Taken" state, show the state transitions for the following sequence of branch outcomes (T = taken, N = not taken): N, N, T, T, T, N, T, N, N. (5 points)

b) In a pipelined MIPS processor running at 3 GHz, branch instructions account for 18% of all instructions. The branch predictor has an accuracy of 92%, and each misprediction results in a 4-cycle penalty. What is the processor's throughput in MIPS (Million Instructions Per Second)? (5 points)

---

## Question 5: Numeric Representation (10 points)

a) Convert the following decimal numbers to IEEE 754 single-precision floating-point format. Show your work, including the sign bit, exponent (with bias), and fraction. (6 points)
   i) 0.1875
   ii) -24.5

b) Represent the decimal number 6.75 in a 16-bit fixed-point format with 8 bits for the integer part and 8 bits for the fractional part (Q8.8). Show your work. (4 points)

---

## Question 6: Custom Instruction Implementation (15 points)

Consider a new instruction for the MIPS architecture called "Swap Memory" (swpm $rt, offset($rs)). This instruction swaps the contents of register $rt with the contents of the memory location at address $rs + offset.

a) Design the machine code format for this instruction. (3 points)

b) List the sequence of operations required to execute this instruction in RTL (Register Transfer Language). (4 points)

c) For a single-cycle implementation, identify any new datapath elements or modifications needed. (4 points)

d) Complete the control signal settings for this instruction in the single-cycle MIPS control table. (4 points)

---

## Question 7: Microcoding Implementation (10 points)

Consider the implementation of the jr (jump register) instruction using microcoding.

a) Write the microcode sequence required to implement the jr instruction on a multi-cycle MIPS processor. For each microinstruction, specify the control signals that would be active. (6 points)

b) Assuming that microcoded control has a microinstruction fetch time of 25 ps and an adder delay of 15 ps (everything else is negligible), calculate the minimum execution time for the jr instruction. (4 points)

---

## Question 8: Pipeline Hazards and Solutions (15 points)

Consider the following sequence of MIPS instructions:

```
lw    $t0, 0($s0)    # Load word from memory at address $s0 into $t0
add   $t1, $t0, $s1  # $t1 = $t0 + $s1
sub   $t2, $t1, $s2  # $t2 = $t1 - $s2
sw    $t2, 4($s0)    # Store $t2 to memory at address $s0 + 4
beq   $t2, $0, label # Branch to label if $t2 equals zero
and   $t3, $s3, $s4  # $t3 = $s3 & $s4
or    $t4, $s5, $s6  # $t4 = $s5 | $s6
```

a) Identify all data hazards in this instruction sequence. For each hazard, specify the type and the instructions involved. (6 points)

b) Show how forwarding can be used to resolve the data hazards. For each forwarding case, indicate the source and destination of the forwarded data. (5 points)

c) Identify any hazards that cannot be resolved by forwarding alone and explain how they would be handled. (4 points)

---

## BONUS Question: Optimizing Component Delays (5 points)

In the processor described in Question 2, your design team needs to reduce power consumption by slowing down one component. Which component would you choose to slow down, and by how much could it be slowed without affecting the overall performance? Justify your answer with calculations.

---

## End of Examination

