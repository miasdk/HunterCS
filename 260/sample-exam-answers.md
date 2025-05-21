# CSCI 260: Computer Architecture
## Sample Final Examination - Solutions

---

## Question 1: Processor Architecture Concepts (10 points)

### a) In a single-cycle MIPS architecture, the clock period must be long enough to accommodate the slowest instruction.

**TRUE**

In a single-cycle architecture, each instruction must complete in exactly one clock cycle. This means that the clock period must be long enough to accommodate the longest-latency instruction path (typically the load word instruction, which requires instruction fetch, register read, ALU operation, data memory access, and register write). All instructions, even simple ones, must wait for this same clock period.

### b) Multi-cycle MIPS generally has a higher CPI than single-cycle MIPS, but can still provide better overall performance.

**TRUE**

In single-cycle MIPS, CPI = 1 by definition. Multi-cycle MIPS breaks instructions into steps, with each instruction taking 3-5 cycles depending on type, resulting in CPI > 1. However, the clock period can be significantly shorter in multi-cycle (determined by the longest individual step rather than the longest complete instruction), which can more than compensate for the increased CPI, leading to better overall performance (execution time = instruction count × CPI × clock period).

### c) In a pipelined architecture, adding more pipeline stages always improves performance.

**FALSE**

Adding more pipeline stages can reduce the clock period by breaking the critical path into smaller segments. However, it also increases hazard penalties, adds pipeline register overhead, and can reduce the amount of useful work done per cycle. Beyond a certain point, these diminishing returns and increased hazards outweigh the benefits of a shorter clock period. There's an optimal number of pipeline stages that balances these factors for a given architecture.

### d) Structural hazards occur when an instruction depends on the result of a previous instruction still in the pipeline.

**FALSE**

This describes a data hazard, not a structural hazard. Structural hazards occur when two instructions need to use the same hardware resource (like memory or register file) simultaneously. Data hazards occur when an instruction depends on data produced by an earlier instruction still in the pipeline. Control hazards occur when the flow of instruction execution depends on the outcome of a branch or jump instruction.

### e) Branch prediction can completely eliminate the performance impact of control hazards.

**FALSE**

While branch prediction can significantly reduce the performance impact of control hazards, it cannot completely eliminate it for two reasons: (1) No prediction mechanism is 100% accurate, and mispredictions still incur penalty cycles, and (2) Even with correct prediction, there's some overhead in the prediction mechanism itself. The best we can do is minimize the impact through increasingly sophisticated prediction techniques.

---

## Question 2: Critical Path Analysis (15 points)

### a) Identify the critical path for an R-type instruction (8 points)

The critical path for an R-type instruction in a single-cycle architecture:

1. PC read: 4 ps
2. Instruction Memory read: 75 ps
3. Register File read: 32 ps
4. ALU operation: 90 ps
5. Register File write: 38 ps

Additional components in the path:
- Control Unit: 5 ps
- MUX for RegisterFile destination selection: 3 ps
- MUX for ALU second input selection: 3 ps

Total critical path delay = 4 + 75 + 5 + 32 + 3 + 90 + 38 = **250 ps**

### b) Identify the critical path for a load (lw) instruction (7 points)

The critical path for a load (lw) instruction:

1. PC read: 4 ps
2. Instruction Memory read: 75 ps
3. Register File read: 32 ps
4. ALU operation (address calculation): 90 ps
5. Data Memory read: 75 ps
6. Register File write: 38 ps

Additional components in the path:
- Control Unit: 5 ps
- MUX for ALU second input: 3 ps
- MUX for Register write data: 3 ps

Total critical path delay = 4 + 75 + 5 + 32 + 3 + 90 + 75 + 3 + 38 = **325 ps**

The load instruction has the longer critical path and would determine the clock period for the single-cycle architecture.

---

## Question 3: Performance Comparison (15 points)

### a) Calculate the maximum clock rate that each architecture can run at. (6 points)

**Single-cycle MIPS:**
The clock period is determined by the longest instruction path, which is the load instruction at 325 ps (from Question 2b).
Maximum clock rate = 1 / 325 ps = **3.077 GHz**

**Multi-cycle MIPS:**
The clock period is determined by the longest individual stage:
- Instruction fetch: PC (4 ps) + Instruction Memory (75 ps) = 79 ps
- Register read: Register File (32 ps) = 32 ps
- ALU operation: ALU (90 ps) + MUX (3 ps) = 93 ps
- Memory access: Data Memory (75 ps) = 75 ps
- Register write: Register File (38 ps) + MUX (3 ps) = 41 ps

The longest stage is ALU operation at 93 ps, which sets the clock period.
Maximum clock rate = 1 / 93 ps = **10.753 GHz**

**Pipelined MIPS:**
The clock period is determined by the slowest pipeline stage, plus overhead for pipeline registers (typically about 5 ps per register).
Longest stage is ALU operation: 93 ps + 5 ps = 98 ps
Maximum clock rate = 1 / 98 ps = **10.204 GHz**

### b) For the multi-cycle MIPS, calculate the average CPI. (3 points)

- R-type instructions (60%): 4 cycles
- Branch instructions (20%): 3 cycles
- Load instructions (12%): 5 cycles
- Store instructions (5%): 4 cycles
- Jump instructions (3%): 3 cycles

Average CPI = (0.60 × 4) + (0.20 × 3) + (0.12 × 5) + (0.05 × 4) + (0.03 × 3)
           = 2.4 + 0.6 + 0.6 + 0.2 + 0.09
           = **3.89 cycles/instruction**

### c) For the pipelined MIPS, calculate the effective CPI. (3 points)

Ideal CPI in a pipelined architecture is 1 cycle/instruction.
Branch frequency = 20%
Branch misprediction rate = 10% (since prediction accuracy is 90%)
Misprediction penalty = 3 cycles

Effective CPI = Ideal CPI + (Branch frequency × Misprediction rate × Penalty)
              = 1 + (0.20 × 0.10 × 3)
              = 1 + 0.06
              = **1.06 cycles/instruction**

### d) Calculate the effective MIPS rating for each architecture when running this benchmark. (3 points)

**Single-cycle MIPS:**
MIPS = Clock rate (MHz) / CPI
     = 3,077 MHz / 1
     = **3,077 MIPS**

**Multi-cycle MIPS:**
MIPS = Clock rate (MHz) / CPI
     = 10,753 MHz / 3.89
     = **2,764 MIPS**

**Pipelined MIPS:**
MIPS = Clock rate (MHz) / CPI
     = 10,204 MHz / 1.06
     = **9,626 MIPS**

The pipelined architecture delivers the highest performance, followed by the single-cycle architecture, with the multi-cycle architecture performing the worst for this particular instruction mix and component delays.

---

## Question 4: Branch Prediction (10 points)

### a) 2-bit saturating counter state transitions (5 points)

Starting from "Strongly Not Taken" (00), the state transitions for the sequence N, N, T, T, T, N, T, N, N:

1. Initial state: Strongly Not Taken (00)
2. Branch outcome N: Stay in Strongly Not Taken (00)
3. Branch outcome N: Stay in Strongly Not Taken (00)
4. Branch outcome T: Move to Weakly Not Taken (01)
5. Branch outcome T: Move to Weakly Taken (10)
6. Branch outcome T: Move to Strongly Taken (11)
7. Branch outcome N: Move to Weakly Taken (10)
8. Branch outcome T: Move to Strongly Taken (11)
9. Branch outcome N: Move to Weakly Taken (10)
10. Branch outcome N: Move to Weakly Not Taken (01)

Final state: Weakly Not Taken (01)

### b) Processor throughput calculation (5 points)

Given:
- Processor clock rate = 3 GHz
- Branch frequency = 18%
- Branch predictor accuracy = 92% (misprediction rate = 8%)
- Misprediction penalty = 4 cycles

Step 1: Calculate effective CPI
Effective CPI = 1 + (Branch frequency × Misprediction rate × Penalty)
              = 1 + (0.18 × 0.08 × 4)
              = 1 + 0.0576
              = 1.0576 cycles/instruction

Step 2: Calculate throughput in MIPS
MIPS = (Clock rate) / (CPI × 10^6)
     = (3 × 10^9) / (1.0576 × 10^6)
     = 3 × 10^3 / 1.0576
     = **2,837 MIPS**

The processor's throughput is approximately 2.837 billion instructions per second.

---

## Question 5: Numeric Representation (10 points)

### a) Convert to IEEE 754 single-precision format (6 points)

#### i) 0.1875

Step 1: Convert to binary
0.1875 = 0.0011 in binary (3/16 = 1/8 + 1/16)

Step 2: Normalize
0.0011 = 1.1 × 2^-3

Step 3: Calculate biased exponent
Exponent = -3 + 127 = 124 = 01111100 in binary

Step 4: Determine sign bit (positive)
Sign bit = 0

Step 5: Extract fraction (mantissa) - remove leading 1
Fraction = 1 (only the digits after the decimal point)

Step 6: Assemble the IEEE 754 format
0 01111100 10000000000000000000000

In hexadecimal: 0x3E400000

#### ii) -24.5

Step 1: Convert to binary
24.5 = 11000.1 in binary (16 + 8 + 0.5)

Step 2: Normalize
11000.1 = 1.10001 × 2^4

Step 3: Calculate biased exponent
Exponent = 4 + 127 = 131 = 10000011 in binary

Step 4: Determine sign bit (negative)
Sign bit = 1

Step 5: Extract fraction (mantissa) - remove leading 1
Fraction = 10001 (the digits after the decimal point)

Step 6: Assemble the IEEE 754 format
1 10000011 10001000000000000000000

In hexadecimal: 0xC1C40000

### b) Represent 6.75 in 16-bit fixed-point Q8.8 format (4 points)

Step 1: Convert the integer part to binary
6 = 110 in binary

Step 2: Convert the fractional part to binary
0.75 = 3/4 = 0.11 in binary

Step 3: Combine parts and pad to appropriate width
Integer part (8 bits): 00000110
Fractional part (8 bits): 11000000

Step 4: Combine
Q8.8 representation: 00000110.11000000 or 0x06C0

---

## Question 6: Custom Instruction Implementation (15 points)

### a) Machine code format for "Swap Memory" (swpm $rt, offset($rs)) (3 points)

Since this instruction uses two registers ($rs and $rt) and an immediate value (offset), the I-type format is most appropriate:

```
| opcode (6 bits) | rs (5 bits) | rt (5 bits) | offset (16 bits) |
```

We would assign a new opcode value that isn't already used by MIPS (e.g., 101101).

### b) Sequence of operations in RTL (4 points)

The swap memory instruction requires the following operations:

1. TEMP ← M[R[rs] + SignExt(offset)]  # Read memory value into temporary register
2. M[R[rs] + SignExt(offset)] ← R[rt]  # Store register value to memory
3. R[rt] ← TEMP                        # Update register with memory value

### c) New datapath elements or modifications needed (4 points)

For a single-cycle implementation, we need:

1. A temporary register to hold the memory value being swapped
2. Additional control path to manage the data flow for the swap operation
3. Modified ALU control to handle the new operation
4. Data path from memory to the temporary register and from the temporary register to the register file

The key addition is the temporary register, which isn't needed for existing MIPS instructions. We also need to modify the control unit to produce the correct sequence of control signals.

### d) Control signal settings for single-cycle MIPS (4 points)

| Control Signal | Value | Explanation |
|----------------|-------|-------------|
| RegDst         | 0     | Destination is rt field |
| ALUSrc         | 1     | ALU uses immediate offset |
| MemtoReg       | 1     | Register value comes from memory |
| RegWrite       | 1     | Enable writing to register file |
| MemRead        | 1     | Enable reading from memory |
| MemWrite       | 1     | Enable writing to memory |
| Branch         | 0     | Not a branch instruction |
| ALUOp          | 00    | ALU performs addition (for address) |
| Jump           | 0     | Not a jump instruction |
| TempRegWrite   | 1     | New signal to enable writing to temporary register |

Note: A single-cycle implementation of this instruction is challenging because it requires sequential memory access (read then write), which contradicts the single-cycle paradigm. In practice, this would likely require a multi-cycle implementation or a more complex memory system that can perform both operations in one cycle.

---

## Question 7: Microcoding Implementation (10 points)

### a) Microcode sequence for jr instruction (6 points)

The `jr` (jump register) instruction loads the PC with the contents of register rs. The microcode sequence would be:

**Microinstruction 1 (Fetch):**
- IorD = 0 (memory address from PC)
- IRWrite = 1 (write instruction to IR)
- ALUSrcA = 0 (ALU input A from PC)
- ALUSrcB = 01 (ALU input B is 4)
- ALUOp = 00 (ALU performs addition)
- PCWrite = 1 (update PC)
- PCSource = 00 (next PC from ALU result)

**Microinstruction 2 (Decode):**
- ALUSrcA = 0 (not used in this state)
- ALUSrcB = 11 (not used in this state)
- ALUOp = 00 (not used in this state)
- NextState = based on opcode/function (to jr execution)

**Microinstruction 3 (Execute jr):**
- ALUSrcA = 1 (ALU input A from register value)
- ALUSrcB = 00 (ALU input B is not used)
- ALUOp = 00 (ALU performs pass-through of A input)
- PCWrite = 1 (update PC)
- PCSource = 00 (next PC from ALU result)

### b) Minimum execution time calculation (4 points)

Assuming microcode implementation with given delays:
- Microinstruction fetch time: 25 ps
- Adder delay: 15 ps

For the jr instruction:
1. Fetch microinstruction: 25 ps
2. Execute fetch (adder for PC+4): 15 ps
3. Fetch next microinstruction: 25 ps
4. Decode (minimal processing): 0 ps (negligible)
5. Fetch next microinstruction: 25 ps
6. Execute jr (adder for register pass-through): 15 ps

Total minimum execution time = 25 + 15 + 25 + 0 + 25 + 15 = **105 ps**

---

## Question 8: Pipeline Hazards and Solutions (15 points)

### a) Identify all data hazards (6 points)

Looking at the instruction sequence:

```
lw    $t0, 0($s0)    # Instruction 1
add   $t1, $t0, $s1  # Instruction 2
sub   $t2, $t1, $s2  # Instruction 3
sw    $t2, 4($s0)    # Instruction 4
beq   $t2, $0, label # Instruction 5
and   $t3, $s3, $s4  # Instruction 6
or    $t4, $s5, $s6  # Instruction 7
```

Data hazards:

1. **RAW hazard between instructions 1 and 2**: Instruction 2 (add) needs $t0, which is being loaded by instruction 1 (lw). This is a load-use hazard.

2. **RAW hazard between instructions 2 and 3**: Instruction 3 (sub) needs $t1, which is being calculated by instruction 2 (add).

3. **RAW hazard between instructions 3 and 4**: Instruction 4 (sw) needs $t2, which is being calculated by instruction 3 (sub).

4. **RAW hazard between instructions 3 and 5**: Instruction 5 (beq) needs $t2, which is being calculated by instruction 3 (sub).

### b) Using forwarding to resolve hazards (5 points)

1. **Hazard between instructions 1 and 2 (load-use hazard)**: 
   - Cannot be fully resolved by forwarding because the data from memory isn't available until after the MEM stage of the lw instruction
   - Requires a stall (discussed in part c)

2. **Hazard between instructions 2 and 3**:
   - Forward from the EX/MEM pipeline register (after instruction 2's EX stage)
   - Forward to the ALU input in instruction 3's EX stage
   - Source: EX/MEM.ALUResult
   - Destination: ALU input A

3. **Hazard between instructions 3 and 4**:
   - Forward from the EX/MEM pipeline register (after instruction 3's EX stage)
   - Forward to the write data input in instruction 4's MEM stage
   - Source: EX/MEM.ALUResult
   - Destination: MEM.WriteData

4. **Hazard between instructions 3 and 5**:
   - Forward from the EX/MEM pipeline register (after instruction 3's EX stage)
   - Forward to the comparator input in instruction 5's EX stage
   - Source: EX/MEM.ALUResult
   - Destination: Branch comparator input A

### c) Hazards that cannot be resolved by forwarding (4 points)

The load-use hazard between instructions 1 and 2 cannot be fully resolved by forwarding alone. This is because:

1. Instruction 1 (lw) loads data from memory in its MEM stage
2. Instruction 2 (add) needs this data in its EX stage
3. In a typical 5-stage pipeline, instruction 2 would be in EX when instruction 1 is in MEM

Since the data isn't available in time, we need to stall the pipeline:
- Stall instruction 2 and all following instructions for one cycle
- This can be implemented by:
  - Holding the IF/ID pipeline register constant (not updating it)
  - Injecting a bubble (NOP) into the ID/EX pipeline register
  - After the stall, forwarding can be used to pass the data from the MEM/WB pipeline register to the ALU input

The pipeline execution with stall:
```
Cycle 1: lw (IF)
Cycle 2: lw (ID), add (IF)
Cycle 3: lw (EX), add (ID)
Cycle 4: lw (MEM), add (ID) [STALL]
Cycle 5: lw (WB), add (EX) [FORWARD]
Cycle 6: sub (ID), add (MEM)
```

---

## BONUS Question: Optimizing Component Delays (5 points)

To determine which component can be slowed down without affecting performance, we need to identify components that are not on the critical path, or that have "slack" in their timing.

From our analysis in Question 2, the critical path for the slowest instruction (load word) is:
PC → Instruction Memory → Register File → ALU → Data Memory → Register File
With a total delay of 325 ps.

Since the Register File write (38 ps) is the last component on this path, we could slow it down without affecting other parts of the critical path. 

The next slower instruction path is for the R-type instructions at 250 ps, which is 75 ps faster than the load instruction. This gives us a "slack" of 75 ps in the Register File write operation.

Therefore, we could slow down the Register File write from 38 ps to 38 + 75 = 113 ps without affecting the overall processor performance. This is a substantial reduction in speed (and thus power) by a factor of almost 3x.

Alternatively, we could slow down the Data Memory read (currently 75 ps) by up to 75 ps to 150 ps, since it's only used in the load instruction which already determines the clock period.

The choice between these two depends on which component consumes more power and would benefit more from being slowed down. Since memory operations typically consume more power than register operations, slowing down the Data Memory would likely provide more power savings.
